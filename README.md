# Who's That? ⚡🎭

A colorful browser-based **Guess the Pokémon / Character** game. Built with **Python, Flask, HTML, CSS and a little JavaScript** as a portfolio-friendly beginner project.

**Version 1.2:** character illustrations, Pokémon artwork silhouettes, animated clues, and answer reveals.

## Features

- ⚡ Play Pokémon rounds, 🎭 fictional-character rounds, or 🎲 mixed rounds.
- 🧩 Four clues per character, from difficult to easier.
- 💯 Earn **100 points** on the first clue. Each added clue lowers the points by 25, and each incorrect guess lowers them by 10 (minimum 10 for a correct answer).
- ✅ Flexible guesses: case, spaces, punctuation, accents, and common aliases are accepted.
- 🏆 An eight-round game with a running score, round history, and a final results screen.
- 🔀 Random questions without repeats within a game.
- 🖼️ Hidden Pokémon silhouettes that become less blurry as you unlock clues; a full-art reveal when you guess or skip.
- 🎨 Twelve local, original stylized SVG portraits for the fictional-character category.
- ✨ A celebratory image pop and sparkle animation for correct guesses, animated clues, and subtle floating artwork. Respects reduced-motion settings.
- 📱 Responsive layout for phone and desktop.
- 🧪 Automated tests with Python's built-in `unittest`, plus GitHub Actions checks on pushes and pull requests.

## Quick start (Mac / Linux)

Open Terminal in the extracted project folder:

```bash
cd ~/Downloads/pokemon-character-guess-game
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser. To stop the server, press **Ctrl+C** in Terminal.

> If another program is using port 5000 on your Mac, edit the last line of `app.py` to `app.run(debug=True, port=5001)` and visit http://127.0.0.1:5001 instead.

### Windows

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

## Test your code

With the virtual environment activated (including Flask installed):

```bash
python -m unittest discover -s tests -v
```

## Files

```text
pokemon-character-guess-game/
├── app.py                # Flask routes, sessions, round management
├── media.py              # Pokémon artwork and local character image URLs
├── game.py               # Rules: answers, matching, points, random picks
├── data.py               # 24 Pokémon / character entries, 4 clues each
├── templates/
│   └── index.html        # Browser interface
├── static/
│   ├── characters/       # Twelve hand-drawn vector portraits
│   ├── styles.css        # Responsive design + animations
│   └── game.js           # Input focus + image loading fallback
├── scripts/
│   └── generate_character_art.py # Rebuild character illustrations
├── tests/
│   └── test_game.py      # Logic and website checks
├── .github/workflows/
│   └── tests.yml         # GitHub Actions automated test workflow
├── requirements.txt
├── .gitignore
└── README.md
```

## Images and animations

- **Pokémon images:** The game loads high-resolution artwork directly from the [PokeAPI sprites repository](https://github.com/PokeAPI/sprites). An internet connection is needed to see these images. The game stays playable if an image fails to load, and shows a question-mark fallback.
- **Fictional characters:** The twelve stylized SVG illustrations are included locally in `static/characters/`, so they work offline. To edit or regenerate them, open `scripts/generate_character_art.py` and run `python scripts/generate_character_art.py`.
- **During guessing:** Images stay blacked out. The blur decreases with each additional clue, revealing a clearer silhouette.
- **After a correct guess or skip:** The image reveals its color. Correct guesses also trigger celebratory sparkles.
- **Accessibility:** Users who select *Reduce motion* in system settings won't receive motion animations.

### Artwork and rights

Pokémon artwork linked from PokéAPI is copyrighted by **The Pokémon Company** ([upstream licensing notice](https://github.com/PokeAPI/sprites/blob/master/LICENCE.txt)). This fan-learning project is unofficial; linking to the images does **not** grant ownership or permission to redistribute them. The included fictional character illustrations are original, simplified fan-style drawings, and their names/likenesses remain associated with their respective owners. For a public or commercial release, check the relevant image and trademark permissions first.

## Push to GitHub **without** GitHub CLI

1. Create a new **empty** GitHub repository at https://github.com/new, named `pokemon-character-guess-game`. Do **not** add a README, `.gitignore`, or license during creation; they're in this folder.
2. Run these commands **inside your extracted project folder**:

```bash
git init
git branch -M main
git add .
git commit -m "Build Pokemon and character guessing game"
git remote add origin https://github.com/YOUR_USERNAME/pokemon-character-guess-game.git
git push -u origin main
```

Change `YOUR_USERNAME` to your GitHub username. You can copy the correct HTTPS URL from the new repo's GitHub page. If `origin` already exists, use `git remote set-url origin YOUR_HTTPS_URL` instead of adding it again.

If `git push` gives `Repository not found`, first verify the repository really exists on GitHub and confirm the URL using `git remote -v`. A new local `git init` does **not** create a repository on GitHub.

If you are prompted for a GitHub password, GitHub requires a supported authentication method such as a credential manager/browser login or personal access token for HTTPS Git operations; your account password alone will not work.

## Make a new change with a feature branch

```bash
git switch -c feature/new-characters
# Edit data.py and run the tests
git add .
git commit -m "Add new game characters"
git push -u origin feature/new-characters
```

Then open the repository on GitHub and use **Compare & pull request**. You do not need the `gh` command.

## Add your own questions

Add another dictionary in `data.py` with a unique `id`, `name`, `category` (`pokemon` or `characters`), optional `aliases`, and **four** clues, arranged from tricky to easy. The app picks up the new question automatically.

## Before deploying to the public internet

This is a **local development demo** using Flask debug mode and browser session cookies. For production, turn debug mode off and set a long random `SECRET_KEY` environment variable. For competitive public play, also move round state to a trusted server-side data store; a Flask signed client-side session is not designed as an anti-cheat system. This starter does not include authentication or a shared leaderboard. The user can also inspect question/image URLs in the browser, so the game is designed for casual play rather than competitive anti-cheat.

*Not affiliated with Nintendo, The Pokémon Company, or the owners of the fictional characters mentioned.*
