#! /usr/bin/env python3
# Batch file substitution

import argparse
import re
import os
from pathlib import Path


def substitute(text, old, new):
    p = re.compile(old)
    return p.sub(new, text)


def batch_substitute(subslist):
    for subs_def in subslist:
        src, old, new = [x.strip() for x in subs_def.split('||')]
        with open(Path(src), 'r+') as text_source:
            new_text = substitute(text_source.read(), old, new.strip('"'))
            text_source.truncate(0)
            text_source.seek(0)
            text_source.write(new_text)


def cli_substitute(args):
    batch_substitute(args.subslist)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Batch file substitution")
    parser.add_argument(
        "subslist", type=argparse.FileType('r'), default=os.sys.stdin,
        help="Substitution list definition files.")

    args = parser.parse_args()
    cli_substitute(args)
