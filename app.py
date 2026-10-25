"""Flask website for the Pokémon / Character guessing game."""

import os

from flask import Flask, redirect, render_template, request, session, url_for

from data import CATEGORIES, QUESTION_BY_ID, ROUND_COUNT
from game import matches_answer, pick_question, points_for

app = Flask(__name__)
# For local development only. Set SECRET_KEY to a random value before deployment.
app.secret_key = os.environ.get("SECRET_KEY", "local-development-only-change-me")


def begin_round():
    question = pick_question(session["category"], session["seen"])
    session["current_id"] = question["id"] if question else None
    if question:
        session["seen"] = [*session["seen"], question["id"]]
    session["clue_index"] = 0
    session["wrong_guesses"] = 0
    session["status"] = "playing" if question else "finished"
    session["feedback"] = ""
    session["feedback_type"] = ""
    session["earned"] = 0


def begin_game(category="pokemon"):
    session.clear()
    session["category"] = category if category in CATEGORIES else "pokemon"
    session["score"] = 0
    session["round"] = 1
    session["seen"] = []
    session["history"] = []
    begin_round()


def record_result(question, result, points):
    session["history"] = [*session["history"], {
        "name": question["name"], "result": result, "points": points,
    }]


def current_question():
    return QUESTION_BY_ID.get(session.get("current_id"))


def say(message, kind="info"):
    session["feedback"] = message
    session["feedback_type"] = kind


@app.get("/")
def index():
    if "category" not in session:
        begin_game()
    question = current_question()
    status = session["status"]
    clue_index = session.get("clue_index", 0)
    wrong_guesses = session.get("wrong_guesses", 0)
    won_count = sum(entry["result"] == "won" for entry in session["history"])
    return render_template(
        "index.html",
        categories=CATEGORIES,
        category=session["category"],
        category_label=CATEGORIES[session["category"]],
        question=question,
        status=status,
        clue_index=clue_index,
        wrong_guesses=wrong_guesses,
        visible_clues=question["clues"][:clue_index + 1] if question else [],
        possible_points=points_for(clue_index, wrong_guesses) if question and status == "playing" else 0,
        score=session["score"],
        round_number=session["round"],
        total_rounds=ROUND_COUNT,
        history=list(reversed(session["history"])),
        won_count=won_count,
        feedback=session.get("feedback", ""),
        feedback_type=session.get("feedback_type", ""),
        earned=session.get("earned", 0),
    )


@app.post("/new-game")
def new_game():
    begin_game(request.form.get("category", "pokemon"))
    return redirect(url_for("index"))


@app.post("/guess")
def guess():
    question = current_question()
    if not question or session.get("status") != "playing":
        return redirect(url_for("index"))
    attempt = request.form.get("guess", "").strip()[:100]
    if not attempt:
        say("Type a name before submitting your guess.")
    elif matches_answer(question, attempt):
        earned = points_for(session["clue_index"], session["wrong_guesses"])
        session["score"] += earned
        session["earned"] = earned
        session["status"] = "won"
        record_result(question, "won", earned)
        say(f"Nailed it! You earned {earned} points.", "success")
    else:
        session["wrong_guesses"] += 1
        say("Not quite! Try another guess or unlock the next clue.", "error")
    return redirect(url_for("index"))


@app.post("/hint")
def hint():
    question = current_question()
    if question and session.get("status") == "playing":
        if session["clue_index"] < len(question["clues"]) - 1:
            session["clue_index"] += 1
            say("A new clue is unlocked. You've got this!")
        else:
            say("All clues are unlocked. Give it your best shot!")
    return redirect(url_for("index"))


@app.post("/skip")
def skip():
    question = current_question()
    if question and session.get("status") == "playing":
        session["status"] = "skipped"
        record_result(question, "skipped", 0)
        say(f"The answer was {question['name']}. You can get the next one!", "info")
    return redirect(url_for("index"))


@app.post("/next")
def next_round():
    if session.get("status") in ("won", "skipped"):
        if session["round"] >= ROUND_COUNT:
            session["current_id"] = None
            session["status"] = "finished"
            say("That's a wrap! Choose a category to play again.", "success")
        else:
            session["round"] += 1
            begin_round()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
