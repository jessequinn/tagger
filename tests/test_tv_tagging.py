"""
Unit tests for Tagging.ShowMetaTag Class.
https://sample-videos.com/ for video samples
"""

from unittest import TestCase
from mutagen.mp4 import MP4
import src.main.python.tagging as tagging
import os


class ShowMetaTag(TestCase):
    def setUp(self):
        self.movie_metatag = tagging.ShowMetaTag(os.getcwd() + '/SampleVideo_1280x720_1mb.mp4')
        self.movie_metatag.set_show_title('Game of Thrones')
        self.movie_metatag.set_episode_title('Winter Is Coming')
        self.movie_metatag.set_description(
            "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.")
        self.movie_metatag.set_date('2011-04-17')
        self.movie_metatag.set_genre('Sci-Fi & Fantasy')
        self.movie_metatag.set_network('HBO')
        self.movie_metatag.set_episode(1)
        self.movie_metatag.set_season(1)

    def test_metatag(self):
        self.assertTrue(type(self.movie_metatag.meta_tag) is MP4)
        self.assertEqual(self.movie_metatag.meta_tag['\xa9nam'], ['Winter Is Coming'])
        self.assertEqual(self.movie_metatag.meta_tag['desc'], [
            "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."])
        self.assertEqual(self.movie_metatag.meta_tag['ldes'], [
            "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army."])
        self.assertEqual(self.movie_metatag.meta_tag['\xa9day'], ['2011-04-17'])
        self.assertEqual(self.movie_metatag.meta_tag['\xa9gen'], ['Sci-Fi & Fantasy'])
        self.assertEqual(self.movie_metatag.meta_tag['tvsh'], ['Game of Thrones'])
        self.assertEqual(self.movie_metatag.meta_tag['tvsn'], [1])
        self.assertEqual(self.movie_metatag.meta_tag['disk'], [(1, 0)])
        self.assertEqual(self.movie_metatag.meta_tag['tves'], [1])
        self.assertEqual(self.movie_metatag.meta_tag['trkn'], [(1, 0)])
        self.assertEqual(self.movie_metatag.meta_tag['tvnn'], ['HBO'])
