import string
from pathlib import Path
from typing import Set

import pytest


class SpellChecker:
    def __init__(self, lexicon: Set[str]):
        self.lexicon = lexicon

    def text_is_valid(self, text: str):
        text_words = (_cleanup_word(word) for word in text.split())
        return all(word in self.lexicon for word in text_words)


def _cleanup_word(word):
    return word.strip(string.punctuation).lower()


@pytest.mark.parametrize(
    ("text", "expected_result"),
    [
        ("hello world", True),
        ("Hello, world!", True),
        ("Helllo, world!", False),
        ("adsfasdf", False),
    ],
)
def test_spellchecker(lexicon, text, expected_result):
    checker = SpellChecker(lexicon)
    assert checker.text_is_valid(text) == expected_result


@pytest.fixture(scope="session")
def lexicon():
    wordlist_path = Path(__file__).parent / "wordlist.txt"
    return set(wordlist_path.read_text().splitlines())
