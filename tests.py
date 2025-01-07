import unittest
from questions import *
from answers import *


class check_fx_is_correct(unittest.TestCase):
    ##test de la fonction is_correct avec une bonne reponse
    def test_correct_answer(self):
        test_question = Question("Quelle est la capitale de la france ?", Choice(["Londres", "Paris", "Berlin"], "b"))
        test_user_input = test_question.answer # on récupère directement la bonne reponse
        self.assertEqual(is_correct(test_question, test_user_input), True)


if __name__ == '__main__':
    unittest.main()