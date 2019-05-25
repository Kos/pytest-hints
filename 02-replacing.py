import unittest
import pytest
from typing import List


class Hero:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.exp = 0
        self.items: List[str] = []

    def add_exp(self, exp: int):
        self.exp += exp
        self.level = 1 + self.exp // 1000


class HeroTestCase(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Merlin")

    def test_hero_initial_level(self):
        """Hero should have initial level = 1"""
        self.assertEqual(1, self.hero.level)

    def test_hero_award_exp(self):
        """Hero should accumulate exp"""
        self.hero.add_exp(2500)
        self.assertEqual(3, self.hero.level)

    def test_hero_level_up(self):
        """Hero level should increase when levelling up"""
        self.hero.add_exp(2500)
        self.hero.add_exp(200)
        self.assertEqual(2700, self.hero.exp)


@pytest.fixture
def hero():
    return Hero("Merlin")


def test_hero_initial_level(hero):
    """Hero should have initial level = 1"""
    assert 1 == hero.level


def test_hero_award_exp(hero):
    """Hero should accumulate exp"""
    hero.add_exp(2500)
    assert 3 == hero.level


def test_hero_level_up(hero):
    """Hero level should increase when levelling up"""
    hero.add_exp(2500)
    hero.add_exp(200)
    assert 2700 == hero.exp
