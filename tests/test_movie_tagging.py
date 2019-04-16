"""
Unit tests for Tagging.FilmMetaTag Class.
https://sample-videos.com/ for video samples
"""

from unittest import TestCase
from mutagen.mp4 import MP4
import src.main.python.tagging as tagging
import os


class FilmMetaTagTests(TestCase):
    def setUp(self):
        self.movie_metatag = tagging.FilmMetaTag(os.getcwd() + '/SampleVideo_1280x720_1mb.mp4')
        self.movie_metatag.set_title('Top Gun')
        self.movie_metatag.set_description(
            "For Lieutenant Pete 'Maverick' Mitchell and his friend and co-pilot Nick 'Goose' Bradshaw, being accepted into an elite training school for fighter pilots is a dream come true. But a tragedy, as well as personal demons, will threaten Pete's dreams of becoming an ace pilot.")
        self.movie_metatag.set_date('1986-05-16')
        self.movie_metatag.set_genre('Action')

    def test_metatag(self):
        self.assertTrue(type(self.movie_metatag.meta_tag) is MP4)
        self.assertEqual(self.movie_metatag.meta_tag['\xa9nam'], ['Top Gun'])
        self.assertEqual(self.movie_metatag.meta_tag['desc'], [
            "For Lieutenant Pete 'Maverick' Mitchell and his friend and co-pilot Nick 'Goose' Bradshaw, being accepted into an elite training school for fighter pilots is a dream come true. But a tragedy, as well as personal demons, will threaten Pete's dreams of becoming an ace pilot."])
        self.assertEqual(self.movie_metatag.meta_tag['ldes'], [
            "For Lieutenant Pete 'Maverick' Mitchell and his friend and co-pilot Nick 'Goose' Bradshaw, being accepted into an elite training school for fighter pilots is a dream come true. But a tragedy, as well as personal demons, will threaten Pete's dreams of becoming an ace pilot."])
        self.assertEqual(self.movie_metatag.meta_tag['\xa9day'], ['1986-05-16'])
        self.assertEqual(self.movie_metatag.meta_tag['\xa9gen'], ['Action'])
