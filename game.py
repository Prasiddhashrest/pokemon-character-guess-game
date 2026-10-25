"""Pure game rules: these functions are easy to test without a web server."""

import random
import re
import unicodedata

from data import POINTS_BY_CLUE, QUESTIONS


def normalize(value):
    """Make spelling checks forgiving of case, accents, punctuation and spaces."""
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def matches_answer(question, guess):
    cleaned = normalize(guess)
    if not cleaned:
        return False
    return any(cleaned == normalize(answer) for answer in [question["name"], *question["aliases"]])


def points_for(clue_index, wrong_guesses):
    if not 0 <= clue_index < len(POINTS_BY_CLUE):
        raise ValueError("Unknown clue number")
    return max(10, POINTS_BY_CLUE[clue_index] - 10 * wrong_guesses)


def pick_question(category, seen_ids, rng=None):
    """Don't repeat a question until the available pool is exhausted."""
    if category not in ("pokemon", "characters", "mixed"):
        raise ValueError("Unknown category")
    choices = [
        item for item in QUESTIONS
        if (category == "mixed" or item["category"] == category)
        and item["id"] not in seen_ids
    ]
    if not choices:
        return None
    return (rng or random).choice(choices)
