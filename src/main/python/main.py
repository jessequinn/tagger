from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QHeaderView, QListWidgetItem
from PyQt5.QtCore import QDir, Qt

import sys
import re
import os
import src.main.python.ui as ui
from src.main.python.dialogs import Dialog
from src.main.python.tagging import FilmMetaTag, ShowMetaTag
from src.main.python.search import TV, Movie

import subprocess

API_KEY = os.path.join(os.path.dirname(__file__), '.api_key')


class AppContext(ApplicationContext):
    def run(self):
        # stylesheet = self.get_resource('styles.qss')
        # self.app.setStyleSheet(open(stylesheet).read())
        self.window.show()
        return self.app.exec_()

    @cached_property
    def window(self):
        return MainWindow()


# MainWindow Class
class MainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # default values
        self.results = None
        self.file_name = None
        self.path = None
        self.file_w_path = []
        self.checked_episode_titles = []
        self.checked_movie_titles = []
        self.checked_files = []

        # setup directories and files
        path = QDir.homePath()

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        self.fileModel.setNameFilters(['*.m4v', '*mp4'])

        self.treeView.setModel(self.dirModel)
        self.listView.setModel(self.fileModel)

        self.treeView.setRootIndex(self.dirModel.index(path))
        self.listView.setRootIndex(self.fileModel.index(path))

        self.hv = self.treeView.header()
        self.hv.setSectionHidden(1, 1)
        self.hv.setSectionHidden(2, 1)
        self.hv.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # by default let's set the movie tab disabled
        # self.tw_shows_movies.setTabEnabled(0, False)

        self.treeView.clicked.connect(self.on_treeview_click)

        # self.le_api_key.setText('API Key: ' + os.getenv('API_KEY'))

        self.listView.clicked.connect(self.on_listview_click)
        self.cb_options.currentTextChanged.connect(self.on_combobox_changed)

        self.lw_show_title.clicked.connect(self.on_show_title_click)
        self.lw_episode_title.itemChanged.connect(self.on_episode_title_check)
        self.lw_movie_title.itemChanged.connect(self.on_movie_title_check)
        self.lw_selected_files.itemChanged.connect(self.on_file_check)

        self.pb_search.clicked.connect(self.on_search_click)
        self.pb_update.clicked.connect(self.on_update_click)

        self.ckbx_select_all.stateChanged.connect(self.on_select_all_check)
        self.hs_connection.valueChanged.connect(self.on_slide_connect_tmdb)

        self.pb_clear.clicked.connect(self.on_pb_clear_click)
        self.pb_connect.clicked.connect(self.on_click_connect_tmdb)

        self.tw_shows_movies.setCurrentIndex(1)

        # menu
        # q
        self.a_quit.triggered.connect(self.close)
        # api key
        self.a_api_key.triggered.connect(self.on_click_api_key)
        # self.a_connect_tmdb.triggered.connect(self.on_click_connect_tmdb)

    def on_pb_clear_click(self):
        self.le_title.clear()
        self.le_season.clear()

    def on_click_api_key(self):
        api_key_dialog = Dialog()
        api_key_dialog.exec_()

        self.api_key_file = open(API_KEY)
        self.le_api_key.setText(self.api_key_file.read())
        self.api_key_file.close()

    def on_click_connect_tmdb(self):
        self.tv = TV(api_key=self.le_api_key.text())
        self.movie = Movie(api_key=self.le_api_key.text())
        self.hs_connection.setValue(1)
        self.l_connection.setText('Connected')

    def on_slide_connect_tmdb(self):
        if self.hs_connection.value() == 1 and self.le_api_key.text() != '':
            self.tv = TV(api_key=self.le_api_key.text())
            self.movie = Movie(api_key=self.le_api_key.text())
            self.l_connection.setText('Connected')
        else:
            self.l_connection.setText('Disconnected')

    def on_select_all_check(self, state):
        """
        Select all lw_selected_files or unselect all
        :param state:
        :return:
        """
        if state == Qt.Checked:
            # get all QListWidgetItems
            for idx in range(0, self.lw_selected_files.count()):
                item = self.lw_selected_files.item(idx)
                item.setCheckState(Qt.Checked)
        else:
            for idx in range(0, self.lw_selected_files.count()):
                item = self.lw_selected_files.item(idx)
                item.setCheckState(Qt.Unchecked)

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

    def on_movie_title_check(self, item):
        """
        Add / remove items from the lw_movie_title
        :param item:
        :return:
        """
        if item.checkState() == Qt.Checked:
            self.checked_movie_titles.append(item)
        if item.checkState() == Qt.Unchecked:
            self.checked_movie_titles.remove(item)

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

    def on_show_title_click(self, index):
        """
        Fills the episode titles listWidget.
        :param index:
        :return:
        """
        self.lw_episode_title.clear()
        self.lw_episode_overviews.clear()
        self.lw_episode_air_dates.clear()

        # need to make all items checkable
        for idx, title in enumerate(self.results[index.row()][2]):
            item = QListWidgetItem()
            item.setText('E{0} '.format(str(idx + 1).zfill(2)) + title)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            self.lw_episode_title.addItem(item)

        self.lw_episode_overviews.addItems(self.results[index.row()][4])
        self.lw_episode_air_dates.addItems(self.results[index.row()][3])

    def on_treeview_click(self, index):
        self.path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listView.setRootIndex(self.fileModel.setRootPath(self.path))

    def on_listview_click(self):
        self.lw_selected_files.clear()
        self.checked_files = []
        self.ckbx_select_all.setCheckState(Qt.Unchecked)
        # need to make all items checkable
        for file in self.listView.selectedIndexes():
            item = QListWidgetItem()
            item.setText(file.data())
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            self.lw_selected_files.addItem(item)

    def on_search_click(self):
        self.checked_episode_titles = []
        self.checked_movie_titles = []
        self.lw_show_id.clear()
        self.lw_show_title.clear()
        self.lw_episode_title.clear()
        self.lw_episode_air_dates.clear()
        self.lw_episode_overviews.clear()
        self.lw_movie_id.clear()
        self.lw_movie_title.clear()
        self.lw_movie_release_date.clear()
        self.lw_movie_overview.clear()
        self.lw_movie_genres.clear()

        if self.cb_options.currentText() == 'Film':
            # set properties
            self.movie.query = self.le_title.text()

            # search above properties
            self.results = self.movie.search_movie()

            # fill list widgets
            self.lw_movie_id.addItems([str(row[0]) for row in self.results])

            # populate lw_movie_title with check boxes
            for title in [row[1] for row in self.results]:
                item = QListWidgetItem()
                item.setText(title)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setCheckState(Qt.Unchecked)
                self.lw_movie_title.addItem(item)
            self.lw_movie_release_date.addItems([row[2] for row in self.results])
            self.lw_movie_overview.addItems([row[3] for row in self.results])
            self.lw_movie_genres.addItems([re.sub("\'", '', str(row[4]).strip('[]')) for row in self.results])
        else:
            if self.__is_number(self.le_season.text()):
                # set properties
                self.tv.query = self.le_title.text()
                self.tv.season = int(self.le_season.text())

                # search above properties
                self.results = self.tv.search_tv_show()

                # fill list widgets
                self.lw_show_id.addItems([str(row[0]) for row in self.results])
                self.lw_show_title.addItems([row[1] for row in self.results])

    def on_combobox_changed(self, value):
        if value == 'Film':
            self.tw_shows_movies.setCurrentIndex(0)
            self.le_season.setDisabled(True)
        else:
            self.tw_shows_movies.setCurrentIndex(1)
            self.le_season.setDisabled(False)

    def on_update_click(self):
        if self.cb_options.currentText() == 'Show':
            if len(self.checked_files) == len(
                    self.checked_episode_titles) and self.checked_files != [] and self.checked_episode_titles != []:
                self.prgbar_update.setMaximum(len(self.checked_files))
                checked_episodes_titles_idx = [self.lw_episode_title.row(t) for t in self.checked_episode_titles]

                selected_show_id_row = self.lw_show_title.row(self.lw_show_title.selectedItems()[0])
                selected_show_id = self.results[selected_show_id_row]

                for i, idx in enumerate(checked_episodes_titles_idx):
                    item = self.lw_selected_files.item(i)
                    file_w_path = (self.path + '/' + item.text())

                    episode_title = selected_show_id[2][idx]
                    episode_air_date = selected_show_id[3][idx]
                    episode_overview = selected_show_id[4][idx]
                    episode_first_genre = selected_show_id[5][0]
                    network = selected_show_id[6][0]
                    show = selected_show_id[1]
                    season = '{0}'.format(str(selected_show_id[7]).zfill(2))
                    episode = '{0}'.format(str(idx + 1).zfill(2))

                    if os.path.isfile(file_w_path):
                        # TODO: no need for ldes/desc
                        # setup instance of ShowMetaTag
                        s = ShowMetaTag(file=file_w_path)

                        # delete tags
                        s.delete_meta_tags()

                        # set properties
                        s.set_episode_title(episode_title)
                        s.set_genre(episode_first_genre)
                        s.set_date(episode_air_date)
                        s.set_description(episode_overview)
                        s.set_network(network)
                        s.set_show_title(show)
                        s.set_episode(int(episode))
                        s.set_season(int(season))

                        # save tags
                        s.save_meta_tags()

                        os.rename(file_w_path,
                                  self.path + '/' + show + ' S' + season + 'E' + episode +
                                  os.path.splitext(item.text())[1].lower())

                        self.prgbar_update.setValue(i + 1)
        else:
            if len(self.checked_files) == len(
                    self.checked_movie_titles) and self.checked_files != [] and self.checked_movie_titles != []:
                self.prgbar_update.setMaximum(len(self.checked_files))
                checked_movie_title_row = [self.lw_movie_title.row(t) for t in self.checked_movie_titles]

                for i, idx in enumerate(checked_movie_title_row):
                    selected_movie_id = self.results[idx]

                    item = self.lw_selected_files.item(i)
                    file_w_path = (self.path + '/' + item.text())

                    movie_title = selected_movie_id[1].replace(':', ' - ')
                    movie_release_date = selected_movie_id[2]
                    movie_overview = selected_movie_id[3]
                    movie_first_genre = selected_movie_id[4][0]

                    if os.path.isfile(file_w_path):
                        # TODO: no need for ldes/desc
                        # setup instance of FilmMetaTag
                        f = FilmMetaTag(file=file_w_path)

                        # delete tags
                        f.delete_meta_tags()

                        # set properties
                        f.set_title(movie_title)
                        f.set_description(movie_overview)
                        f.set_date(movie_release_date)
                        f.set_genre(movie_first_genre)

                        # save tags
                        f.save_meta_tags()

                        if self.rb_3d.isChecked():
                            os.rename(file_w_path,
                                      self.path + '/' + movie_title + ' ' + movie_release_date + ' - 3D' +
                                      os.path.splitext(item.text())[1].lower())
                        else:
                            os.rename(file_w_path,
                                      self.path + '/' + movie_title + ' ' + movie_release_date[:4] +
                                      os.path.splitext(item.text())[1].lower())
                        self.prgbar_update.setValue(i + 1)

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


if __name__ == '__main__':
    appctxt = AppContext()  # 4. Instantiate the subclass
    exit_code = appctxt.run()  # 5. Invoke run()
    sys.exit(exit_code)
