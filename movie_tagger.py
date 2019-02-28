import os, subprocess, shutil, re
from tmdbv3api import TMDb, Movie, TV, Genre

from dotenv import load_dotenv

load_dotenv()

tmdb = TMDb()
tmdb.api_key = os.getenv('API_KEY')
tmdb.language = 'en'
# tmdb.debug = True

movie = Movie()
tv = TV()
genre = Genre()
genres = genre.movie_list()

g = dict([(g.id, g.name) for g in genres])

file_w_path = os.path.dirname(os.path.abspath(__file__))
iTunes = "/mnt/storages/storage1/iTunes/iTunes Media/Automatically Add to iTunes"
processed = file_w_path + "/processed"

if not os.path.exists(processed):
    print("Directory: %s doesn't exist. Will be created." % processed)
    try:
        os.makedirs(processed, exist_ok=True)
    except FileExistsError:
        print("During the mkdir operation of %s an error occurred." % processed)
        pass

for fileName in os.listdir(file_w_path):
    if fileName.endswith(".m4v"):
        m = re.findall(r"""(.*?[ .])     # title
                       (\d{4})           # year
                       [ .a-zA-Z]*       # Space, period, or words
                       (\d{3,4}p)?       # Quality
                    """, fileName, re.VERBOSE)

        title = m[0][0].replace('.', ' ').rstrip()
        year = m[0][1]
        quality = m[0][2]

        # https://developers.themoviedb.org/3/movies/get-movie-details
        res = movie.search(title)
        for r in res:
            releaseDate = r.release_date.split('-')[0]

            if year == releaseDate:
                title = r.title
                description = r.overview
                first_genre = g[r.genre_ids[0]]

                # clear old meta data
                subprocess.call(["AtomicParsley", fileName, "--metaEnema", "--overWrite"])

                # add new meta data
                subprocess.call(
                    ["AtomicParsley", fileName, "--overWrite", "--title", title, "--desc", description,
                     "--longdesc", description, "--year", releaseDate, "--genre", first_genre,
                     "--hdvideo", "true", "--stik", "Movie"])
                print("Metadata successfully set for - " + fileName)

                shutil.copy(fileName, iTunes)
                shutil.move(fileName, processed)
                print(fileName + " - added to iTunes.")
