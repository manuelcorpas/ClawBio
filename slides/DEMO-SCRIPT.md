# Live Demo Script — PharmGx First, Then Ancestry PCA

Total demo time: ~5 minutes across both skills.

## Pre-Demo Checklist (do before the talk)

```bash
# Terminal setup
cd ~/ClawBio/examples
clear

# Test PharmGx (should complete in <1 sec)
python3 ../skills/claw-pharmgx/pharmgx_reporter.py \
    --input ../skills/claw-pharmgx/demo_patient.txt \
    --output /tmp/test_pharmgx

# Test Ancestry PCA (should complete in <5 sec with --demo flag)
python3 ../skills/claw-ancestry-pca/ancestry_pca.py \
    --demo \
    --output /tmp/test_ancestry

# Clean up
rm -rf /tmp/test_pharmgx /tmp/test_ancestry

# Pre-open both reports in browser tabs
# Tab 1: skills/claw-pharmgx/demo_report/report.md
# Tab 2: Ancestry PCA figure in slides/img/ancestry_pca_composite.png
```

## Font Size

Set terminal font to 24pt+ so the back row can read it.

```bash
# macOS Terminal: Cmd+Shift+. to increase font size
# iTerm2: Cmd+= to zoom in
```

---

## DEMO 1: PharmGx Reporter (the gasp moment)

### Setup (what to say before typing)

Say: "Here's the scenario. I just got my 23andMe results back. I want to know which drugs might not work for me. With ChatGPT, I'd spend 45 minutes debugging hallucinated star alleles. With ClawBio, I type one command."

### Step 1: Run it

```bash
python3 ../skills/claw-pharmgx/pharmgx_reporter.py \
    --input ../skills/claw-pharmgx/demo_patient.txt \
    --output pharmgx_report
```

It finishes in under 1 second. Let the speed land.

### Step 2: Walk through the output

Point to the terminal as results appear:
- "CYP2D6 *4/*4 — Poor Metabolizer. This is the headline."
- "10 drugs flagged AVOID. Codeine won't work. Your body can't convert it to morphine."
- "20 drugs flagged CAUTION. Warfarin needs dose adjustment."
- "21 drugs are fine."

Say: "I didn't tell the tool which genes to check. I didn't specify which guidelines to follow. That domain knowledge is baked into the ClawBio skill. This is what 'a domain expert's judgement, frozen into code' actually means."

### Step 3: Switch to slides (15-17)

Advance to Slide 15 (terminal output fallback), then 16 (gene table), then 17 (why PGx matters).

Key line on Slide 17: "7% of people in this room might be CYP2D6 poor metabolizers. If you take codeine after surgery, you get zero pain relief."

Then: "That was the personal level. Now let me zoom out to the global picture."

---

## DEMO 2: Ancestry PCA (the zoom-out)

### Step 1: Introduce it

Say: "Second skill. Same principle — one command, works out of the box. But instead of 'what drugs won't work for me?', the question is 'where does my cohort sit in global genetic space?'"

"The reference panel is the Simons Genome Diversity Project: 345 samples from 164 populations spanning every inhabited continent."

### Step 2: Run it

```bash
python3 ../skills/claw-ancestry-pca/ancestry_pca.py \
    --demo \
    --output ancestry_report
```

Say while waiting: "Same idea. One command. It finds common variants between your cohort and SGDP, runs PCA on the merged set, and generates a publication-quality 4-panel figure."

### Step 3: Walk through the figure

Switch to Slide 19 (full figure). Point to each panel:
- "Top-left: PC1 vs PC2 — internal structure of 28 Peruvian indigenous populations"
- "Top-right: regional groupings — Highland, Amazonian, Coastal"
- "Bottom-left: linguistic groupings — Quechua and Aymara"
- "Bottom-right — the money shot: Peru vs 164 global populations. Circles are Peru, triangles are SGDP."

### Step 4: Land the reproducibility message (Slide 20)

"That figure is from a paper we're writing on the Peruvian Genome Project. When we publish, anyone can reproduce it with one command. Not 'code available on GitHub' — one command, identical figure, checksums to prove it."

### Step 5: Advance to Slide 21 (Reproducibility Is Broken)

"How many of you have tried to reproduce a figure from a published paper using the authors' code? It almost never works. ClawBio changes this. Every figure in your paper can be a skill."

---

## If Either Demo Fails

### PharmGx fallback:
Skip to Slide 15 (pre-generated terminal output). Say: "Let me show you what the output looks like." The pre-generated report is in `skills/claw-pharmgx/demo_report/`.

### Ancestry PCA fallback:
Skip to Slide 19 (pre-generated PCA composite figure). The figure is already embedded in the slide. Walk through the 4 panels as normal. Say: "This was generated with one command from the claw-ancestry-pca skill."

---

## The Narrative Arc

```
Personal problem    → "What drugs should I worry about?"
                       (PharmGx: visceral, immediate, everyone relates)

Global picture      → "Where does my cohort sit in global genetic space?"
                       (Ancestry PCA: population genetics, real data, zooms out)

Reproducibility     → "That figure is from a paper. One command reproduces it."
                       (Bridge from demo to the bigger idea)

The reframe         → "Reproducibility is broken. ClawBio fixes it."
                       (Slide 21 — confronts the real problem)

The value prop      → "Publish skills, not just papers."
                       (Tip 10 — the call to action)
```
