"""Artwork URLs. Pokémon images are hosted by PokeAPI; character SVGs are local."""

from flask import url_for

# National Pokédex numbers used by the PokeAPI sprite repository.
POKEDEX_IDS = {
    "pikachu": 25, "eevee": 133, "charizard": 6, "bulbasaur": 1,
    "squirtle": 7, "jigglypuff": 39, "snorlax": 143, "meowth": 52,
    "mewtwo": 150, "psyduck": 54, "gengar": 94, "lucario": 448,
}
ARTWORK_BASE = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork"


def artwork_url(question):
    """Get a portrait for a question without revealing the answer to the player."""
    if question["category"] == "pokemon":
        return f"{ARTWORK_BASE}/{POKEDEX_IDS[question['id']]}.png"
    return url_for("static", filename=f"characters/{question['id']}.svg")
