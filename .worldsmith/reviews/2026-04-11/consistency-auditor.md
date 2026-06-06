# Consistency Audit

**Auditor**: consistency-auditor
**Date**: 2026-04-11
**Scope**: Full manuscript (21 chapters, ~13,430 words)
**Canonical sources**: themes.md, world.md, style.md, characters.md, outline.md, countermeasures.md

---

## Findings

### HIGH

**(No HIGH consistency issues found.)**

### MEDIUM

#### M-1: Meri's Pronouns Incorrect in Chapter 5

- **Location**: 05-check-in.tex, line 56
- **Quoted text**: `On my way to the transit desk I pass Meri in the hallway. They are not carrying the Operations Manual, which is either progress or surrender.`
- **Also**: line 58: `"I read the section," they say.`
- **Problem**: Meri is referred to with "they/them" pronouns. The canonical character doc specifies Meri uses "she/her" pronouns. In every other chapter (02, 09, 16, 18), Meri is consistently "she/her." The "they" in ch2 before Meri identifies herself is defensible (Tert doesn't know the new hire yet), but by ch5 Tert has known Meri for a week.
- **Suggestion**: Replace "They are not carrying" with "She is not carrying" and "they say" with "she says" in ch5, lines 56 and 58.
- **Confidence**: HIGH. Clear error against canonical specification.

### LOW

#### L-1: Chapter Comment Numbering Out of Sync

- **Location**: 18-meri.tex (says "Chapter 15"), 19-the-field.tex (says "Chapter 17b"), 20-completion.tex (says "Chapter 16"), 21-the-next-file.tex (says "Chapter 17")
- **Problem**: LaTeX comment headers contain chapter numbers that don't match the file numbering or the actual chapter sequence. These are not rendered in the manuscript but could cause confusion during editing.
- **Suggestion**: Update comment headers to reflect the actual 21-chapter sequence.
- **Confidence**: HIGH. Visible in the source files.

#### L-2: Gordon Has a "Bag" Despite Being Retired

- **Location**: 03-the-house.tex, line 55
- **Quoted text**: `the first thing he does is put his keys on the hook and his bag on the chair by the door`
- **Problem**: Gordon is retired. The "bag" is unspecified. A retired person returning from errands might carry a bag, but it reads slightly odd without context -- a grocery bag? A tote? The word "bag" in isolation reads more like a work bag.
- **Assessment**: This is more ambiguous than wrong. A retired man coming home at 4 PM from a day out would plausibly have a bag. But it might benefit from a single modifier ("shopping bag," "canvas bag") to ground it.
- **Suggestion**: Optional. Could add a specifying word, or leave it -- the ambiguity is minor.
- **Confidence**: MEDIUM. Defensible as-is but slightly dissonant.

---

## Consistency Strengths

1. **Timeline is accurate.** The five-week arc is internally consistent. "Seventeen days" in ch10 (week 3) and "thirty-five days" in ch20 (week 5) both check out. The turn occurs at exactly the 60% mark as specified in the outline.

2. **Physical environment is stable.** The house description (bungalow, 1923, hardwood, plaster, bookshelves flanking fireplace, grab bar, sickroom, back garden) is consistent across all chapters. Objects introduced in ch1 (the survey photos) reappear correctly in ch3 (first visit), ch11 (the turn), ch15 (the doorway), and ch20 (completion).

3. **The bookmark thread is precise.** Introduced as "no bookmark handy" in ch1 (survey photo), identified as "a bookmark about two-thirds through" in ch3, used at the same position in ch11, and noted as having moved in ch20. Clean progression.

4. **Prim's characterization is consistent.** Always "they/them" (correctly, as a legion), always clipboard, always the same corporate-speak register. The WORLD'S BEST mug appears in ch5 and is consistent with the character doc.

5. **The sickroom thread tracks correctly.** Door closed in ch3, referenced as baseline in ch4, held in reserve in ch10, opened by Gordon (not Tert) in ch15, closed again in ch20. The restraint (Tert never uses it) matches the canonical decision.

6. **Gordon's routine is stable.** Dinner at seven, TV until 9:30, bed around 11 -- this holds across ch4, ch10, ch11, and ch20. The one variation (4 AM coffee, ch10) is noted as exceptional.

7. **Motif repetitions are controlled.** "Wrong temperature" coffee: ch2, ch12, ch16, ch21 -- four occurrences, spaced evenly, functioning as structural bookends. "Circle hat": ch2, ch18 (twice) -- three occurrences, the third showing Meri has adopted it. "I drink it anyway": ch2, ch12, ch21 -- three times, all in office scenes, marking Tert's continuation.
