import re

end_of_sentence = re.compile(r"[\?\.\!]+\s+")


def split_by_sentence(s: str):
    # I don't know how to split on a regex while still including
    # what the regex matched in the resulting strings. And I refuse
    # to pay $5 for airplane wifi to look it  up. I'll just assume
    # `@@@` won't show up in any of my inputs.
    return [
        s
        for s in (
            s.replace(". ", ". @@@")
            .replace("? ", "? @@@")
            .replace("! ", "! @@@")
            .split("@@@")
        )
    ]


def count_commas(s: str):
    return len([c for c in s if c == ","])


def windows(l, size):
    for idx in range(len(l)):
        if idx + size > len(l):
            return
        yield l[idx : idx + size]


def with_comma_count(s):
    sentences = split_by_sentence(s.replace("\n", " "))
    return [
        (sentence.strip(), count_commas(sentence))
        for sentence in sentences
        if sentence.strip() != ""
    ]
