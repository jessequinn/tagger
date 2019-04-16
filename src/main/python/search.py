import requests
import re


class Search(object):
    # API URL
    URL = 'https://api.themoviedb.org/3/'

    def __init__(self, api_key, language='en-US', query='', page=1):
        """

        :param api_key:
        :param language:
        :param query:
        :param page:
        """
        self._api_key = api_key
        self._language = language
        self._query = query
        self._page = page

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        if not bool(re.findall('^[\\w]+$', value)):
            raise ValueError("API KEY must be alphanumerical.")
        self._api_key = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        # TODO: may be use regrex here.
        if '-' not in value:
            raise ValueError("Not using correct language format (ex. en-US).")
        self._language = value

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        # TODO: some sort of filter for query is needed?
        self._query = value

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        # TODO: defaults to 1, maybe allow for multiple page scrolling.
        self._page = value

    # TODO: define deleters for disconnect


class TV(Search):
    def __init__(self, api_key, language='en-US', query='', page=1, season=1, episode=1):
        """

        :param api_key:
        :param language:
        :param query:
        :param page:
        :param season:
        :param episode:
        """
        Search.__init__(self, api_key, language, query, page)
        self._season = season
        self._episode = episode

    @property
    def season(self):
        return self._season

    @season.setter
    def season(self, value):
        if not isinstance(value, int):
            raise TypeError('Value passed must be an integer.')
        self._season = value

    @property
    def episode(self):
        return self._page

    @episode.setter
    def episode(self, value):
        if not isinstance(value, int):
            raise TypeError('Value passed must be an integer.')
        self._episode = value

    def search_tv_show(self):
        """

        :return:
        """
        payload = {'api_key': self.api_key, 'language': self.language, 'query': self.query, 'page': self.page}
        shows_found = requests.get(self.URL + 'search/tv', payload)

        if shows_found.status_code == requests.codes.ok:
            arr = []

            for show in shows_found.json()['results']:

                payload = {
                    'api_key': self.api_key,
                    'language': self.language
                }
                episodes_found = requests.get(self.URL + 'tv/' + str(show['id']) + '/season/' + str(self.season),
                                              payload)
                show_details_found = requests.get(self.URL + 'tv/' + str(show['id']), payload)
                seasons_amount = len(show_details_found.json()['seasons'])

                try:
                    episode_titles = [episode['name'] for episode in
                                      episodes_found.json()['episodes']]
                except KeyError:
                    episode_titles = []

                try:
                    networks = [network['name'] for network in
                                show_details_found.json()['networks']]
                except KeyError:
                    networks = ''

                try:
                    episode_overviews = [episode['overview'] for episode in
                                         episodes_found.json()['episodes']]
                except KeyError:
                    episode_overviews = []

                try:
                    episode_air_dates = [episode['air_date'] for episode in
                                         episodes_found.json()['episodes']]
                except KeyError:
                    episode_air_dates = []

                try:
                    genres = [genres['name'] for genres in
                              show_details_found.json()['genres']]
                except KeyError:
                    genres = ''

                arr.append([
                    show['id'],
                    show['name'],
                    episode_titles,
                    episode_air_dates,
                    episode_overviews,
                    genres,
                    networks,
                    self.season,
                    seasons_amount
                ])

            return arr

        return False


class Movie(Search):
    def __init__(self, api_key, language='en-US', query='', page=1, include_adult=False):
        """

        :param api_key:
        :param language:
        :param query:
        :param page:
        :param include_adult:
        """
        Search.__init__(self, api_key, language, query, page)
        self._include_adult = include_adult

    @property
    def include_adult(self):
        return self._include_adult

    @include_adult.setter
    def include_adult(self, value):
        if not isinstance(value, bool):
            raise TypeError('Value passed must be a boolean.')
        self._include_adult = value

    def search_movie(self):
        """

        :return:
        """
        payload = {
            'api_key': self.api_key,
            'language': self.language,
            'query': self.query, 'page': self.page,
            'include_adult': self.include_adult
        }
        movies_found = requests.get(self.URL + 'search/movie', payload)

        if movies_found.status_code == requests.codes.ok:
            arr = []

            for movie in movies_found.json()['results']:

                payload = {'api_key': self.api_key, 'language': self.language}
                movie_details_found = requests.get(self.URL + 'movie/' + str(movie['id']), payload)

                try:
                    genres = [genres['name'] for genres in
                              movie_details_found.json()['genres']]
                except KeyError:
                    genres = ''

                arr.append([
                    movie['id'],
                    movie['title'],
                    movie['release_date'],
                    movie['overview'],
                    genres
                ])

            return arr

        return False
