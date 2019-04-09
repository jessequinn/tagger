#!/home/jessequinn/.pyenv/versions/3.6.8/envs/tagger-3.6.8/bin/python

"""
Unit tests for Tagger.TaggerTV Class.
"""

from unittest import TestCase
from mock import patch
import src.main.python.tagger as tagger


class StandAloneTests(TestCase):
    """
    Test the stand-alone module functions.
    """

    t = tagger.Tagger('keytest', 'pt')

    @patch('__builtin__.open')
    def test_tagger_api_key(self):
        """
        Test intial variables of an instance of Tagger
        :return:
        """
        self.assertEqual(t.tmdb.api_key, 'keytest')
