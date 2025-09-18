#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2025-09-18
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs="+",
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    sorted = args.sorted

    if sorted:
        items.sort()

    num_items = len(items)
    if num_items == 1:
        print(f'You are bringing {items[0]}.')
    elif num_items == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        print(f'You are bringing {', '.join(items[:-1])}, and {items[-1]}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
