## Three models have been used in one-shot and adversarial turn-by-turn design sessions to create molecules that have the lowest possible docking score for the enzyme HMGCR. The models are: 

1. OPENAI's GPT5.2
2. Anthropic's Claude
3. Google's Gemini-3-flash

## In addition, some other models were used for one-shot only design. These were:

1. deepseek-v3.1:671b
2. gpt-oss:120b
3. gpt-oss:20b
4. devstral-2:123b
5. cogito-2.1:671b
6. nemotron-3-nano:30b
7. gemini-3-flash-preview
8. kimi-k2:1t

## In the results folder you will find:

1. dock_verify.out : this file has verified docking scores for the one-shot and adversarial sessions for the main models.

2. lipisnki_for_dock_leads.out : this file has Lipinski properties for the one-shot and adversarial sessions for the main models.

3. dock_finalist_images : this folder contains images for the one-shot and adversarial sessions for the main models.

4. ONE_SHOT/one_shots.out : this file contains verified docking scores for the one-shot sessions for the additional models.

5. GPT_FIRST/adversary_design_2026-03-20_10-55-04.md: the turn-by turn design where GPT5.2 leads and has access to tools, and Claude is the adversary.

6. ANT_FIRST/adversary_design_2026-04-01_10-27-25.md: the turn-by turn design where Claude leads and has access to tools, and GPT5.2 is the adversary.

7. GEMINI_FIRST/adversary_design_2026-03-24_08-21-17.md: the turn-by turn design where Gemini leads and has access to tools, and Claude is the adversary.

## Use all of these resources to put together a summary markdown document that describes the strengths and weaknesses of each model/session, compares one-shot to adversarial design, and includes the verified scores, Lipinksi properties, and images where appropriate. 



