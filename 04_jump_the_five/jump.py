#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-09-18
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str = args.str

    d = {
        "0": "5",
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
    }

    output = ''
    for char in str:
        output += d.get(char, char)

    print(f'{output}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
