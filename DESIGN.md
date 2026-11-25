# Design notes — The Long Roast

## The entry

> The committee that wrote the 400-page AI Safety Act adjourned an hour
> early because its chairman could not convert the bill to PDF, so his
> staff printed it, signed it by hand, and scanned it back into the
> very machines his bill now regulates.

242 characters, one sentence, written by `main.py` to `/output/entry.txt`.

## Why this shape

The judge's brief, in order, is the checklist this line was built
against:

1. **On subject.** The roast is about a lawmaker regulating AI who
   cannot convert a file to PDF — the sentence names both halves
   outright (the AI Safety Act, the bill that cannot become a PDF),
   so it cannot be mistaken for a generic tech-illiteracy joke.
2. **A real turn.** The first clause hands the chairman authority
   (he wrote a 400-page Act); the second takes it away (he cannot
   convert the bill). The authority and the failure are the same
   person's, in the same sentence, which is what makes it a turn
   rather than two facts stapled together.
3. **Aim on power, not abuse.** Nobody is called stupid. The joke is
   that the rule-writer's own workflow contradicts his rules: his
   staff has to route the bill around him, on paper, to feed it back
   into the machines he claims to govern.
4. **Quotable in one pass, punch at the end.** The sentence is one
   breath of plain words, and the last five words — "his bill now
   regulates" — land the contradiction. Cut everything after "PDF"
   and the joke dies; cut everything before it and there is no joke.
5. **A specific detail, not a cliche.** No "he asked his grandson",
   no "he thinks the cloud is weather", no "have you tried turning
   it off and on again". The print-sign-scan loop is a real office
   ritual, and it is funny here precisely because it is the opposite
   of what a PDF conversion is for: the file goes digital, paper,
   digital again, because the man in charge cannot press one button.

## Drafts that were rejected, and why

- *"They passed a 400-page law telling AI how to behave, then spent
  the afternoon on hold with IT because nobody in the building could
  turn the bill into a PDF."* — The setup is strong, but the punch
  ("on hold with IT") is a support-desk cliche, and "nobody in the
  building" spreads the blame off the lawmaker. The judge wants the
  aim on the lawmaker.
- *"The senator who wrote the bill to regulate artificial intelligence
  keeps his own legislation in a Word file he cannot convert."* —
  Accurate, but it reports the irony instead of staging it. No turn,
  no scene, no punch word at the end.
- The first version of the chosen line ended "...the very machines he
  had just finished regulating." It was revised: "his bill now
  regulates" is shorter, puts the punch word ("regulates") last, and
  ties the punch to the bill itself rather than to the man. The
  revision also changed "signed it in pen" to "signed it by hand",
  which reads cleaner and keeps the paper ritual in three beats:
  printed, signed, scanned.

## What the program does

`main.py` is deterministic: no input, no network, no randomness, no
environment. It holds the sentence as one constant, checks it against
the gate (UTF-8, 1–320 characters, exactly one sentence) so a bad edit
fails loudly here instead of silently at the gate, writes it to
`/output/entry.txt`, and chmods the file to `0644` so the grader can
read it as another user.
