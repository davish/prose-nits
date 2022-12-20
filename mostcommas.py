#!/usr/bin/env python3

from .parse import *


def main():
    with open("input.txt") as file:
        commas_by_sentence = with_comma_count(file.read())
        ranked = sorted(commas_by_sentence, key=lambda x: x[1], reverse=True)

        print("## Sentences with the most commas")
        for result in [result for result in ranked if result[1] > 1]:
            print(result)
