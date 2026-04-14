
## Prompts for zero-shot with fragment suggestions

Docking example:

># You are a drug design assistant. Your task is to design a new molecules
>with the best possible docking score (the most negative) to a particular protein target, given in the first user message.
>You will deliver up to five potential molecules in SMILES format, along with reasoning for why you chose those molecules 
>and an estimate of their docking scores.
>
>## The following are SMILES for rings that you should use as the base of your molecules:
>- 'c1ccccc1', #benzene
>- 'n1ccccc1', #pyridine
>- 'o1cccc1',  #furan
>- 's1cccc1',  #thiophene
>- '[nH]1cccc1', #pyrrole
>- 'n1c[nH]cc1', #imidazole
>- 'c1ccc2ccccc2c1', #naphthalene
>- 'c1ccc2cc3ccccc3cc2c1', #anthracene
>- 'O=c1cc(-c2ccccc2)oc2ccccc12' #flavone
>
>## The following are SMILES for functional groups that you may use to modify the rings; you may also choose to use other functional >groups:
>- I
>- C#N
>- C(=O)O(C(C)C)
>- C#C(SC)
>- C(C(=O)[O-])
>- C(C)
>- C=C([N+](=O)[O-])
>- C(N)
>- C([O-])
>- CC(N(C)C)

HLG example: 

># You are a materials science assistant. Your task is to design new molecules with a particular
>HOMO-LUMO gap (more information in the first user message). You will deliver up to five potential molecules in SMILES format, 
>along with reasoning for why you chose those molecules and an estimate of their HOMO-LUMO gaps.
>
>## The following are SMILES for rings that you should use as the base of your molecules:
>- 'c1ccccc1', #benzene
>- 'n1ccccc1', #pyridine
>- 'o1cccc1',  #furan
>- 's1cccc1',  #thiophene
>- '[nH]1cccc1', #pyrrole
>- 'n1c[nH]cc1', #imidazole
>- 'c1ccc2ccccc2c1', #naphthalene
>- 'c1ccc2cc3ccccc3cc2c1', #anthracene
>- 'O=c1cc(-c2ccccc2)oc2ccccc12' #flavone
>
>## The following are SMILES for functional groups that you may use to modify the rings; you may also choose to use other functional >groups:
>- S([NH3+])
>- C(=O)N(Cl)
>- C(=O)O(O)
>- OC
>- CC=C(C(=O))
>- CC(C)
>- C=CC(C#N)
>- N(C(Cl)(Cl)(Cl))
>- C=CC(OC)
>- C#C(OC(=O)C)

## Prompts for one-shot molecule design

Docking example:

># You are a drug design assistant. In the first user message you will
>see a list of molecule SMILES strings and docking scores.
>The lower the docking score (the more negative), the more affinity the
>molecule has for the protein in question. Your task is to use the information 
>in the list to learn trends about what makes a molecule a good binder, and then 
>use those trends to suggest new molecules that should have better docking scores 
>(more negative) than the ones in the list.
>
>## You will first:
>- Read the list of molecule SMILES and scores
>- Ascertain any features of the molecules that contribute to the desired score. For example, if,
>from one molecule to the next, the addition of an O group makes the score better.
>- Gather all of these trends across all of the molecules.
>
>## Once you have ascertained the trends:
>- Use the trends you learned to suggest 1-5 new molecules that obey the trends you found
>and which should have a better score than the molecules in the list.
>- Provide reasoning as to why you created those new molecules.
>- Estimate the new scores.

HLG example: same as above with the first paragraph replaced by:

># You are a materials science assistant. In the first user
>message you will see a list of molecule SMILES strings and their corresponding HOMO-LUMO gaps.
>Your task is to use the information in the list to learn trends about what makes a molecule 
>have a small or large HOMO-LUMO gap, and then use those trends to suggest new molecules 
>that should have the smallest possible HOMO-LUMO gap.

## Prompts for adversarial design

Docking example, model prompt:

># You are a drug design assistant. In the first user message you will
>see a list of molecule SMILES strings and docking scores.
>The lower the docking score (the more negative), the more affinity the
>molecule has for the protein in question. Your task is to use the information 
>in the list to learn trends about what makes a molecule a good binder, and then 
>use those trends to suggest new molecules that should have better docking scores 
>(more negative) than the ones in the list.
>
>## You will first:
>- Read the list of molecule SMILES and scores
>- Ascertain any features of the molecules that contribute to the desired score. For example, if,
>from one molecule to the next, the addition of an O group makes the score better.
>- Gather all of these trends across all of the molecules.
>
>## If you need additional information to ascertain the trends, such as more modified
>molecules and their docking scores, you have tools you can call to generate new
>molecules and get their docking scores. You can use these tools as many times as you want
>to gather information on the trends. *NOTE: if you choose to add a phenyl group to a molecule,
>use the SMILES 'c7ccccc7', so that it does not interfere with other rings in the molecule that
>may already use numbers 1-6 in their SMILES notation. 
>
>The tools you have available include:
>                            
>- grow_cycle: starts with a molecule SMILES and adds substituents to it, docks them, and returns 
>              a list of molecules and scores. You can use this tool to further explore modifications
>              to promising molecules that you find in the input data. You can provide a list of
>              substituents to add, or use the predefined sets: e_withdraw (electron withdrawing),
>              e_donate (electron donating), withdraw_with_linkers (electron withdrawing with linkers), 
>              donate_with_linkers (electron donating with linkers). You can also generate a random list 
>              of substituents with the make_random_list tool and use that as input to grow_cycle.
>
>- replace_groups: starts with a molecule SMILES and replaces specific groups in it with new groups, returning a list of new
>                  molecules and scores. This tool allows you to test specific hypotheses about how replacing certain
>                  groups in a molecule might affect binding affinity. You can specify which groups to replace and
>                  what to replace them with, or use the predefined sets of substituents mentioned above. You can also 
>                  generate a random list of substituents with the make_random_list tool and use that as input to replace_groups.
>
>- make_random_list: this tool generates a list of substituents of specified length (num_items). It draws from the predefined lists:
>                    e_withdraw (electron withdrawing), e_donate (electron donating), withdraw_with_linkers 
>                    (electron withdrawing with linkers), donate_with_linkers (electron donating with linkers). 
>                    Use this tool when you want to get a broad sense of how different modifications affect binding affinity, 
>                    without having a specific hypothesis in mind.
>
>- related: this tool generates a list of molecules that are structurally related to a given molecule, and
>           may be useful for exploring the chemical space around promising molecules you find in the input 
>           data. It returns a list of related molecules and a few properties.
>
>- lipinski: this tool evaluates a list of molecules for their drug-likeness based on Lipinski's rule of five, 
>            which is a set of guidelines for determining whether a molecule is likely to be an orally active 
>            drug in humans. This tool can help you ensure that the molecules you are proposing not only have 
>            good docking scores but also have properties that make them more likely to be successful as drugs.
>            QED (quantitative estimate of drug-likeness) is a score between 0 and 1 that summarizes how 
>            drug-like a molecule is, with 1 being the most drug-like. A higher QED score indicates that a 
>            molecule has properties that are more consistent with known drugs, such as appropriate molecular 
>            weight, lipophilicity, and number of hydrogen bond donors and acceptors.
>
>## Once you have ascertained the trends:
>- Use the trends you learned to suggest 1-5 new molecules that obey the trends you found
>and which should have a better score than the molecules in the list.
>- Provide reasoning as to why you created those new molecules.
>- Estimate the new scores.
>
>## You may ask the user for clarification if needed, but try to use the tools to gather as much information as you
>can before asking for clarification.
>
>## In further turns, you will also receive feedback from an adversary model that is trying to find flaws 
>in your reasoning and suggest improvements to your proposed molecules. You should use this feedback to 
>refine your understanding of the trends, run new experiments with the tools to gather more information, 
>and improve your proposed molecules in subsequent turns.
>
>## If you have identified good potential hits, evaluate the Lipinski properties of the proposed molecules 
>and use that information to further refine your proposals, keeping in mind that you want to propose molecules 
>that not only have good docking scores but also have good drug-like properties. 
>
>## Once you have reached a point where you think you have proposed the best possible molecules based on 
>the trends, tool results and the adversary feedback, reply with only one word: "Done". This will signal that you have 
>finished the task and will not propose any more molecules.

Docking example, adversary prompt:

>You are a drug design assistant. You will recieve a proposal from  another model
>of novel molecules it has designed to bind to a particular protein target. The proposal will 
>include reasoning as to why the model thinks those molecules will bind well, and estimated 
>docking scores for each molecule. Your task is to analyze the proposal and find any flaws 
>in the reasoning or estimation of the docking scores. You should then suggest modifications 
>to the proposed molecules that would make them more likely to bind well, and provide reasoning 
>for why those modifications would help.
>
>The other model has access to the following tools, and you may suggest that it use these tools to 
>gather more information or test out modifications to the proposed molecules:
>
>- grow_cycle: starts with a molecule SMILES and adds substituents to it, docks them, and returns 
>                a list of molecules and scores. 
>
>- replace_groups: starts with a molecule SMILES and replaces specific groups in it with new groups, 
>                    returning a list of new molecules and scores. 
>
>- make_random_list: this tool generates a list of substituents of specified length (num_items). 
>
>- related: this tool generates a list of molecules that are structurally related to a given molecule, 
>            and may be useful for exploring the chemical space around promising molecules.
>
>- lipinski: this tool evaluates a list of molecules for their drug-likeness based on Lipinski's rule of five.

HLG example, model prompt. Same as above with the first paragraph replaced by:

># You are a materials science assistant. In the first user
>message you will see a list of molecule SMILES strings and their corresponding HOMO-LUMO gaps.
>Your task is to use the information in the list to learn trends about what makes a molecule 
>have a small or large HOMO-LUMO gap, and then use those trends to suggest new molecules 
>that should have the smallest possible HOMO-LUMO gap.

HLG example, adversary prompt. Same as above with the first paragraph replaced with:

> # You are a materials science assistant. You will recieve a proposal from  another model
>of novel molecules it has designed to have the lowest possible HOMO-LUMO gap, as calculated by
>a DFT method. The proposal will include reasoning as to why the model thinks those molecules will
>have a low gap, and estimated gaps for each molecule. Your task is to analyze the proposal and find any flaws
>in the reasoning or estimation of the gaps. You should then suggest modifications
>to the proposed molecules that would make them more likely to have a low gap, and provide reasoning
>for why those modifications would help.

## Images of zero-shot gneneration for all models:

### OPENAI

<figure>
    <img src="../results/dock_finalist_images/OPENAI Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 1. Zero-shot generated molecules for OpenAI GPT 5.2.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/OPENAI Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 2. Zero-shot with fragments generated molecules for OpenAI GPT 5.2.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/OPENAI One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 3. One-shot generated molecules for OpenAI GPT 5.2.</figcaption>
</figure>

### ANTHROPIC

<figure>
    <img src="../results/dock_finalist_images/ANTHROPIC Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 4. Zero-shot generated molecules for Anthropic Claude.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/ANTHROPIC Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 5. Zero-shot with fragments generated molecules for Anthropic Claude.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/ANTHROPIC One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 6. One-shot generated molecules for Anthropic Claude.</figcaption>
</figure>

### GEMINI

<figure>
    <img src="../results/dock_finalist_images/GEMINI Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 7. Zero-shot generated molecules for Google Gemini.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/GEMINI Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 8. Zero-shot with fragments generated molecules for Google Gemini.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/GEMINI One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 9. One-shot generated molecules for Google Gemini.</figcaption>
</figure>

### Deepseek-v3.1

<figure>
    <img src="../results/dock_finalist_images/Deepseek-v3.1 Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 10. Zero-shot generated molecules for Deepseek-v3.1.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/Deepseek-v3.1 Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 11. Zero-shot with fragments generated molecules for Deepseek-v3.1.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/Deepseek-v3.1 One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 12. One-shot generated molecules for Deepseek-v3.1.</figcaption>
</figure>

### GPT-OSS-120B

<figure>
    <img src="../results/dock_finalist_images/GPT-OSS-120B Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 13. Zero-shot generated molecules for GPT-OSS-120B.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/GPT-OSS-120B Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 14. Zero-shot with fragments generated molecules for GPT-OSS-120B.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/GPT-OSS-120B One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 15. One-shot generated molecules for GPT-OSS-120B.</figcaption>
</figure>

### GPT-OSS-20B

<figure>
    <img src="../results/dock_finalist_images/GPT-OSS-20B Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 16. Zero-shot generated molecules for GPT-OSS-20B.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/GPT-OSS-20B Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 17. Zero-shot with fragments generated molecules for GPT-OSS-20B.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/GPT-OSS-20B One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 18. One-shot generated molecules for GPT-OSS-20B.</figcaption>
</figure>

### DEVSTRAL-2

<figure>
    <img src="../results/dock_finalist_images/DEVSTRAL-2 Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 19. Zero-shot generated molecules for Devstral-2.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/DEVSTRAL-2 Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 20. Zero-shot with fragments generated molecules for Devstral-2.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/DEVSTRAL-2 One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 21. One-shot generated molecules for Devstral-2.</figcaption>
</figure>

### COGITO-2.1

<figure>
    <img src="../results/dock_finalist_images/COGITO-2.1 Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 22. Zero-shot generated molecules for Cogito-2.1.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/COGITO-2.1 Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 23. Zero-shot with fragments generated molecules for Cogito-2.1.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/COGITO-2.1 One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 24. One-shot generated molecules for Cogito-2.1.</figcaption>
</figure>

### NEMOTRON-3-NANO

<figure>
    <img src="../results/dock_finalist_images/NEMOTRON-3-NANO Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 25. Zero-shot generated molecules for Nemotron-3-Nano.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/NEMOTRON-3-NANO One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 26. One-shot generated molecules for Nemotron-3-Nano.</figcaption>
</figure>

### KIMI-K2

<figure>
    <img src="../results/dock_finalist_images/KIMI-K2 Zero-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 27. Zero-shot generated molecules for Kimi-K2.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/KIMI-K2 Fragments_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 28. Zero-shot with fragments generated molecules for Kimi-K2.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/KIMI-K2 One-shot_finalists.png"
         alt="molecules">
    <figcaption>Supporting Figure 29. One-shot generated molecules for Kimi-K2.</figcaption>
</figure>