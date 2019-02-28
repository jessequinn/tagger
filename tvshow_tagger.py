import os, tvdb_api, subprocess, shutil, re

tvdb = tvdb_api.Tvdb()
file_w_path = os.path.dirname(os.path.abspath(__file__))
iTunes = "/mnt/storages/storage1/iTunes/iTunes Media/Automatically Add to iTunes"
completed = file_w_path + "/completed"

if not os.path.exists(completed):
    print("Directory: %s doesn't exist. Will be created." % completed)
    try:
        os.makedirs(completed, exist_ok=True)
    except FileExistsError:
        print("During the mkdir operation of %s an error occurred." % completed)
        pass

# Unicode -> ascii punctuation substitutions (left/right + single/double quotes)
punctuation = {0x2018: 0x27, 0x2019: 0x27, 0x201C: 0x22, 0x201D: 0x22}

for fileName in os.listdir(file_w_path):
    if fileName.endswith(".m4v"):
        tv = re.findall(r"""(.*)          # Title
                        [ .]
                        S(\d{1,2})    # Season
                        E(\d{1,2})    # Episode
                        [ .a-zA-Z]*  # Space, period, or words like PROPER/Buried
                        (\d{3,4}p)?   # Quality
                    """, fileName, re.VERBOSE)

        show = tv[0][0].replace('.', ' ')
        season = tv[0][1]
        episode = tv[0][2]
        title = tvdb[show][int(season)][int(episode)]['episodename']
        network = tvdb[show]['network']
        description = tvdb[show][int(season)][int(episode)]['overview']
        airDate = tvdb[show][int(season)][int(episode)]['firstaired']
        genre = (tvdb[show]['genre'])[1:len(tvdb[show]['genre'])]
        fileInfo = show + " - " + episode

        # clear old meta data
        subprocess.call(["AtomicParsley", fileName, "--metaEnema", "--overWrite"])

        # add new meta data
        subprocess.call(
                ["AtomicParsley", fileName, "--overWrite", "--TVShowName", show, "--TVSeasonNum",
                 season, "--TVEpisodeNum", episode, "--title", title, "--TVNetwork", network, "--desc", description,
                 "--longdesc", description, "--year", airDate, "--genre", genre[0], "--track", episode,
                 "--disk", season, "--hdvideo", "true", "--stik", "TV Show"])
        print("Metadata successfully set for - " + fileInfo)

        shutil.copy(fileName, iTunes)
        shutil.move(fileName, completed)
        print(fileName + " - added to iTunes.")
