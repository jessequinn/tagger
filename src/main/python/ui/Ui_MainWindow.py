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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 761, 31))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(761, 31))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
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
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.tw_shows_movies = QtWidgets.QTabWidget(self.centralwidget)
        self.tw_shows_movies.setEnabled(True)
        self.tw_shows_movies.setGeometry(QtCore.QRect(20, 460, 1871, 521))
        self.tw_shows_movies.setObjectName("tw_shows_movies")
        self.t_movie = QtWidgets.QWidget()
        self.t_movie.setObjectName("t_movie")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.t_movie)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1201, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lw_movie_title = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lw_movie_title.setObjectName("lw_movie_title")
        self.horizontalLayout_2.addWidget(self.lw_movie_title)
        self.lw_movie_release_date = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lw_movie_release_date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_movie_release_date.setObjectName("lw_movie_release_date")
        self.horizontalLayout_2.addWidget(self.lw_movie_release_date)
        self.lw_movie_overview = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lw_movie_overview.setObjectName("lw_movie_overview")
        self.horizontalLayout_2.addWidget(self.lw_movie_overview)
        self.tw_shows_movies.addTab(self.t_movie, "")
        self.t_tvshow = QtWidgets.QWidget()
        self.t_tvshow.setObjectName("t_tvshow")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.t_tvshow)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 1841, 461))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lw_show_id_title = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.lw_show_id_title.setMinimumSize(QtCore.QSize(300, 0))
        self.lw_show_id_title.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lw_show_id_title.setObjectName("lw_show_id_title")
        self.horizontalLayout_4.addWidget(self.lw_show_id_title)
        self.lw_episode_title = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.lw_episode_title.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.lw_episode_title.setObjectName("lw_episode_title")
        self.horizontalLayout_4.addWidget(self.lw_episode_title)
        self.lw_selected_files = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.lw_selected_files.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lw_selected_files.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lw_selected_files.setObjectName("lw_selected_files")
        self.horizontalLayout_4.addWidget(self.lw_selected_files)
        self.lw_episode_overviews = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.lw_episode_overviews.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.lw_episode_overviews.setObjectName("lw_episode_overviews")
        self.horizontalLayout_4.addWidget(self.lw_episode_overviews)
        self.lw_episode_air_dates = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.lw_episode_air_dates.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lw_episode_air_dates.setObjectName("lw_episode_air_dates")
        self.horizontalLayout_4.addWidget(self.lw_episode_air_dates)
        self.tw_shows_movies.addTab(self.t_tvshow, "")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 380, 1406, 74))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pte_title = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_3)
        self.pte_title.setMinimumSize(QtCore.QSize(700, 31))
        self.pte_title.setMaximumSize(QtCore.QSize(700, 31))
        self.pte_title.setAutoFillBackground(False)
        self.pte_title.setTabChangesFocus(True)
        self.pte_title.setObjectName("pte_title")
        self.horizontalLayout_3.addWidget(self.pte_title)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pte_season = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_3)
        self.pte_season.setMinimumSize(QtCore.QSize(300, 31))
        self.pte_season.setMaximumSize(QtCore.QSize(300, 31))
        self.pte_season.setToolTip("")
        self.pte_season.setToolTipDuration(2)
        self.pte_season.setTabChangesFocus(True)
        self.pte_season.setOverwriteMode(False)
        self.pte_season.setObjectName("pte_season")
        self.horizontalLayout_5.addWidget(self.pte_season)
        self.cb_options = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.cb_options.setMaximumSize(QtCore.QSize(100, 31))
        self.cb_options.setObjectName("cb_options")
        self.cb_options.addItem("")
        self.cb_options.addItem("")
        self.horizontalLayout_5.addWidget(self.cb_options)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1800, 380, 92, 72))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_search = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_search.setObjectName("pb_search")
        self.verticalLayout.addWidget(self.pb_search)
        self.pb_update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_update.setObjectName("pb_update")
        self.verticalLayout.addWidget(self.pb_update)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tw_shows_movies.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tagger"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "API KEY here"))
        self.tw_shows_movies.setTabText(self.tw_shows_movies.indexOf(self.t_movie), _translate("MainWindow", "Movie"))
        self.tw_shows_movies.setTabText(self.tw_shows_movies.indexOf(self.t_tvshow), _translate("MainWindow", "Shows"))
        self.pte_title.setPlainText(_translate("MainWindow", "Game of thrones"))
        self.pte_season.setPlainText(_translate("MainWindow", "1"))
        self.cb_options.setItemText(0, _translate("MainWindow", "TV Show"))
        self.cb_options.setItemText(1, _translate("MainWindow", "Movie"))
        self.pb_search.setText(_translate("MainWindow", "Search"))
        self.pb_update.setText(_translate("MainWindow", "Update"))


