#!/home/jessequinn/.pyenv/versions/3.6.8/envs/tagger-3.6.8/bin/python

"""
Unit tests for Tagger.TaggerTV Class.
"""

from unittest import TestCase
import src.main.python.tagger as tagger


class StandAloneTests(TestCase):
    """
    Test the stand-alone module functions.
    """

    t = tagger.Tagger('keytest', 'pt')

    def test_tagger_api_key(self):
        """
        Test initial api key variables of an instance of Tagger.
        :return:
        """
        self.assertEqual(self.t.tmdb.api_key, 'keytest')

    def test_tagger_language(self):
        """
        Test initial language variable of an instance of Tagger.
        :return:
        """
        self.assertEqual(self.t.tmdb.language, 'pt')
