import sqlite3
import pandas as pd
from typing import Dict, List, Tuple, Any

def connect_database():
    """Connect to the molecules database"""
    conn = sqlite3.connect('../data/gen_molecules.db')
    return conn

def get_column_info() -> Dict[str, str]:
    """Get column names and their types from the database"""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(molecules)")
    columns = cursor.fetchall()
    conn.close()
    
    column_info = {}
    for col in columns:
        col_name = col[1]
        col_type = col[2]
        column_info[col_name] = col_type
    
    return column_info

def display_columns(column_info: Dict[str, str]):
    """Display available columns in the database"""
    print("\n" + "="*60)
    print("AVAILABLE COLUMNS IN DATABASE")
    print("="*60)
    for i, (col_name, col_type) in enumerate(column_info.items(), 1):
        print(f"{i}. {col_name:<20} (Type: {col_type})")
    print("="*60 + "\n")

def select_columns(column_info: Dict[str, str]) -> List[str]:
    """Allow user to select which columns to query"""
    col_list = list(column_info.keys())
    selected = []
    
    print("Select columns to query (comma-separated numbers, or 'all' for all columns):")
    user_input = input("Enter selection: ").strip().lower()
    
    if user_input == 'all':
        selected = col_list
    else:
        try:
            indices = [int(x.strip()) - 1 for x in user_input.split(',')]
            selected = [col_list[i] for i in indices if 0 <= i < len(col_list)]
        except (ValueError, IndexError):
            print("Invalid selection. Using all columns.")
            selected = col_list
    
    return selected

def get_thresholds(selected_columns: List[str], column_info: Dict[str, str]) -> Dict[str, Tuple[str, Any]]:
    """Get threshold criteria for selected columns"""
    thresholds = {}
    numeric_types = {'REAL', 'INTEGER'}
    
    print("\nSet thresholds for filtering (press Enter to skip a column):")
    print("-" * 60)
    
    for col in selected_columns:
        if col == 'id':  # Skip ID column
            continue
        
        col_type = column_info[col]
        
        if col_type in numeric_types:
            print(f"\nFor column '{col}' (numeric):")
            print("  Enter operator and value, e.g., '> 0.5' or '= SMILES_value'")
            print("  Operators: >, <, >=, <=, =, !=")
            user_input = input(f"  Threshold for {col}: ").strip()
            
            if user_input:
                # Parse operator and value
                for op in ['>=', '<=', '!=', '=', '>', '<']:
                    if user_input.startswith(op):
                        value = user_input[len(op):].strip()
                        thresholds[col] = (op, value)
                        break
        else:  # Text column
            print(f"\nFor column '{col}' (text):")
            user_input = input(f"  Filter value for {col} (e.g., partial match): ").strip()
            
            if user_input:
                thresholds[col] = ('LIKE', f'%{user_input}%')
    
    return thresholds

def build_query(selected_columns: List[str], thresholds: Dict[str, Tuple[str, Any]]) -> Tuple[str, List[Any]]:
    """Build SQL query based on selected columns and thresholds"""
    columns_str = '*'
    
    where_clauses = []
    params = []
    
    for col, (op, value) in thresholds.items():
        if op == 'LIKE':
            where_clauses.append(f"{col} {op} ?")
            params.append(value)
        else:
            # Try to convert to number if it's a numeric operator
            try:
                numeric_value = float(value) if '.' in str(value) else int(value)
                where_clauses.append(f"{col} {op} ?")
                params.append(numeric_value)
            except ValueError:
                # If conversion fails, treat as string
                where_clauses.append(f"{col} {op} ?")
                params.append(value)
    
    query = f"SELECT {columns_str} FROM molecules"
    
    if where_clauses:
        query += " WHERE " + " AND ".join(where_clauses)
    
    query += " ORDER BY id"
    
    return query, params

def execute_query(query: str, params: List[Any]) -> pd.DataFrame:
    """Execute the query and return results as a DataFrame"""
    conn = connect_database()
    try:
        df = pd.read_sql_query(query, conn, params=params)
        return df
    finally:
        conn.close()

def display_results(df: pd.DataFrame):
    """Display query results in a nicely formatted table"""
    if df.empty:
        print("\n" + "!"*60)
        print("No rows found matching your criteria.")
        print("!"*60 + "\n")
    else:
        print("\n" + "="*60)
        print(f"QUERY RESULTS - {len(df)} rows found")
        print("="*60)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(df.to_string(index=False))
        print("="*60 + "\n")

def main():
    """Main function to run the database query tool"""
    print("\n" + "="*60)
    print("MOLECULE DATABASE QUERY TOOL")
    print("="*60)
    
    # Get and display available columns
    column_info = get_column_info()
    display_columns(column_info)
    
    # Select columns to query
    selected_columns = select_columns(column_info)
    print(f"\nSelected columns: {', '.join(selected_columns)}")
    
    # Get threshold criteria
    thresholds = get_thresholds(selected_columns, column_info)
    
    if thresholds:
        print("\nApplied filters:")
        for col, (op, val) in thresholds.items():
            print(f"  {col} {op} {val}")
    else:
        print("\nNo filters applied - retrieving all rows.")
    
    # Build and execute query
    query, params = build_query(selected_columns, thresholds)
    print(f"\nExecuting query...")
    
    df = execute_query(query, params)
    
    # Display results
    display_results(df)

if __name__ == "__main__":
    main()
