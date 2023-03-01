#!/usr/bin/env python3
"""Reads names from a list and creates username permutations."""

import os
import sys
import re
import argparse

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--infile', required=True, help='File containing first and last names.')
parser.add_argument('--outfile', required=True, help='File to save generated usernames.')
args = parser.parse_args()

def name_generator():
    """Reads names from a file"""
    if os.path.exists(args.infile):
        with open(args.infile, encoding="UTF-8") as names:
            lines = filter(None, (line.rstrip().lower() for line in names))
            for name in lines:
                cleanname = re.sub(r"[^a-zA-Z]+", ' ', name)
                token = cleanname.split()
                if len(token) < 1:
                    continue
                if len(token) > 2:
                    fname = str(token[0])
                    lname = str(token[1]+token[2])
                if len(token) == 2:
                    fname = str(token[0])
                    lname = str(token[1])
                # Print possible usernames
                with open(args.outfile, 'a') as outfile:
                    print(f"{fname}", file=outfile)               # john
                    print(f"{lname}", file=outfile)               # smith
                    print(f"{fname}{lname}", file=outfile)        # johnsmith
                    print(f"{fname}.{lname}", file=outfile)       # john.smith
                    print(f"{fname[0]}{lname}", file=outfile)     # jsmith
                    print(f"{fname[0]}.{lname}", file=outfile)    # j.smith
    else:
        print(f'File {args.infile} not found...')
        sys.exit(0)

if __name__ == "__main__":
    name_generator()
