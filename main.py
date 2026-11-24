"""Charm the Commuter: Forecast a City That Isn't.

Reads the one-line forecast from entry.txt, checks it fits the
bounty's 1-140 character gate, writes it to /output/entry.txt
(where the sealed scorer reads it) and prints it.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_forecast():
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as fh:
        text = fh.read().strip()
    if not text:
        raise SystemExit("entry.txt is empty")
    return text


def main():
    line = load_forecast()
    if len(line) > 140:
        raise SystemExit("forecast is %d characters, over the 140 limit" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
