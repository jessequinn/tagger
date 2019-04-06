import click
import os
import subprocess
import shutil
import re
from tmdbv3api import TMDb, Movie, Genre

from dotenv import load_dotenv

load_dotenv()

tmdb = TMDb()
tmdb.api_key = os.getenv('API_KEY')
tmdb.language = 'en'


# tmdb.debug = True


@click.command()
@click.option('--movies', help='Uses the TMDB to search titles for movies.', default=1)
@click.option('--shows', help='Uses the TMDB to search titles for shows.', default=0)
def main(movies, shows):
    if movies:
        movie = Movie()
        genre = Genre()
        genres = genre.movie_list()
        g = dict([(g.id, g.name) for g in genres])

        file_w_path = os.path.dirname(os.path.abspath(__file__))
        processed = file_w_path + '/processed'
        unprocessed = file_w_path + '/unprocessed'

        # creates the processed folder where all processed movie
        if not os.path.exists(processed):
            click.echo("Directory: %s doesn't exist. Will be created." % processed)
            try:
                os.makedirs(processed, exist_ok=True)
            except FileExistsError:
                click.echo("During the mkdir operation of %s an error occurred." % processed)
                pass

        # creates an unprocessed folder where you will place the movies or shows to be processed
        if not os.path.exists(unprocessed):
            click.echo("Directory: %s doesn't exist. Will be created." % unprocessed)
            try:
                os.makedirs(unprocessed, exist_ok=True)
            except FileExistsError:
                click.echo("During the mkdir operation of %s an error occurred." % unprocessed)
                pass

        for path, subdirs, files in os.walk(file_w_path):
            if 'unprocessed' in path:
                for file in files:
                    file_path = os.path.join(path, file)
                    click.echo(file)

                    if file.endswith('.mp4') or file.endswith('.m4v') or file.endswith('.mkv') and not file.startswith('.'):
                        m = re.findall(r"""^(
                          (?P<ShowNameA>.*[^ (_.]) # Show name
                            [ (_.]+
                            ( # Year with possible Season and Episode
                              (?P<ShowYearA>\d{4})
                              ([ (_.]+S(?P<SeasonA>\d{1,2})E(?P<EpisodeA>\d{1,2}))?
                            | # Season and Episode only
                              (?<!\d{4}[ (_.])
                              S(?P<SeasonB>\d{1,2})E(?P<EpisodeB>\d{1,2})
                            | # Alternate format for episode
                              (?P<EpisodeC>\d{3})
                            )
                        |
                          # Show name with no other information
                          (?P<ShowNameB>.+)
                        )""", file, re.VERBOSE)
                        click.echo(m)
                        search_title = m[0][0]

                        while True:
                            try:
                                assert click.confirm(
                                    'Search will use the following title: ' + search_title + '. Is it correct?')
                            except AssertionError:
                                search_title = click.prompt('Please enter the correct title then: ', type=str)
                            else:
                                break

                        # https://developers.themoviedb.org/3/movies/get-movie-details
                        res = movie.search(search_title)

                        # select the first three results and place into a menu
                        for idx, item in enumerate(res[:3]):
                            title = item.title
                            description = item.overview
                            releaseDate = item.release_date.split('-')[0]

                            click.secho(str(idx + 1) + ': ', fg='red')
                            click.secho('\tTitle: ' + title, fg='yellow')
                            click.secho('\tDescription: ' + description, fg='yellow')
                            click.secho('\tRelease Date: ' + releaseDate, fg='yellow')

                        while True:
                            try:
                                option = click.prompt('Please enter a valid integer: ', default=1, type=int)
                                assert 0 < option < 4
                            except ValueError:
                                click.echo("Not an integer! Please enter an integer.")
                            except AssertionError:
                                click.echo("Please enter an integer between 1 and 3")
                            else:
                                break

                        click.echo('\n')
                        click.echo("You selected: " + str(option))

                        idx = option - 1

                        title = res[idx].title
                        description = res[idx].overview
                        first_genre = g[res[idx].genre_ids[0]]
                        releaseDate = res[idx].release_date.split('-')[0]

                        click.echo('\n')
                        click.secho('\t' + title, fg='yellow')
                        click.secho('\t' + description, fg='yellow')
                        click.secho('\t' + first_genre, fg='yellow')
                        click.secho('\t' + releaseDate, fg='yellow')

                        # add new meta data
                        subprocess.call(
                            ["AtomicParsley", file_path, "--overWrite", "--title", title, "--desc", description,
                             "--longdesc", description, "--year", releaseDate, "--genre", first_genre,
                             "--hdvideo", "true", "--stik", "Movie"])

                        shutil.move(file_path, processed)
                        # following naming convention for Plex
                        # https://support.plex.tv/articles/200381023-naming-movie-files/
                        os.rename(processed + '/' + file,
                                  processed + '/' + title + ' (' + releaseDate + ')' + os.path.splitext(file)[1].lower())
                        click.echo(file + " was processed successfully.")

                        try:
                            shutil.rmtree(path)
                        except OSError as e:
                            print("Error: %s - %s." % (e.filename, e.strerror))


if __name__ == '__main__':
    main()
