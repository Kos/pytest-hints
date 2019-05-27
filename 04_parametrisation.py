import string
from pathlib import Path
from typing import Set


class SpellChecker:
    def __init__(self, lexicon: Set[str]):
        self.lexicon = lexicon

    def text_is_valid(self, text: str):
        text_words = (_cleanup_word(word) for word in text.split())
        return all(word in self.lexicon for word in text_words)


def _cleanup_word(word):
    return word.strip(string.punctuation).lower()


def test_spellchecker():
    # TODO: Add more cases
    # TODO: avoid loading the lexicon every time
    checker = SpellChecker(lexicon())
    assert checker.text_is_valid("hello world!") is True
    assert checker.text_is_valid("ehlo world") is False


def lexicon():
    wordlist_path = Path(__file__).parent / "wordlist.txt"
    return set(wordlist_path.read_text().splitlines())
