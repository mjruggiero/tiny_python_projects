#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-09-19
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    # print(f"outfile: {outfile}")
    if len(outfile) != 0:
        with open(outfile, "wt") as f:
            f.write(text.upper())
    else:
        print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
