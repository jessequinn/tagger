from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QHeaderView, QListWidgetItem
from PyQt5.QtCore import QDir, QThread, pyqtSlot, Qt

import sys
import ui
import os, subprocess, shutil, re
from tmdbv3api import TMDb, Movie, Genre, TV, Season
from dotenv import load_dotenv

load_dotenv()


class AppContext(ApplicationContext):
    def run(self):
        # stylesheet = self.get_resource('styles.qss')
        # self.app.setStyleSheet(open(stylesheet).read())
        self.window.show()
        return self.app.exec_()

    @cached_property
    def window(self):
        return MainWindow()


class Progress(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        pass
        # self.emit(QtCore.SIGNAL('__updateProgressBar(int)'), 0)  ## Reset progressbar value
        # file_in = "xfile"
        # loading = 0
        # with open(file_in) as f:
        #     fl_content = f.read().splitlines()
        #     total_lines = len(fl_content)
        #     for i, line in enumerate(fl_content):
        #         print
        #         line
        #         self.emit(QtCore.SIGNAL('__updateProgressBar(int)'), i * 100 / total_lines)
        #         sleep(0.1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.results = None
        self.file_name = None
        self.path = None
        self.file_w_path = []
        self.checked_episode_titles = []
        self.checked_files = []

        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # setup directories and files
        path = QDir.homePath()

        self.ui.dirModel = QFileSystemModel()
        self.ui.dirModel.setRootPath(QDir.rootPath())
        self.ui.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.ui.fileModel = QFileSystemModel()
        self.ui.fileModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.ui.treeView.setModel(self.ui.dirModel)
        self.ui.listView.setModel(self.ui.fileModel)

        self.ui.treeView.setRootIndex(self.ui.dirModel.index(path))
        self.ui.listView.setRootIndex(self.ui.fileModel.index(path))

        self.hv = self.ui.treeView.header()
        self.hv.setSectionHidden(1, 1)
        self.hv.setSectionHidden(2, 1)
        self.hv.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # by default let's set the movie tab disabled
        # self.ui.tw_shows_movies.setTabEnabled(0, False)

        self.ui.treeView.clicked.connect(self.on_treeview_click)

        self.ui.plainTextEdit.setPlainText('API Key: ' + os.getenv('API_KEY'))

        self.taggermovie = TaggerMovie(key=os.getenv('API_KEY'))
        self.taggertv = TaggerTV(key=os.getenv('API_KEY'))

        self.ui.listView.clicked.connect(self.on_listview_click)
        self.ui.cb_options.currentTextChanged.connect(self.on_combobox_changed)

        self.ui.lw_show_id_title.clicked.connect(self.on_show_id_title_click)
        self.ui.lw_episode_title.itemChanged.connect(self.on_episode_title_check)
        self.ui.lw_selected_files.itemChanged.connect(self.on_file_check)

        self.ui.pb_search.clicked.connect(self.on_search_click)
        self.ui.pb_update.clicked.connect(self.on_update_click)

    def on_episode_title_check(self, item):
        """
        Add / remove items from the lw_episode_title
        :param item:
        :return:
        """
        if item.checkState() == Qt.Checked:
            self.checked_episode_titles.append(item)
        if item.checkState() == Qt.Unchecked:
            self.checked_episode_titles.remove(item)

    def on_file_check(self, item):
        """
        Add / remove items from the lw_episode_title
        :param item:
        :return:
        """
        if item.checkState() == Qt.Checked:
            self.checked_files.append(item)
        if item.checkState() == Qt.Unchecked:
            self.checked_files.remove(item)

    def on_show_id_title_click(self, index):
        """
        Fills the episode titles listWidget.
        :param index:
        :return:
        """
        self.ui.lw_episode_title.clear()

        # need to make all items checkable
        for idx, title in enumerate(self.results[index.row()][2]):
            item = QListWidgetItem()
            item.setText('E{0} '.format(str(idx + 1).zfill(2)) + title)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            self.ui.lw_episode_title.addItem(item)

        # self.ui.lw_episode_title.addItems(self.results[index.row()][2])
        self.ui.lw_episode_overviews.addItems(self.results[index.row()][4])
        self.ui.lw_episode_air_dates.addItems(self.results[index.row()][3])

    def on_treeview_click(self, index):
        self.path = self.ui.dirModel.fileInfo(index).absoluteFilePath()

        self.ui.listView.setRootIndex(self.ui.fileModel.setRootPath(self.path))
        # self.ui.label.setText(self.ui.fileModel.fileName(self.ui.fileModel.index(index.row(), 0, index.parent())))

    def on_listview_click(self):
        self.ui.lw_selected_files.clear()
        self.checked_files = []
        # self.file_name = str(index.data())
        # self.ui.pte_title.setPlainText(str(index.data()))
        # self.ui.lw_selected_files.addItems([file.data() for file in self.ui.listView.selectedIndexes()])

        # need to make all items checkable
        for file in self.ui.listView.selectedIndexes():
            item = QListWidgetItem()
            item.setText(file.data())
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            # self.checked_files.append(item)
            self.ui.lw_selected_files.addItem(item)

    def on_search_click(self):
        self.ui.lw_show_id_title.clear()
        self.ui.lw_episode_title.clear()
        self.ui.lw_episode_air_dates.clear()
        self.ui.lw_episode_overviews.clear()
        self.ui.lw_movie_title.clear()
        self.ui.lw_movie_release_date.clear()
        self.ui.lw_movie_overview.clear()

        if self.ui.cb_options.currentText() == 'Movie':
            self.results = self.taggermovie.search_results(self.ui.pte_title.toPlainText())
            self.ui.lw_movie_title.addItems([row[0] for row in self.results])
            self.ui.lw_movie_release_date.addItems([row[1] for row in self.results])
            self.ui.lw_movie_overview.addItems([row[2] for row in self.results])
        else:
            if self.__is_number(self.ui.pte_season.toPlainText()):
                self.results = self.taggertv.search_results(
                    self.ui.pte_title.toPlainText(),
                    int(self.ui.pte_season.toPlainText())
                )
                self.ui.lw_show_id_title.addItems([row[1] + ' (' + str(row[0]) + ')' for row in self.results])

    def on_combobox_changed(self, value):
        if value == 'Movie':
            self.ui.tw_shows_movies.setCurrentIndex(0)
            self.ui.pte_season.setReadOnly(True)
            # self.ui.tw_shows_movies.setTabEnabled(1, False)
        else:
            self.ui.tw_shows_movies.setCurrentIndex(1)
            self.ui.pte_season.setReadOnly(False)
            # self.ui.tw_shows_movies.setTabEnabled(0, False)

    def on_update_click(self):
        if self.ui.cb_options.currentText() == 'TV Show':
            if len(self.checked_files) == len(self.checked_episode_titles) and self.checked_files != [] and self.checked_episode_titles != []:
                # checked_episode_titles = self.ui.lw_episode_title.selectedItems()
                checked_episodes_titles_idx = [self.ui.lw_episode_title.row(t) for t in self.checked_episode_titles]

                selected_show_id_row = self.ui.lw_show_id_title.row(self.ui.lw_show_id_title.selectedItems()[0])
                selected_show_id = self.results[selected_show_id_row]

                # for idx in range(0, checked_episodes_idx):
                for i, idx in enumerate(checked_episodes_titles_idx):
                    item = self.ui.lw_selected_files.item(i)
                    file_w_path = (self.path + '/' + item.text())

                    episode_title = selected_show_id[2][idx]
                    episode_air_date = selected_show_id[3][idx]
                    episode_overview = selected_show_id[4][idx]
                    episode_first_genre = selected_show_id[5]
                    network = selected_show_id[6]
                    show = selected_show_id[1]
                    season = '{0}'.format(str(selected_show_id[7]).zfill(2))
                    episode = '{0}'.format(str(idx + 1).zfill(2))

                    print(i, item.text(), idx+1, episode_title)

                    if os.path.isfile(file_w_path):
                        subprocess.call(
                            ["AtomicParsley", file_w_path, "--overWrite", "--TVShowName", show,
                             "--TVSeasonNum", season, "--TVEpisodeNum", episode, "--title", episode_title,
                             "--TVNetwork",
                             network, "--desc", episode_overview, "--longdesc", episode_overview,
                             "--year", episode_air_date,
                             "--genre", episode_first_genre, "--track", episode, "--disk", season, "--hdvideo",
                             "true", "--stik", "TV Show"])

                        os.rename(file_w_path,
                                  self.path + '/' + show + ' S' + season + 'E' + episode +
                                  os.path.splitext(item.text())[1].lower())

                        # self.ui.lw_selected_files.removeItemWidget(item)

        print('Completed task')
        print('Debug: ', len(self.checked_files), len(self.checked_files))

    @staticmethod
    def __is_number(s):
        """
        helper function to test if a string is numerical
        :return:
        """
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    @pyqtSlot(int)
    def __updateProgressBar(self, percent):
        self.progress.setValue(percent)

    def start(self):
        self.progressView.start()


class Tagger(object):
    def __init__(self, key, language='en'):
        self.tmdb = TMDb()
        self.tmdb.api_key = key
        self.tmdb.language = language


class TaggerMovie(Tagger):
    def __init__(self, key, language='en'):
        Tagger.__init__(self, key, language)
        self.movie = Movie()
        self.genres = Genre().movie_list()

    def __get_genres(self):
        return dict([(g.id, g.name) for g in self.genres])

    def search_results(self, title):
        return [[item.title, item.release_date.split('-')[0], item.overview] for item in self.movie.search(title)]


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


if __name__ == '__main__':
    appctxt = AppContext()  # 4. Instantiate the subclass
    exit_code = appctxt.run()  # 5. Invoke run()
    sys.exit(exit_code)
