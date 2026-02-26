# Speaker Notes — 10 Tips for Becoming a Top 1% AI User

Total talk time: 45-50 minutes + Q&A
28 slides. PharmGx first (visceral), Ancestry PCA (population), Semantic Similarity (systemic), then reproducibility framing.

---

## Slide 1: Title (2 min)

"Welcome everyone. I'm Manuel Corpas, Senior Lecturer at the University of Westminster and Turing Fellow. Tonight I want to share 10 practical techniques that separate casual AI users from the top 1% who are shipping research faster than ever."

"We'll start with quick wins you can adopt tomorrow morning, and end with two live demos — including one where I'll show you which drugs won't work based on a genetic test."

---

## Slide 2: The Gap (3 min)

"Here's the gap I see every day. Most researchers use AI like a search engine. They open ChatGPT, ask a question, paste the answer somewhere, and move on. No memory. No automation. No compounding."

"The top 1% have moved past that. They have agents that work while they sleep. Persistent memory that spans months. Automated pipelines that process papers, emails, and data without human intervention."

"The good news: you can cross this gap in a weekend. Let me show you how."

---

## Slides 3-9: Tips 1-7 (13 min)

Standard tips delivery — no changes needed. See slide notes.

---

## Slide 10: Transition (30 sec)

"Everything so far is about using AI tools that already exist. Now I want to talk about building. Because the bioinformatics community has specific needs that general AI tools don't address."

---

## Slide 11: Tip 8 — Why Not Just Use ChatGPT? (3 min)

**THIS IS THE PIVOT. Nail this.**

"Now, some of you are thinking: can't I just ask ChatGPT to do this? You can try."

"Ask it to profile pharmacogenes from a 23andMe file. It'll write plausible-looking Python. But it'll hallucinate star allele calls. It'll use outdated CPIC guidelines. It won't know that CYP2D6 *4 is no-function, not just reduced. You'll spend 45 minutes debugging output that looks right but isn't."

"This is the core problem. General-purpose AI is powerful but blind to biology. It doesn't know your preferred FST method. It doesn't generate reproducibility bundles. And you can't send your patient genomes to a cloud API."

"So I built ClawBio."

[REVEAL LOGO]

"ClawBio encodes the correct bioinformatics decisions so the agent gets it right first time, every time. A domain expert's judgement, frozen into code that an AI agent executes. Let me show you what that looks like."

---

## Slide 12: Architecture (1.5 min)

Keep brief. "Natural language in, markdown report out. The orchestrator routes to the right skill. Each skill wraps proven bioinformatics tools. Every analysis ships with a reproducibility bundle."

Don't linger on architecture. The audience wants to see it work.

---

## Slide 13: Skill Catalogue (1 min)

"Three skills at MVP. Seven more on the roadmap. But let me just show you."

Transition immediately to demo.

---

## Slide 14: Tip 9 + PharmGx Demo Intro (switch to terminal)

"Here's the scenario. I just got my 23andMe results back. I want to know which drugs might not work for me."

[SWITCH TO TERMINAL — see DEMO-SCRIPT.md]

Run PharmGx Reporter. One command. Under 1 second.

---

## Slides 15-16: PharmGx Results (3 min total)

Walk through terminal output, then gene profile table.

**Key moments:**
- "CYP2D6 *4/*4 — Poor Metabolizer. This single gene affects 22 drugs."
- "Codeine literally cannot work. Your body can't convert it to morphine."
- "I didn't tell the tool which genes to check. That domain knowledge is baked in."
- "Under one second. Zero cloud dependencies. Your genetic data never left this laptop."

---

## Slide 17: Why PGx Matters (1.5 min)

"Raise your hand if you've ever taken codeine after a dental procedure."

[Wait for hands]

"About 7% of you in this room are CYP2D6 poor metabolizers. Codeine gave you zero pain relief and you didn't know why."

"2% are CYP2C19 poor metabolizers — clopidogrel won't protect them after a stent."

"0.5% carry DPYD variants where a standard 5-FU chemo dose can be fatal."

"That was the personal level. Now let me zoom out to the systemic level."

---

## Slide 18: Ancestry PCA Demo (1.5 min)

[SWITCH TO TERMINAL]

"Second skill. Same principle — one command, works out of the box. The question now is: where does my cohort sit in global genetic space?"

"The reference panel is the Simons Genome Diversity Project: 345 samples from 164 populations spanning every inhabited continent. The skill finds common variants, runs PCA on the merged set, and generates a 4-panel figure."

"I didn't tell it which reference to use, how to normalise contigs, or how to handle IBD. That's baked in."

Run Ancestry PCA in demo mode. Show the output.

---

## Slide 19: Ancestry PCA — Full Figure (2 min)

**Let the figure breathe. Point to each panel.**

"Four panels. Top-left: PC1 vs PC2 showing the internal structure of 28 Peruvian populations. Top-right: regional groupings — Highland in red, Amazonian in green, Coastal in blue. Bottom-left: linguistic groupings — Quechua and Aymara."

"And bottom-right — the money shot: Peru against the Simons Genome Diversity Project. Circles are Peru, triangles are SGDP. You can see exactly where indigenous Peruvian populations sit relative to 164 global populations."

---

## Slide 20: What This Tells Us (2.5 min)

"Panel D is the key. Amazonian indigenous groups like the Matzes sit in genetic space that no SGDP population occupies. They are genuinely underrepresented — not just in GWAS, but in the reference panels we use to study diversity."

"That figure is from a paper we're writing on the Peruvian Genome Project. But there's a deeper problem. Even when diseases are studied, their research doesn't connect. Let me show you what I mean."

**This is the bridge to the semantic similarity demo.**

---

## Slide 21: Semantic Similarity Index Demo (1.5 min)

"Third skill. Same principle — one command. But now the question is systemic: which diseases are trapped in knowledge silos?"

"We embedded 13.1 million PubMed abstracts with PubMedBERT and computed a Semantic Isolation Index for every GBD disease. The result: neglected tropical diseases are 38% more isolated than other conditions. They exist in knowledge silos with almost no cross-disciplinary research bridges."

---

## Slide 22: Semantic Structure — Full Figure (2 min)

**Let the figure breathe. Point to each panel.**

"Four panels again. Top-left: semantic isolation by disease category — Injuries and Infectious diseases at the top. Top-right: the 20 most isolated diseases — 14 of the top 25 are Global South priority conditions, shown in red and orange."

"Bottom-left: the inverse correlation between research volume and isolation — the less you study a disease, the more isolated its research becomes. A vicious cycle. Bottom-right: NTDs versus everything else — statistically significant, large effect size."

"This is structural neglect made visible through language models."

---

## Slide 23: Why Semantic Isolation Matters (1.5 min)

"A malaria immunology breakthrough could help leishmaniasis, but those two literatures barely overlap. Drug repurposing depends on cross-disease bridges, and NTDs have almost none."

"Three demos tonight, three scales: personal pharmacogenomics, population ancestry, and systemic knowledge silos. Each one runs with one command. Each one is a figure from a paper. And that's the real point: every figure should be reproducible with one command."

---

## Slide 24: Reproducibility Is Broken (2 min)

"How many of you have tried to reproduce a figure from a published paper using the authors' code?"

[Wait for reactions]

"It almost never works. Dependencies are broken. Paths are hardcoded to someone else's machine. The reference data isn't included. You email the first author and wait three weeks."

"ClawBio changes this. Every figure in your paper can be a skill. The inputs, dependencies, and reference data are all declared. Someone reads your paper, types one command, and gets the exact figure. With a checksum to prove it's identical."

"That's not just a toolkit. It's a new way to publish reproducible bioinformatics."

---

## Slide 25: Tip 10 — Publish Skills, Not Just Papers (2.5 min)

"Tip 10: publish skills, not just papers. claw-pharmgx took 2 days to build. claw-ancestry-pca wraps a real publication pipeline. claw-semantic-sim embeds 13.1 million abstracts and reveals structural neglect. All three are figures from papers in preparation, and anyone will be able to reproduce them with one command."

"Think about your own work. That GWAS pipeline you run every time? Make it a skill. That metagenomics classifier? Make it a skill. That clinical variant interpretation workflow? Wrap it. The template is there. The orchestrator routes to your skill automatically."

"Imagine a world where every bioinformatics paper ships with a ClawBio skill. You read the paper, you run the skill, you get the exact figures. That's the world we're building."

---

## Slide 26: Get Started (1.5 min)

"The repo is live now. Tonight you can run all three demos on your own data. claw-pharmgx works with any 23andMe or AncestryDNA file. claw-ancestry-pca works with any VCF and population map. claw-semantic-sim runs on the full GBD disease list. All include demo data so you can try them immediately."

"If you want to build the next skill, the template is there. Think about the analysis you run most often. Wrap it. Submit a PR. I'll review it personally."

---

## Slide 27: Recap (1 min)

Quick recap. Don't linger.

"Tips 1-7: AI fluency. Tips 8-10: building with AI. The throughline: the top 1% build systems. Everyone else uses tools one at a time."

---

## Slide 28: Thank You

"Thank you. I'll be at the pub after. Come talk to me if you want to build a skill, have ideas for the library, or just want to chat about AI in bioinformatics. Questions?"

---

## Timing Summary

| Section | Slides | Time |
|---------|--------|------|
| Title + Gap | 1-2 | 5 min |
| Tips 1-7 | 3-9 | 13 min |
| Transition | 10 | 0.5 min |
| Tip 8 (Why not ChatGPT? + ClawBio) | 11-13 | 5.5 min |
| PharmGx Demo (visceral) | 14-17 | 7 min |
| Ancestry PCA Demo (population) | 18-20 | 6 min |
| Semantic Similarity Demo (systemic) | 21-23 | 5 min |
| Reproducibility + Tip 10 + CTA | 24-26 | 6 min |
| Recap + Thank You | 27-28 | 2 min |
| **Total** | **28** | **~50 min** |
| Q&A | — | 5-10 min |

---

## The Narrative Arc

```
HOOK:       "What drugs should I worry about?" (PharmGx — everyone relates)
REVEAL:     "Under 1 second. Your data never left your laptop."
PIVOT:      "That was personal. Now here's the global picture." (Ancestry PCA)
ZOOM OUT:   "Which diseases are trapped in knowledge silos?" (Semantic Similarity)
INSIGHT:    "Three figures from three papers. Each reproducible with one command."
REFRAME:    "Reproducibility is broken. ClawBio fixes it."
ASK:        "Publish skills, not just papers. Who wants to build one?"
```
