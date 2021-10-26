#! /usr/bin/env python3
# Batch file replicator

import argparse
import os
from pathlib import Path
from shutil import copy


def replicate(src, filenames_stream):
    for filename in filenames_stream:
        copy(src, filename.strip())


def cli_replicate(args):
    replicate(args.src, args.filenames)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Batch file replicator")
    parser.add_argument(
        "src", type=Path, help="File to replicate")
    parser.add_argument(
        "filenames",
        type=argparse.FileType('r'),
        default=os.sys.stdin, help="List of filenames on a file or stdin")

    args = parser.parse_args()
    cli_replicate(args)
