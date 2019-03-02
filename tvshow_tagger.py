import os, subprocess, shutil, re

from tmdbv3api import TMDb, TV, Season

from dotenv import load_dotenv

load_dotenv()

tmdb = TMDb()
tmdb.api_key = os.getenv('API_KEY')
tmdb.language = 'en'
# tmdb.debug = True

tv = TV()

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
        t = re.findall(r"""(.*)          # Title
                        [ .]
                        S(\d{1,2})    # Season
                        E(\d{1,2})    # Episode
                        [ .a-zA-Z]*  # Space, period, or words like PROPER/Buried
                        (\d{3,4}p)?   # Quality
                    """, fileName, re.VERBOSE)

        show = t[0][0].replace('.', ' ')
        s = int(t[0][1])
        e = int(t[0][2])

        # https://developers.themoviedb.org/3/tv/get-tv-details
        res = tv.search(show)
        for r in res:
            season = Season()
            tv_details = tv.details(r.id)
            show_season = season.details(r.id, s)
            title = show_season.episodes[e - 1]['name']
            network = tv_details.networks[0]['name']
            description = show_season.episodes[e - 1]['overview']
            airDate = show_season.episodes[e - 1]['air_date']
            first_genre = tv_details.genres[0]['name']

            # clear old meta data
            subprocess.call(["AtomicParsley", fileName, "--metaEnema", "--overWrite"])

            # add new meta data
            subprocess.call(["AtomicParsley", fileName, "--overWrite", "--TVShowName", show,
                             "--TVSeasonNum", str(s), "--TVEpisodeNum", str(e), "--title", title, "--TVNetwork",
                             network, "--desc", description, "--longdesc", description, "--year", airDate,
                             "--genre", first_genre, "--track", str(e), "--disk", str(s), "--hdvideo",
                             "true", "--stik", "TV Show"])

            print("Metadata successfully set for - " + fileName)

            shutil.move(fileName, processed)
            print(fileName + " - added to iTunes.")
