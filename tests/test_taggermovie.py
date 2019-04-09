#!/home/jessequinn/.pyenv/versions/3.6.8/envs/tagger-3.6.8/bin/python

"""
Unit tests for Tagger.TaggerMovie Class.
"""

from unittest import TestCase
import src.main.python.tagger as tagger
from dotenv import load_dotenv
import os

load_dotenv()


class TaggerTVTests(TestCase):
    def setUp(self) -> None:
        self.movie = tagger.TaggerMovie(os.getenv('API_KEY'), language='fr')

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
        self.assertEqual(self.movie.get_language(), 'fr')
