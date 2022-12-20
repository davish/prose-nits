#!/usr/bin/env python3
from parse import *


def find_runon_strings(commas_by_sentence, num_sentences, num_commas):
    return [
        window
        for window in windows(commas_by_sentence, num_sentences)
        if sum(s[1] for s in window) >= num_commas
    ]


def main():
    with open("input.txt") as file:
        commas_by_sentence = with_comma_count(file.read())
        for result in [
            result for result in find_runon_strings(commas_by_sentence, 2, 4)
        ]:
            print("***")
            print(" ".join(s[0] for s in result))
            print(f"- {sum([s[1] for s in result])} commas")


if __name__ == "__main__":
    main()
