#!/usr/bin/env python3
from random import choice
import csv

WHITE_CARDS = []
BLACK_CARDS = []

def load():
    """Load cards from CSV."""
    global WHITE_CARDS
    global BLACK_CARDS

    with open('./cards.csv', 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            black = r[0]
            white = r[1]
            if white:
                WHITE_CARDS.append(white)
            if black:
                BLACK_CARDS.append(black)

def generate():
    """Generate a complete phrase."""
    repl_count = 0

    phrase = choice(BLACK_CARDS)
    while '_' in phrase:
        repl_count += 1
        phrase = phrase.replace('_', choice(WHITE_CARDS), 1)

    if repl_count == 0:
        phrase += " " + choice(WHITE_CARDS)

    return phrase

def main():
    """Main point of execution."""
    load()

    print(generate())

if __name__ == '__main__':
    main()
