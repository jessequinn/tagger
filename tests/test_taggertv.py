#!/home/jessequinn/.pyenv/versions/3.6.8/envs/tagger-3.6.8/bin/python

"""
Unit tests for Tagger.TaggerTV Class.
"""

from unittest import TestCase
import src.main.python.tagger as tagger
from dotenv import load_dotenv
import os

load_dotenv()


class TaggerTVTests(TestCase):
    def setUp(self) -> None:
        self.tv = tagger.TaggerTV(os.getenv('API_KEY'), language='pt')

    def test_tagger_api_key(self):
        """
        Test initial api key variables of an instance of Tagger.
        :return:
        """
        self.assertEqual(self.tv.get_api_key(), os.getenv('API_KEY'))

    def test_tagger_language(self):
        """
        Test initial language variable of an instance of Tagger.
        :return:
        """
        self.assertEqual(self.tv.get_language(), 'pt')
