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
        self.tv = tagger.TaggerTV(os.getenv('API_KEY'), language='en')

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
        self.assertEqual(self.tv.get_language(), 'en')

    def test_search_results(self):
        """
        Test if an array is returned with proper contents.
        :return:
        """
        self.assertEqual(self.tv.search_results(show='game of thrones', season=1)[0],
                         [1399, 'Game of Thrones',
                          ['Winter Is Coming', 'The Kingsroad', 'Lord Snow', 'Cripples, Bastards, and Broken Things',
                           'The Wolf and the Lion', 'A Golden Crown', 'You Win or You Die', 'The Pointy End', 'Baelor',
                           'Fire and Blood'],
                          ['2011-04-17', '2011-04-24', '2011-05-01', '2011-05-08', '2011-05-15', '2011-05-22',
                           '2011-05-29', '2011-06-05', '2011-06-12', '2011-06-19'],
                          [
                              "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
                              'While Bran recovers from his fall, Ned takes only his daughters to Kings Landing. Jon Snow goes with his uncle Benjen to The Wall. Tyrion joins them.',
                              "Lord Stark and his daughters arrive at King's Landing to discover the intrigues of the king's realm.",
                              "Eddard investigates Jon Arryn's murder. Jon befriends Samwell Tarly, a coward who has come to join the Night's Watch.",
                              'Catelyn has captured Tyrion and plans to bring him to her sister, Lysa Arryn, at The Vale, to be tried for his, supposed, crimes against Bran. Robert plans to have Daenerys killed, but Eddard refuses to be a part of it and quits.',
                              'While recovering from his battle with Jamie, Eddard is forced to run the kingdom while Robert goes hunting. Tyrion demands a trial by combat for his freedom. Viserys is losing his patience with Drogo.',
                              "Robert has been injured while hunting and is dying. Jon and the others finally take their vows to the Night's Watch. A man, sent by Robert, is captured for trying to poison Daenerys. Furious, Drogo vows to attack the Seven Kingdoms.",
                              'Eddard and his men are betrayed and captured by the Lannisters. When word reaches Robb, he plans to go to war to rescue them. The White Walkers attack The Wall. Tyrion returns to his father with some new friends.',
                              "Robb goes to war against the Lannisters. Jon finds himself struggling on deciding if his place is with Robb or the Night's Watch. Drogo has fallen ill from a fresh battle wound. Daenerys is desperate to save him.",
                              "With Ned dead, Robb vows to get revenge on the Lannisters. Jon must officially decide if his place is with Robb or the Night's Watch. Daenerys says her final goodbye to Drogo."],
                          'Sci-Fi & Fantasy', 'HBO', 1, 9]
                         )
