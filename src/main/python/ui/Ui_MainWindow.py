# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 1871, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.horizontalLayoutWidget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.listView = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView.setMaximumSize(QtCore.QSize(600, 900))
        self.listView.setDragEnabled(False)
        self.listView.setDragDropOverwriteMode(False)
        self.listView.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.tw_shows_movies = QtWidgets.QTabWidget(self.centralwidget)
        self.tw_shows_movies.setEnabled(True)
        self.tw_shows_movies.setGeometry(QtCore.QRect(20, 430, 1311, 601))
        self.tw_shows_movies.setObjectName("tw_shows_movies")
        self.t_movie = QtWidgets.QWidget()
        self.t_movie.setObjectName("t_movie")
        self.gridLayoutWidget = QtWidgets.QWidget(self.t_movie)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1271, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lw_movie_release_date = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.lw_movie_release_date.setMinimumSize(QtCore.QSize(100, 0))
        self.lw_movie_release_date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_movie_release_date.setProperty("showDropIndicator", False)
        self.lw_movie_release_date.setObjectName("lw_movie_release_date")
        self.gridLayout_2.addWidget(self.lw_movie_release_date, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(100, 31))
        self.label_9.setMaximumSize(QtCore.QSize(100, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(100, 31))
        self.label_12.setMaximumSize(QtCore.QSize(100, 31))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 7, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(0, 31))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 31))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 3, 1, 1)
        self.lw_movie_id = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.lw_movie_id.setMinimumSize(QtCore.QSize(100, 0))
        self.lw_movie_id.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_movie_id.setObjectName("lw_movie_id")
        self.gridLayout_2.addWidget(self.lw_movie_id, 1, 0, 1, 1)
        self.lw_movie_overview = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.lw_movie_overview.setMinimumSize(QtCore.QSize(0, 0))
        self.lw_movie_overview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lw_movie_overview.setObjectName("lw_movie_overview")
        self.gridLayout_2.addWidget(self.lw_movie_overview, 1, 3, 1, 1)
        self.lw_movie_genres = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.lw_movie_genres.setMinimumSize(QtCore.QSize(100, 0))
        self.lw_movie_genres.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_movie_genres.setObjectName("lw_movie_genres")
        self.gridLayout_2.addWidget(self.lw_movie_genres, 1, 7, 1, 1)
        self.lw_movie_title = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.lw_movie_title.setMinimumSize(QtCore.QSize(500, 0))
        self.lw_movie_title.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lw_movie_title.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.lw_movie_title.setObjectName("lw_movie_title")
        self.gridLayout_2.addWidget(self.lw_movie_title, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(500, 31))
        self.label_8.setMaximumSize(QtCore.QSize(500, 31))
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(100, 31))
        self.label_11.setMaximumSize(QtCore.QSize(100, 31))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.tw_shows_movies.addTab(self.t_movie, "")
        self.t_tvshow = QtWidgets.QWidget()
        self.t_tvshow.setObjectName("t_tvshow")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.t_tvshow)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 1281, 541))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lw_show_title = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.lw_show_title.setMinimumSize(QtCore.QSize(300, 0))
        self.lw_show_title.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lw_show_title.setObjectName("lw_show_title")
        self.gridLayout_4.addWidget(self.lw_show_title, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setMaximumSize(QtCore.QSize(100, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 31))
        self.label_3.setMaximumSize(QtCore.QSize(300, 31))
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 31))
        self.label_5.setMaximumSize(QtCore.QSize(600, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 3, 1, 1)
        self.lw_episode_overviews = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.lw_episode_overviews.setMaximumSize(QtCore.QSize(600, 16777215))
        self.lw_episode_overviews.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.lw_episode_overviews.setObjectName("lw_episode_overviews")
        self.gridLayout_4.addWidget(self.lw_episode_overviews, 1, 3, 1, 1)
        self.lw_episode_air_dates = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.lw_episode_air_dates.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_episode_air_dates.setObjectName("lw_episode_air_dates")
        self.gridLayout_4.addWidget(self.lw_episode_air_dates, 1, 7, 1, 1)
        self.lw_show_id = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.lw_show_id.setMinimumSize(QtCore.QSize(100, 0))
        self.lw_show_id.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_show_id.setObjectName("lw_show_id")
        self.gridLayout_4.addWidget(self.lw_show_id, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setMinimumSize(QtCore.QSize(0, 31))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 31))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.lw_episode_title = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.lw_episode_title.setMaximumSize(QtCore.QSize(600, 16777215))
        self.lw_episode_title.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.lw_episode_title.setObjectName("lw_episode_title")
        self.gridLayout_4.addWidget(self.lw_episode_title, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 31))
        self.label_2.setMaximumSize(QtCore.QSize(600, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)
        self.tw_shows_movies.addTab(self.t_tvshow, "")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 380, 1471, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setMinimumSize(QtCore.QSize(100, 31))
        self.label_7.setMaximumSize(QtCore.QSize(100, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.le_title = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.le_title.setMinimumSize(QtCore.QSize(0, 31))
        self.le_title.setMaximumSize(QtCore.QSize(16777215, 31))
        self.le_title.setObjectName("le_title")
        self.horizontalLayout_3.addWidget(self.le_title)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setMinimumSize(QtCore.QSize(100, 31))
        self.label_6.setMaximumSize(QtCore.QSize(100, 31))
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.le_season = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.le_season.setMinimumSize(QtCore.QSize(0, 31))
        self.le_season.setMaximumSize(QtCore.QSize(16777215, 31))
        self.le_season.setObjectName("le_season")
        self.horizontalLayout_5.addWidget(self.le_season)
        self.cb_options = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.cb_options.setMinimumSize(QtCore.QSize(0, 31))
        self.cb_options.setMaximumSize(QtCore.QSize(100, 31))
        self.cb_options.setObjectName("cb_options")
        self.cb_options.addItem("")
        self.cb_options.addItem("")
        self.horizontalLayout_5.addWidget(self.cb_options)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pb_search = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pb_search.setMinimumSize(QtCore.QSize(0, 31))
        self.pb_search.setMaximumSize(QtCore.QSize(16777215, 31))
        self.pb_search.setObjectName("pb_search")
        self.horizontalLayout_5.addWidget(self.pb_search)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.pb_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pb_clear.setMinimumSize(QtCore.QSize(0, 31))
        self.pb_clear.setMaximumSize(QtCore.QSize(16777215, 31))
        self.pb_clear.setObjectName("pb_clear")
        self.horizontalLayout_3.addWidget(self.pb_clear)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1400, 460, 471, 481))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lw_selected_files = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.lw_selected_files.setMaximumSize(QtCore.QSize(600, 16777215))
        self.lw_selected_files.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lw_selected_files.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lw_selected_files.setObjectName("lw_selected_files")
        self.gridLayout_3.addWidget(self.lw_selected_files, 2, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ckbx_select_all = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.ckbx_select_all.setMinimumSize(QtCore.QSize(0, 31))
        self.ckbx_select_all.setMaximumSize(QtCore.QSize(16777215, 31))
        self.ckbx_select_all.setObjectName("ckbx_select_all")
        self.gridLayout_6.addWidget(self.ckbx_select_all, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 31))
        self.label_4.setMaximumSize(QtCore.QSize(600, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 1, 1, 1)
        self.rb_3d = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.rb_3d.setMinimumSize(QtCore.QSize(60, 31))
        self.rb_3d.setMaximumSize(QtCore.QSize(60, 31))
        self.rb_3d.setObjectName("rb_3d")
        self.gridLayout_6.addWidget(self.rb_3d, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 2, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.prgbar_update = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.prgbar_update.setMinimumSize(QtCore.QSize(0, 31))
        self.prgbar_update.setMaximumSize(QtCore.QSize(16777215, 31))
        self.prgbar_update.setProperty("value", 0)
        self.prgbar_update.setObjectName("prgbar_update")
        self.gridLayout_5.addWidget(self.prgbar_update, 0, 0, 1, 1)
        self.pb_update = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_update.setMinimumSize(QtCore.QSize(0, 31))
        self.pb_update.setMaximumSize(QtCore.QSize(16777215, 31))
        self.pb_update.setObjectName("pb_update")
        self.gridLayout_5.addWidget(self.pb_update, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 2, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 1871, 33))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.l_connection = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.l_connection.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_connection.setObjectName("l_connection")
        self.gridLayout.addWidget(self.l_connection, 0, 2, 1, 1)
        self.hs_connection = QtWidgets.QSlider(self.gridLayoutWidget_4)
        self.hs_connection.setMinimumSize(QtCore.QSize(50, 31))
        self.hs_connection.setMaximumSize(QtCore.QSize(50, 31))
        self.hs_connection.setMaximum(1)
        self.hs_connection.setOrientation(QtCore.Qt.Horizontal)
        self.hs_connection.setObjectName("hs_connection")
        self.gridLayout.addWidget(self.hs_connection, 0, 3, 1, 1)
        self.le_api_key = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.le_api_key.setMinimumSize(QtCore.QSize(400, 31))
        self.le_api_key.setMaximumSize(QtCore.QSize(400, 31))
        self.le_api_key.setObjectName("le_api_key")
        self.gridLayout.addWidget(self.le_api_key, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setMinimumSize(QtCore.QSize(50, 31))
        self.label_14.setMaximumSize(QtCore.QSize(50, 31))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 28))
        self.menubar.setObjectName("menubar")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.a_api_key = QtWidgets.QAction(MainWindow)
        self.a_api_key.setObjectName("a_api_key")
        self.a_quit = QtWidgets.QAction(MainWindow)
        self.a_quit.setObjectName("a_quit")
        self.a_connect_tmdb = QtWidgets.QAction(MainWindow)
        self.a_connect_tmdb.setObjectName("a_connect_tmdb")
        self.menuTool.addAction(self.a_api_key)
        self.menuTool.addAction(self.a_connect_tmdb)
        self.menuFile.addAction(self.a_quit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())

        self.retranslateUi(MainWindow)
        self.tw_shows_movies.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tagger"))
        self.label_9.setText(_translate("MainWindow", "Release Date"))
        self.label_12.setText(_translate("MainWindow", "Genres"))
        self.label_10.setText(_translate("MainWindow", "Overviews"))
        self.label_8.setText(_translate("MainWindow", "Film"))
        self.label_11.setText(_translate("MainWindow", "ID"))
        self.tw_shows_movies.setTabText(self.tw_shows_movies.indexOf(self.t_movie), _translate("MainWindow", "Film"))
        self.label.setText(_translate("MainWindow", "Airing Dates"))
        self.label_3.setText(_translate("MainWindow", "Show"))
        self.label_5.setText(_translate("MainWindow", "Episode Overviews"))
        self.label_13.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Episode Number and Title"))
        self.tw_shows_movies.setTabText(self.tw_shows_movies.indexOf(self.t_tvshow), _translate("MainWindow", "Show"))
        self.label_7.setText(_translate("MainWindow", "Show"))
        self.le_title.setText(_translate("MainWindow", "Game of thrones"))
        self.label_6.setText(_translate("MainWindow", "Season"))
        self.le_season.setText(_translate("MainWindow", "1"))
        self.cb_options.setCurrentText(_translate("MainWindow", "Show"))
        self.cb_options.setItemText(0, _translate("MainWindow", "Show"))
        self.cb_options.setItemText(1, _translate("MainWindow", "Film"))
        self.pb_search.setText(_translate("MainWindow", "Search"))
        self.pb_clear.setText(_translate("MainWindow", "Clear"))
        self.ckbx_select_all.setText(_translate("MainWindow", "Select All"))
        self.label_4.setText(_translate("MainWindow", "Selected Files"))
        self.rb_3d.setText(_translate("MainWindow", "3D"))
        self.pb_update.setText(_translate("MainWindow", "Update"))
        self.l_connection.setText(_translate("MainWindow", "Disconnected"))
        self.label_14.setText(_translate("MainWindow", "API Key"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.a_api_key.setText(_translate("MainWindow", "API KEY"))
        self.a_api_key.setShortcut(_translate("MainWindow", "Alt+K"))
        self.a_quit.setText(_translate("MainWindow", "Quit"))
        self.a_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.a_connect_tmdb.setText(_translate("MainWindow", "Connect to TMDB"))
        self.a_connect_tmdb.setShortcut(_translate("MainWindow", "Alt+C"))


