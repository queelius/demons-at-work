# Craft Auditor Report

**Date**: 2026-04-09
**Manuscript**: Demons at Work (13 chapters, ~9,574 words)
**Scope**: Full manuscript, prose quality and scene mechanics

## Methodology

Analyzed prose for mechanical patterns (via count_patterns.py), sentence structure repetition, cliche detection, scene construction, and adherence to the style guide's constraints (no em-dashes, short punches, dual register, trust the reader).

## Mechanical Pattern Counts

The manuscript is exceptionally clean on mechanical crutches:
- **Crutch words**: "something" (17x total), "just" (5x), "quite" (3x), "actually" (1x). For ~9,574 words, these are well within acceptable ranges.
- **Filter words**: 1 instance of "could hear" (Ch4)
- **Weak verbs**: 0
- **Adverb dialogue tags**: 0
- **Em-dashes**: 0 (style constraint honored throughout)

## Findings

### HIGH

*No HIGH craft issues found.*

### MEDIUM

#### M1. "Which" clause accumulation in Ch5

- **Location**: Ch5 "Good Acoustics" (672 words, 6 "which" clauses)
- **Examples**:
  - Line 8: "designated Primus Ordinatus, which everyone shortens to Prim"
  - Line 10: "which means either... which they always are... which was issued to all middle management during a morale initiative whose purpose and origin nobody remembers" (three in one sentence)
  - Line 54: "which is what Prim came for"
  - Line 56: "which is either progress or surrender"
- **Problem**: The "which" appositional clause is a signature of Tert's analytical voice and works well in moderation. In Ch5, the density reaches 1 per 112 words. Line 10 stacks three in a single sentence. The effect is syntactically heavy where the voice should be clipped and punchy. The style guide says "short punches."
- **Suggestion**: Break one or two of the three "which" clauses in line 10 into separate sentences. "Prim is carrying a clipboard. They always are." This preserves the dryness while reducing the syntactic weight.
- **Confidence**: High

#### M2. "Not X" corrective fragment pattern

- **Location**: Throughout, 15 occurrences across 9,574 words (1 per ~638 words)
- **Examples**:
  - Ch2: "Not hot, not cold. Not lukewarm..."
  - Ch3: "Not invisible. I am already concealed."
  - Ch3: "Not the scaring. The calibration."
  - Ch4: "Not fear. Not dread."
  - Ch6: "Not much. Enough to accelerate..."
  - Ch6: "Not wake. Shift."
  - Ch9: "Not loudly. Not at anything I can identify."
- **Problem**: This is a strong voice pattern and should not be eliminated. However, at 15 occurrences in ~9,500 words, attentive readers may begin to feel the machinery. The pattern is most dense in Ch3 (4x in 1,167 words) and Ch6 (4x in 566 words = 1 per 142 words).
- **Suggestion**: Reduce by 2-3 instances in the densest chapters. Keep the strongest uses (Ch3's "Not the scaring. The calibration" and Ch6's "Not wake. Shift." are the best). Cut or restructure the weaker ones where the "Not X" is doing clarification rather than characterization.
- **Confidence**: Medium (reasonable people may disagree on the threshold)

### LOW

#### L1. "I do not" negative construction frequency

- **Location**: Throughout, 20 occurrences
- **Observation**: "I do not" appears 20 times in 9,574 words (1 per ~479 words). This is characteristic of Tert's voice: formal, declarative, un-contracted. It contributes to the professional register. Most instances are earned. Ch1 has the highest concentration (7 instances in 1,856 words). This is acceptable for the opening chapter where the voice is establishing itself.
- **Status**: Monitor but do not reduce. The formality is the voice.
- **Confidence**: High

#### L2. "This is" declarative pattern

- **Location**: Throughout, 21 occurrences
- **Examples**:
  - "This is the part of the work I love."
  - "This is what Phase 1 is."
  - "This is the question."
  - "This is atmospheric work at the level I have always known I was capable of."
  - "This is good work. This is the work I am here to do."
- **Observation**: A strong pattern used for emphasis. The two-in-a-row usage in Ch12 ("This is good work. This is the work I am here to do.") is the strongest instance and earns its repetition. Other instances are individually fine. The cumulative effect is acceptable.
- **Status**: No action needed. Noting for awareness.
- **Confidence**: High

## Strengths

### S1. Scene construction: The Middlemarch plant-and-payoff

The book on the shelf is mentioned in Ch1 (survey photograph, line 73: "a book is lying flat on top of the other books"), again in Ch3 (first visit, line 27: "a thick paperback with a cracked spine and a bookmark about two-thirds through"), and paid off in Ch10 (the turn, line 14-16: Tert reads the title for the first time). This three-stage reveal across ten chapters is expertly paced. Tert's professional eye catalogs it as furniture; the reader's eye accumulates it as a question. The payoff lands because the reader has been carrying the image longer than they realize.

### S2. The coffee temperature motif

The wrong-temperature coffee appears in Ch2 (establishment, extended description), Ch5 (implicit, during the check-in), and Ch11 (post-turn: "It is the wrong temperature. I drink it anyway."). The Ch11 instance is the same words but reads differently because Tert reads differently. This is the dual register at the sentence level: the repetition is comic in Ch2 and elegiac in Ch11.

### S3. The thermostat as narrative device

Ch4: Tert shifts it down two degrees. Ch6: Gordon finds it at 66, turns it to 68. Ch6: "He found the thermostat. I will not use it again." Three beats, perfectly weighted. The first establishes the tactic, the second shows the human's practical response, the third shows Tert's professional respect. The pragmatic human defeating the demon's craft through mundane attention is the book's core joke, executed in miniature.

### S4. Horror craft as genuine instruction

The passages where Tert explains his technique (the acoustic properties of bookshelves, the joist-timing method, the three-part Wednesday night sequence) read as genuine knowledge about how horror works. The reader learns something real about atmospheric dread while being entertained. This dual function is rare and difficult to sustain.

### S5. The garden chapter (Ch7, 324 words)

Every sentence carries weight. No fat. The margin-pad note at the end ("subject engaging with outdoor space; investigate external sound vectors") is the gap between what Tert writes and what the reader sees, rendered in Tert's own hand. This is the dual register compressed to a single gesture.
