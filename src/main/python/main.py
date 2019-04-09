from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QHeaderView, QListWidgetItem, QDialog
from PyQt5.QtCore import QDir, Qt

import sys
import os
import ui
from tagger import TaggerTV, TaggerMovie

import subprocess
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


# API Dialog Class
# TODO: refactor
class Dialog(QDialog, ui.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.btn_bx_api_key.accepted.connect(self.save_api_key)
        self.btn_bx_api_key.rejected.connect(self.rejected)

    def save_api_key(self, f='.api_key'):
        try:
            with open(f, 'w') as the_file:
                the_file.write('{0}'.format(self.pte_api_key.text()))
        except EnvironmentError:
            # TODO: new error message
            print('error with file write')
            self.rejected()
        self.accept()


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

        self.le_api_key.setText('API Key: ' + os.getenv('API_KEY'))

        self.taggermovie = TaggerMovie(key=os.getenv('API_KEY'))
        self.taggertv = TaggerTV(key=os.getenv('API_KEY'))

        self.listView.clicked.connect(self.on_listview_click)
        self.cb_options.currentTextChanged.connect(self.on_combobox_changed)

        self.lw_show_title.clicked.connect(self.on_show_title_click)
        self.lw_episode_title.itemChanged.connect(self.on_episode_title_check)
        self.lw_movie_title.itemChanged.connect(self.on_movie_title_check)
        self.lw_selected_files.itemChanged.connect(self.on_file_check)

        self.pb_search.clicked.connect(self.on_search_click)
        self.pb_update.clicked.connect(self.on_update_click)

        self.ckbx_select_all.stateChanged.connect(self.on_select_all_check)

        # menu
        # q
        self.a_quit.triggered.connect(self.close)
        # api key
        self.a_api_key.triggered.connect(self.on_click_api_key)

    def on_click_api_key(self):
        api_key_dialog = Dialog()
        api_key_dialog.exec_()

        # save_api_key(api_key_dialog.)

    def on_select_all_check(self, state):
        """
        Select all lw_selected_files or unselect all
        :param state:
        :return:
        """
        if state == Qt.Checked:
            # get all QListWidgetItems
            print(self.lw_selected_files.count())
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

        # self.lw_episode_title.addItems(self.results[index.row()][2])
        self.lw_episode_overviews.addItems(self.results[index.row()][4])
        self.lw_episode_air_dates.addItems(self.results[index.row()][3])

    def on_treeview_click(self, index):
        self.path = self.dirModel.fileInfo(index).absoluteFilePath()

        self.listView.setRootIndex(self.fileModel.setRootPath(self.path))
        # self.label.setText(self.fileModel.fileName(self.fileModel.index(index.row(), 0, index.parent())))

    def on_listview_click(self):
        self.lw_selected_files.clear()
        self.checked_files = []
        # self.checked_movie_titles = []
        # self.checked_episode_titles = []
        self.ckbx_select_all.setCheckState(Qt.Unchecked)
        # self.file_name = str(index.data())
        # self.le_title.setPlainText(str(index.data()))
        # self.lw_selected_files.addItems([file.data() for file in self.listView.selectedIndexes()])

        # need to make all items checkable
        for file in self.listView.selectedIndexes():
            item = QListWidgetItem()
            item.setText(file.data())
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            # self.checked_files.append(item)
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
        self.lw_movie_first_genre.clear()

        if self.cb_options.currentText() == 'Movie':
            self.results = self.taggermovie.search_results(self.le_title.text())
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
            self.lw_movie_first_genre.addItems([row[4] for row in self.results])
        else:
            if self.__is_number(self.le_season.text()):
                self.results = self.taggertv.search_results(
                    self.le_title.text(),
                    int(self.le_season.text())
                )
                self.lw_show_id.addItems([str(row[0]) for row in self.results])
                self.lw_show_title.addItems([row[1] for row in self.results])

    def on_combobox_changed(self, value):
        if value == 'Movie':
            self.tw_shows_movies.setCurrentIndex(0)
            self.le_season.setDisabled(True)
            # self.tw_shows_movies.setTabEnabled(1, False)
        else:
            self.tw_shows_movies.setCurrentIndex(1)
            self.le_season.setDisabled(False)
            # self.tw_shows_movies.setTabEnabled(0, False)

    def on_update_click(self):
        print(len(self.checked_files), len(self.checked_episode_titles))
        if self.cb_options.currentText() == 'TV Show':
            if len(self.checked_files) == len(
                    self.checked_episode_titles) and self.checked_files != [] and self.checked_episode_titles != []:
                # checked_episode_titles = self.lw_episode_title.selectedItems()
                checked_episodes_titles_idx = [self.lw_episode_title.row(t) for t in self.checked_episode_titles]

                selected_show_id_row = self.lw_show_title.row(self.lw_show_title.selectedItems()[0])
                selected_show_id = self.results[selected_show_id_row]

                # for idx in range(0, checked_episodes_idx):
                for i, idx in enumerate(checked_episodes_titles_idx):
                    item = self.lw_selected_files.item(i)
                    file_w_path = (self.path + '/' + item.text())

                    episode_title = selected_show_id[2][idx]
                    episode_air_date = selected_show_id[3][idx]
                    episode_overview = selected_show_id[4][idx]
                    episode_first_genre = selected_show_id[5]
                    network = selected_show_id[6]
                    show = selected_show_id[1]
                    season = '{0}'.format(str(selected_show_id[7]).zfill(2))
                    episode = '{0}'.format(str(idx + 1).zfill(2))

                    print(i, item.text(), idx + 1, episode_title)

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

                        # self.lw_selected_files.removeItemWidget(item)
        else:
            if len(self.checked_files) == len(
                    self.checked_movie_titles) and self.checked_files != [] and self.checked_movie_titles != []:
                checked_movie_title_row = [self.lw_movie_title.row(t) for t in self.checked_movie_titles]

                for i, idx in enumerate(checked_movie_title_row):
                    selected_movie_id = self.results[idx]

                    item = self.lw_selected_files.item(i)
                    file_w_path = (self.path + '/' + item.text())

                    movie_title = selected_movie_id[1].replace(':', ' - ')
                    movie_release_date = selected_movie_id[2]
                    movie_overview = selected_movie_id[3]
                    movie_first_genre = selected_movie_id[4]

                    print(movie_title)
                    if os.path.isfile(file_w_path):
                        subprocess.call(
                            ["AtomicParsley", file_w_path, "--overWrite", "--title", movie_title, "--desc",
                             movie_overview,
                             "--longdesc", movie_overview, "--year", movie_release_date, "--genre", movie_first_genre,
                             "--hdvideo", "true", "--stik", "Movie"])

                        if self.rb_3d.isChecked():
                            os.rename(file_w_path,
                                      self.path + '/' + movie_title + ' ' + movie_release_date + ' - 3D' +
                                      os.path.splitext(item.text())[1].lower())
                        else:
                            os.rename(file_w_path,
                                      self.path + '/' + movie_title + ' ' + movie_release_date +
                                      os.path.splitext(item.text())[1].lower())

        print('Completed task')

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