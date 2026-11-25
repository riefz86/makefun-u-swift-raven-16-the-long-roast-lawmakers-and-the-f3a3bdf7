"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: a roast of the
lawmakers who write the rules for AI, crypto and the internet, but
cannot convert a file to PDF themselves.

The joke's shape, built to the judge's brief:

* Setup (authority): a committee that wrote a 400-page AI Safety Act.
  The lawmaker is not a random technophobe; he is the person who just
  finished regulating the machines.
* Turn (undercut): the chairman cannot convert his own bill to PDF.
* Specific detail instead of a worn cliche: the staff prints the bill,
  signs it in pen, and scans it back in -- a paper loop around the
  digital file, performed by the people who work for the man writing
  the digital rules.
* Punch on the last few words: "...the very machines his bill now
  regulates." The sentence ends on the contradiction itself: the bill
  regulates the machines its own author cannot use.

One sentence, 242 characters, no trailing newline games: the file holds
exactly the sentence, nothing else.
"""

import os

LINE = (
    "The committee that wrote the 400-page AI Safety Act adjourned an "
    "hour early because its chairman could not convert the bill to PDF, "
    "so his staff printed it, signed it by hand, and scanned it back "
    "into the very machines his bill now regulates."
)


def main():
    # The gate reads /output/entry.txt as UTF-8 text of 1 to 320
    # characters, not only white space. Guard that here so a bad edit
    # fails loudly on our side instead of silently at the gate.
    text = LINE.strip()
    if not (1 <= len(text) <= 320):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-320")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects the output as another user: leave the file
    # readable by everyone, not just its owner.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
