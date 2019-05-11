from pathlib import Path
import string
import pytest
from typing import Set


class SpellChecker:
    def __init__(self, lexicon: Set[str]):
        self.lexicon = lexicon

    def text_is_valid(self, input: str):
        return all(self._cleanup_word(word) in self.lexicon for word in input.split())

    def _cleanup_word(self, word):
        return word.strip(string.punctuation).lower()


@pytest.mark.parametrize(
    ("input", "expected_output"), [("Hello, world!", True), ("Ehllo, world!", False)]
)
def test_spellchecker(lexicon, input, expected_output):
    checker = SpellChecker(lexicon)
    assert checker.text_is_valid(input) == expected_output


@pytest.fixture(scope="session")
def lexicon():
    return set(Path("wordlist.txt").read_text().splitlines())
