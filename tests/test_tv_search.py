"""
Unit tests for Search.TV Class.
"""

from unittest import TestCase
import src.main.python.search as search
from dotenv import load_dotenv
import os

load_dotenv()


class TaggerTVTests(TestCase):
    def setUp(self):
        self.tv = search.TV(os.getenv('API_KEY'), language='en-US', query='game of thrones', season=1)

    def test_search_api_key(self):
        """
        Test initial api key variables of an instance of TV.
        :return:
        """
        self.assertEqual(self.tv.api_key, os.getenv('API_KEY'))
        with self.assertRaises(ValueError):
            self.tv.api_key = '-sdfdsfdse43434'

    def test_search_language(self):
        """
        Test initial language variable of an instance of TV.
        :return:
        """
        self.assertEqual(self.tv.language, 'en-US')
        with self.assertRaises(ValueError):
            self.tv.language = 'enUS'

    def test_search_results(self):
        """
        Test if an array is returned with proper contents.
        :return:
        """
        self.assertEqual(
            self.tv.search_tv_show()[0],
            [1399, 'Game of Thrones',
             ['Winter Is Coming', 'The Kingsroad', 'Lord Snow', 'Cripples, Bastards, and Broken Things',
              'The Wolf and the Lion', 'A Golden Crown', 'You Win or You Die', 'The Pointy End', 'Baelor',
              'Fire and Blood'],
             ['2011-04-17', '2011-04-24', '2011-05-01', '2011-05-08', '2011-05-15', '2011-05-22', '2011-05-29',
              '2011-06-05', '2011-06-12', '2011-06-19'], [
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
             ['Sci-Fi & Fantasy', 'Drama', 'Action & Adventure'], ['HBO'], 1, 9]
        )
