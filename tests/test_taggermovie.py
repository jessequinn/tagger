#!/home/jessequinn/.pyenv/versions/3.6.8/envs/tagger-3.6.8/bin/python

"""
Unit tests for Tagger.TaggerMovie Class.
"""

from unittest import TestCase
import src.main.python.tagger as tagger
from dotenv import load_dotenv
import os

load_dotenv()


class TaggerMovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = tagger.TaggerMovie(os.getenv('API_KEY'), language='en')

    def test_tagger_api_key(self):
        """
        Test initial api key variables of an instance of Tagger.
        :return:
        """
        self.assertEqual(self.movie.get_api_key(), os.getenv('API_KEY'))

    def test_tagger_language(self):
        """
        Test initial language variable of an instance of Tagger.
        :return:
        """
        self.assertEqual(self.movie.get_language(), 'en')

    def test_tagger_movie_genre(self):
        """
        Test if genre returns with a dictionary.
        :return:
        """
        g = self.movie.get_genres()
        self.assertTrue(g.get(28) == 'Action')

    def test_search_results(self):
        """
        Test if an array is returned with proper contents.
        :return:
        """
        self.assertEqual(self.movie.search_results(title='top gun')[0],
                         [744, 'Top Gun', '1986',
                          "For Lieutenant Pete 'Maverick' Mitchell and his friend and co-pilot Nick 'Goose' Bradshaw, being accepted into an elite training school for fighter pilots is a dream come true. But a tragedy, as well as personal demons, will threaten Pete's dreams of becoming an ace pilot.",
                          'Action']
                         )
