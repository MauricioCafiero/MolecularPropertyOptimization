import time
import pubchempy as pcp
import requests


def is_commercially_available(smiles_list: list[str]) -> str:
    """Uses PubChemPy to look up chemicals by SMILES, then uses the PUG-View
    annotation API to retrieve commercial suppliers for each. Returns a string
    summarizing the commercial availability for each SMILES in the list.

      Args:
        smiles_list: A list of SMILES strings to look up.

      Returns:
        A string summarizing the commercial availability for each SMILES in the list.
    """
    all_results = []

    for smiles in smiles_list:
        try:
            # Step 1: Use PubChemPy to find the Compound ID (CID) from the SMILES
            compounds = pcp.get_compounds(smiles, "smiles")
            if not compounds:
                all_results.append(f"Chemical with SMILES '{smiles}' not found in PubChem.")
                continue

            cid = compounds[0].cid
            # Add a check here for cid being None
            if cid is None:
                all_results.append(f"Result: SMILES '{smiles}' is not commercially available or no vendor data found.")
                continue

            # print(f"Found CID {cid} for SMILES '{smiles}'. Retrieving vendors...")

            # Step 2: Query the PUG-View API for the compound's data
            url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON"

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 404:
                all_results.append(f"SMILES '{smiles}' (CID {cid}): No data found.")
                continue

            if response.status_code == 400:
                all_results.append(f"SMILES '{smiles}' (CID {cid}): PUGVIEW.BadRequest: {response.text}")
                continue

            response.raise_for_status()
            data = response.json()

            # Recursive helper function to check for existence of vendor information
            def contains_vendor_info(obj):
                if isinstance(obj, dict):
                    # If there are any 'Information' blocks, it implies vendor data
                    if obj.get("Information"): # Checks if the list of Information blocks is non-empty
                        return True
                    # Recursively search in nested 'Section' lists
                    for sub_section in obj.get("Section", []):
                        if contains_vendor_info(sub_section):
                            return True
                elif isinstance(obj, list):
                    for item in obj:
                        if contains_vendor_info(item):
                            return True
                return False

            # Start search from the top-level sections
            top_sections = data.get("Record", {}).get("Section", [])
            is_available = False
            for section in top_sections:
                if section.get("TOCHeading") == "Chemical Vendors":
                    # Check if this section or its subsections contain any vendor info
                    if contains_vendor_info(section):
                        is_available = True
                        break # Found vendor data

            if is_available:
                all_results.append(f"SMILES '{smiles}' is commercially available.")
            else:
                all_results.append(f"SMILES '{smiles}' is not commercially available or no vendor data found.")

        except pcp.PubChemHTTPError as e:
            all_results.append(f"SMILES '{smiles}': PubChemPy API error: {e}")
        except requests.exceptions.RequestException as e:
            all_results.append(f"SMILES '{smiles}': Network error querying vendor data: {e}")
        except Exception as e:
            all_results.append(f"SMILES '{smiles}': An unexpected error occurred: {e}")
        finally:
            # Stay compliant with PubChem's 5 requests-per-second limit
            time.sleep(0.5)
    
    return "\n".join(all_results)