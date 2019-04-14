import requests


class Search(object):
    def __init__(self, api_key, language='en-US'):
        self.api_key = api_key
        self.language = language

    def get_api_key(self) -> str:
        return self.api_key

    def get_language(self) -> str:
        return self.language


class TV(Search):
    # API URL
    URL = 'https://api.themoviedb.org/3/'

    def __init__(self, api_key, language='en-US'):
        """

        :param api_key:
        :param language:
        """
        Search.__init__(self, api_key, language)

    def search_tv_show(self, query, page=1, season=1):
        """

        :param query:
        :param page:
        :param season:
        :return:
        """
        payload = {'api_key': self.api_key, 'language': self.language, 'query': query, 'page': page}
        shows_found = requests.get(self.URL + 'search/tv', payload)

        if shows_found.status_code == requests.codes.ok:
            arr = []

            for show in shows_found.json()['results']:

                payload = {
                    'api_key': self.api_key,
                    'language': self.language
                }
                episodes_found = requests.get(self.URL + 'tv/' + str(show['id']) + '/season/' + str(season), payload)
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
                    season,
                    seasons_amount
                ])

            return arr

        return False


class Movie(Search):
    # API URL
    URL = 'https://api.themoviedb.org/3/'

    def __init__(self, api_key, language='en-US'):
        """

        :param api_key:
        :param language:
        """
        Search.__init__(self, api_key, language)

    def search_movie(self, query, page=1, include_adult=False):
        """

        :param query:
        :param page:
        :param include_adult:
        :return:
        """
        payload = {
            'api_key': self.api_key,
            'language': self.language,
            'query': query, 'page': page,
            'include_adult': include_adult
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
