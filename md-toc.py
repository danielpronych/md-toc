#!/usr/bin/python
"""
Generate table of contents (toc) from a markdown files
"""
from __future__ import print_function
import argparse
import re
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("-l", "--level", type=int,
                        default=1,
                        help="Number of header levels to inclue")
    parser.add_argument("file",
                         type=argparse.FileType('r'))

    try:
        args = parser.parse_args()
    except IOError as e:
        print(e)
        sys.exit(2)

    toc = list()
    for line in args.file:
        i = 0
        token = ""
        while i < int(args.level):
            i += 1
            token = token + "#"
            s = "^" + token + " "

            m = re.search(s, line)
            if m is not None:
                s, h = line.split(token)
                item = h.lstrip().rstrip()
                link = item.replace(' ', '-').lower()
                entry = "- [" + item + "](" + token + link + ")"
                toc.append(entry)

    print(toc)
if __name__ == "__main__":
    main()
