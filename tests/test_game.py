import unittest

try:
    from app import app
except ModuleNotFoundError as error:
    if error.name != 'flask':
        raise
    app = None

from data import QUESTION_BY_ID, QUESTIONS, ROUND_COUNT
from game import matches_answer, normalize, pick_question, points_for


class GameLogicTests(unittest.TestCase):
    def test_question_pool_is_large_enough_and_unique(self):
        self.assertEqual(len({q['id'] for q in QUESTIONS}), len(QUESTIONS))
        self.assertGreaterEqual(sum(q['category'] == 'pokemon' for q in QUESTIONS), ROUND_COUNT)
        self.assertGreaterEqual(sum(q['category'] == 'characters' for q in QUESTIONS), ROUND_COUNT)
        self.assertTrue(all(len(q['clues']) == 4 for q in QUESTIONS))

    def test_normalize_ignores_punctuation_accents_and_spaces(self):
        self.assertEqual(normalize('POKÉ MON!'), 'pokemon')
        self.assertEqual(normalize(' Spider-Man '), 'spiderman')

    def test_answers_and_aliases(self):
        self.assertTrue(matches_answer(QUESTION_BY_ID['spiderman'], 'peter parker'))
        self.assertTrue(matches_answer(QUESTION_BY_ID['pikachu'], 'PiKaChU'))
        self.assertFalse(matches_answer(QUESTION_BY_ID['pikachu'], ''))
        self.assertFalse(matches_answer(QUESTION_BY_ID['pikachu'], 'bulbasaur'))

    def test_scoring(self):
        self.assertEqual(points_for(0, 0), 100)
        self.assertEqual(points_for(1, 0), 75)
        self.assertEqual(points_for(3, 0), 25)
        self.assertEqual(points_for(0, 2), 80)
        self.assertEqual(points_for(3, 20), 10)
        with self.assertRaises(ValueError):
            points_for(4, 0)

    def test_pick_avoids_repeats_and_respects_category(self):
        first = pick_question('pokemon', [])
        self.assertEqual(first['category'], 'pokemon')
        for _ in range(30):
            second = pick_question('pokemon', [first['id']])
            self.assertNotEqual(first['id'], second['id'])
        self.assertIsNone(pick_question('pokemon', [q['id'] for q in QUESTIONS]))


@unittest.skipIf(app is None, "Flask is not installed")
class WebsiteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True, SECRET_KEY='testing-not-production')
        self.client = app.test_client()
        self.client.get('/')

    def test_start_game_and_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'GUESS', response.data)
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['score'], 0)
            self.assertEqual(sess['round'], 1)

    def test_correct_guess_increases_score_and_next_round(self):
        with self.client.session_transaction() as sess:
            answer = QUESTION_BY_ID[sess['current_id']]['name']
        self.client.post('/guess', data={'guess': answer})
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['score'], 100)
            self.assertEqual(sess['status'], 'won')
            self.assertEqual(len(sess['history']), 1)
        self.client.post('/next')
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['round'], 2)
            self.assertEqual(sess['status'], 'playing')

    def test_incorrect_guess_reduces_potential_score(self):
        self.client.post('/guess', data={'guess': 'thisisnotaname'})
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['wrong_guesses'], 1)
        self.client.post('/hint')
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['clue_index'], 1)
            answer = QUESTION_BY_ID[sess['current_id']]['name']
        self.client.post('/guess', data={'guess': answer})
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['score'], 65)

    def test_skip_and_final_screen(self):
        for i in range(ROUND_COUNT):
            self.client.post('/skip')
            self.client.post('/next')
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['status'], 'finished')
            self.assertEqual(len(sess['history']), ROUND_COUNT)
            self.assertEqual(sess['score'], 0)
        response = self.client.get('/')
        self.assertIn(b'Game complete', response.data)

    def test_category_selection(self):
        self.client.post('/new-game', data={'category': 'characters'})
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['category'], 'characters')
            self.assertEqual(QUESTION_BY_ID[sess['current_id']]['category'], 'characters')


if __name__ == '__main__':
    unittest.main()
