"""Question bank. Clues go from hardest to easiest."""

QUESTIONS = [
    # Pokémon
    {"id": "pikachu", "name": "Pikachu", "category": "pokemon", "aliases": [],
     "clues": ["I store electricity in a special part of my body.", "My species often travels with human trainers.", "I am a small, yellow Electric-type Pokémon.", "I am Ash's famous partner, and I say 'Pika Pika!'"]},
    {"id": "eevee", "name": "Eevee", "category": "pokemon", "aliases": [],
     "clues": ["My genetic makeup is famously unstable.", "I have many possible evolutions.", "I am a brown, foxlike Normal-type Pokémon.", "My evolutions include Vaporeon, Jolteon, and Flareon."]},
    {"id": "charizard", "name": "Charizard", "category": "pokemon", "aliases": [],
     "clues": ["I am the final evolution of a Kanto starter Pokémon.", "I can fly and breathe very hot fire.", "My body is orange and I have large wings.", "I evolve from Charmeleon, which evolves from Charmander."]},
    {"id": "bulbasaur", "name": "Bulbasaur", "category": "pokemon", "aliases": [],
     "clues": ["I was one of the original three starter choices in Kanto.", "I have both Grass and Poison types.", "A plant bulb grows on my back.", "My Pokédex number is 0001."]},
    {"id": "squirtle", "name": "Squirtle", "category": "pokemon", "aliases": [],
     "clues": ["I was one of the original three starter choices in Kanto.", "I protect myself with a hard shell.", "I am a little blue Water-type turtle.", "My evolution line includes Wartortle and Blastoise."]},
    {"id": "jigglypuff", "name": "Jigglypuff", "category": "pokemon", "aliases": [],
     "clues": ["My voice is my greatest talent.", "I often get annoyed when nobody listens to me.", "I am round, pink, and have large eyes.", "My lullaby makes people fall asleep."]},
    {"id": "snorlax", "name": "Snorlax", "category": "pokemon", "aliases": [],
     "clues": ["My lifestyle is famously low-energy.", "I can block a road simply by resting on it.", "I am a giant, sleepy Normal-type Pokémon.", "Trainers sometimes wake me with a Poké Flute."]},
    {"id": "meowth", "name": "Meowth", "category": "pokemon", "aliases": [],
     "clues": ["I have a particular interest in shiny currency.", "One famous member of my species can speak like a human.", "I look like a cream-colored cat with a coin on my forehead.", "In the anime, I am often seen with Jessie and James."]},
    {"id": "mewtwo", "name": "Mewtwo", "category": "pokemon", "aliases": [],
     "clues": ["I was created through scientific experimentation.", "I am an extremely powerful Psychic-type Pokémon.", "My origin is connected to the mythical Pokémon Mew.", "I am the central Pokémon in the first Pokémon movie."]},
    {"id": "psyduck", "name": "Psyduck", "category": "pokemon", "aliases": [],
     "clues": ["I often seem confused and uncomfortable.", "A headache can trigger my mysterious powers.", "I am a yellow, ducklike Water-type Pokémon.", "Misty has a famously headache-prone one in the anime."]},
    {"id": "gengar", "name": "Gengar", "category": "pokemon", "aliases": [],
     "clues": ["I enjoy lurking in dark places.", "I am both Ghost-type and Poison-type.", "I am purple and have a huge mischievous grin.", "I evolve from Haunter and am in Gastly's evolution line."]},
    {"id": "lucario", "name": "Lucario", "category": "pokemon", "aliases": [],
     "clues": ["I can sense and interpret the energy of living things.", "I have Fighting and Steel types.", "I am a blue-and-black jackal-like Pokémon.", "I use aura powers and evolve from Riolu."]},
    # Fictional characters
    {"id": "mario", "name": "Mario", "category": "characters", "aliases": ["super mario"],
     "clues": ["My earliest adventures involved climbing and jumping.", "I frequently rescue someone in a fantasy kingdom.", "I wear red and work as a plumber.", "My brother is Luigi, and I battle Bowser."]},
    {"id": "luigi", "name": "Luigi", "category": "characters", "aliases": [],
     "clues": ["I am brave, but often a little nervous.", "I have explored haunted mansions with special equipment.", "I am a tall plumber who wears green.", "My brother is Mario."]},
    {"id": "sonic", "name": "Sonic the Hedgehog", "category": "characters", "aliases": ["sonic"],
     "clues": ["Speed is the foundation of my adventures.", "I collect golden rings and fight a scientist.", "I am a blue hedgehog wearing red shoes.", "My enemy is Dr. Eggman, also known as Dr. Robotnik."]},
    {"id": "elsa", "name": "Elsa", "category": "characters", "aliases": ["queen elsa"],
     "clues": ["I spent much of my youth hiding a remarkable ability.", "I have a close relationship with my younger sister.", "I can create snow and ice using magic.", "I sing 'Let It Go' in Disney's Frozen."]},
    {"id": "shrek", "name": "Shrek", "category": "characters", "aliases": [],
     "clues": ["I value privacy and my quiet home.", "A talkative donkey is my best friend.", "I am a large green ogre who lives in a swamp.", "My wife is Princess Fiona."]},
    {"id": "hermione", "name": "Hermione Granger", "category": "characters", "aliases": ["hermione"],
     "clues": ["My academic dedication often saves my friends.", "I am a talented witch who loves books.", "My closest friends include Ron and Harry.", "I attended Hogwarts and used a Time-Turner."]},
    {"id": "spongebob", "name": "SpongeBob SquarePants", "category": "characters", "aliases": ["spongebob", "sponge bob", "sponge bob square pants"],
     "clues": ["I am almost always cheerful about going to work.", "My best friend is a starfish.", "I live underwater in a pineapple.", "I work as a fry cook at the Krusty Krab."]},
    {"id": "batman", "name": "Batman", "category": "characters", "aliases": ["bruce wayne"],
     "clues": ["I rely on preparation and equipment, not superpowers.", "I protect a city that has many unusual villains.", "My alter ego is billionaire Bruce Wayne.", "I wear a bat-themed costume and protect Gotham City."]},
    {"id": "spiderman", "name": "Spider-Man", "category": "characters", "aliases": ["spiderman", "peter parker", "spider man"],
     "clues": ["Responsibility is an important theme in my life.", "I can cling to walls and sense danger.", "My alter ego is Peter Parker.", "I swing through New York City using webs."]},
    {"id": "vader", "name": "Darth Vader", "category": "characters", "aliases": ["vader", "anakin skywalker"],
     "clues": ["I once followed a very different path.", "My breathing is instantly recognizable.", "I wear black armor and wield a red lightsaber.", "I am Luke Skywalker's father in Star Wars."]},
    {"id": "naruto", "name": "Naruto Uzumaki", "category": "characters", "aliases": ["naruto"],
     "clues": ["I dream of earning the respect of my community.", "I practice a combat art that uses chakra.", "I am a blond ninja dressed mostly in orange.", "My dream is to become Hokage of the Hidden Leaf Village."]},
    {"id": "kirby", "name": "Kirby", "category": "characters", "aliases": [],
     "clues": ["My greatest ability involves taking in new powers.", "I live in Dream Land on Planet Popstar.", "I am a small, round, pink Nintendo hero.", "I inhale enemies to copy their abilities."]},
]

QUESTION_BY_ID = {question["id"]: question for question in QUESTIONS}
CATEGORIES = {"pokemon": "Pokémon", "characters": "Characters", "mixed": "Mixed"}
ROUND_COUNT = 8
POINTS_BY_CLUE = (100, 75, 50, 25)
