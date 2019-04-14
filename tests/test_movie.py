#!/home/jessequinn/.pyenv/versions/3.6.8/envs/Search-3.6.8/bin/python

"""
Unit tests for Search.Movie Class.
"""

from unittest import TestCase
import src.main.python.search as search
from dotenv import load_dotenv
import os

load_dotenv()


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = search.Movie(os.getenv('API_KEY'), language='en-US')

    def test_search_api_key(self):
        """
        Test initial api key variables of an instance of Movie.
        :return:
        """
        self.assertEqual(self.movie.get_api_key(), os.getenv('API_KEY'))

    def test_search_language(self):
        """
        Test initial language variable of an instance of Movie.
        :return:
        """
        self.assertEqual(self.movie.get_language(), 'en-US')

    def test_search_results(self):
        """
        Test if an array is returned with proper contents.
        :return:
        """
        self.assertEqual(
            self.movie.search_movie(query='top gun')[0],
            [744, 'Top Gun', '1986-05-16',
             "For Lieutenant Pete 'Maverick' Mitchell and his friend and co-pilot Nick 'Goose' Bradshaw, being accepted into an elite training school for fighter pilots is a dream come true. But a tragedy, as well as personal demons, will threaten Pete's dreams of becoming an ace pilot.",
             ['Action', 'Romance']]

        )
