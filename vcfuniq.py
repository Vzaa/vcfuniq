#!/usr/bin/env python
import sys

def main():
    card_strs = set()
    with open(sys.argv[1]) as vfile:
        lines = vfile.readlines()
        cardstr = ""
        for line in lines:
            stripped = line.strip()
            cardstr += line
            if stripped == "END:VCARD":
                card_strs.add(cardstr)
                cardstr = ""

    with open(sys.argv[2], "w") as vfile:
        vfile.writelines(card_strs)

if __name__ == "__main__":
    main()
