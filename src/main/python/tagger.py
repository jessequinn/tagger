from tmdbv3api import TMDb, Movie, Genre, TV, Season


class Tagger(object):
    """
    Base Class Tagger contains TMDB() instance, language, and key
    """
    def __init__(self, key, language='en'):
        self.tmdb = TMDb()
        self.tmdb.api_key = key
        self.tmdb.language = language

    def get_api_key(self) -> str:
        return self.tmdb.api_key

    def get_language(self) -> str:
        return self.tmdb.language


class TaggerMovie(Tagger):
    def __init__(self, key, language='en'):
        Tagger.__init__(self, key, language)
        self.movie = Movie()
        self.genres = Genre().movie_list()

    def get_genres(self) -> dict:
        return dict([(g.id, g.name) for g in self.genres])

    def search_results(self, title):
        """
        Search results for a movie
        :param title:
        :return: Returns an array that contains id, title, release date, overview, and first genre.
        """
        g = self.get_genres()
        arr = []

        for item in self.movie.search(title):
            title = item.title

            try:
                release_date = item.release_date.split('-')[0]
            except IndexError:
                release_date = ''

            try:
                overview = item.overview
            except IndexError:
                overview = ''

            try:
                first_genre = g[item.genre_ids[0]]
            except IndexError:
                first_genre = ''

            arr.append([item.id, title, release_date, overview, first_genre])

        return arr


class TaggerTV(Tagger):
    def __init__(self, key, language='en'):
        Tagger.__init__(self, key, language)
        self.tv = TV()

    def search_results(self, show, season):
        """
        Search results for a season.
        :param show:
        :param season:
        :return arr: Returns multidimensional array
        """
        results = self.tv.search(show)
        arr = []

        for item in results:
            s = Season()
            tv_details = self.tv.details(item.id)
            show_name = tv_details.name
            show_season = s.details(item.id, season)
            seasons_amount = len(tv_details.seasons)

            if season <= seasons_amount:
                try:
                    episode_titles = [episode['name'] for episode in
                                      show_season.episodes]
                except IndexError:
                    episode_titles = []
                except AttributeError:
                    episode_titles = []

                try:
                    network = tv_details.networks[0]['name']
                except IndexError:
                    network = ''

                try:
                    episode_overviews = [episode['overview'] for episode in
                                         show_season.episodes]
                except IndexError:
                    episode_overviews = []
                except AttributeError:
                    episode_overviews = []

                try:
                    episode_air_dates = [episode['air_date'] for episode in
                                         show_season.episodes]
                except IndexError:
                    episode_air_dates = []
                except AttributeError:
                    episode_air_dates = []

                try:
                    first_genre = tv_details.genres[0]['name']
                except IndexError:
                    first_genre = ''

                arr.append(
                    [item.id, show_name, episode_titles, episode_air_dates, episode_overviews, first_genre, network,
                     season, seasons_amount])

        return arr
