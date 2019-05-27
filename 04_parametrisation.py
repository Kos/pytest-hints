from pathlib import Path
import string
import pytest
from typing import Set


class SpellChecker:
    def __init__(self, lexicon: Set[str]):
        self.lexicon = lexicon

    def text_is_valid(self, text: str):
        text_words = (self._cleanup_word(word) for word in text.split())
        return all(word in self.lexicon for word in text_words)

    def _cleanup_word(self, word):
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
    return set(Path("wordlist.txt").read_text().splitlines())
