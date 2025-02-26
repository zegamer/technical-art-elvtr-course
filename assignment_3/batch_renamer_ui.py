# Form implementation generated from reading ui file 'batch_renamer.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 591)
        self.central_widget = QtWidgets.QWidget(parent=MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.option_group = QtWidgets.QGroupBox(parent=self.central_widget)
        self.option_group.setGeometry(QtCore.QRect(10, 10, 671, 141))
        self.option_group.setObjectName("option_group")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.option_group)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 651, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.options_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.options_layout.setContentsMargins(0, 0, 0, 0)
        self.options_layout.setObjectName("options_layout")
        self.line_1_layout = QtWidgets.QHBoxLayout()
        self.line_1_layout.setObjectName("line_1_layout")
        self.file_path_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.file_path_label.setObjectName("file_path_label")
        self.line_1_layout.addWidget(self.file_path_label)
        self.file_path_line_edit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.file_path_line_edit.setObjectName("file_path_line_edit")
        self.line_1_layout.addWidget(self.file_path_line_edit)
        self.browse_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.browse_button.setObjectName("browse_button")
        self.line_1_layout.addWidget(self.browse_button)
        self.options_layout.addLayout(self.line_1_layout)
        self.line_2_layout = QtWidgets.QHBoxLayout()
        self.line_2_layout.setObjectName("line_2_layout")
        self.mode_layout = QtWidgets.QHBoxLayout()
        self.mode_layout.setObjectName("mode_layout")
        self.mode_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.mode_label.setObjectName("mode_label")
        self.mode_layout.addWidget(self.mode_label)
        self.mode_radio_button = QtWidgets.QHBoxLayout()
        self.mode_radio_button.setObjectName("mode_radio_button")
        self.rename_radio_button = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.rename_radio_button.setChecked(True)
        self.rename_radio_button.setObjectName("rename_radio_button")
        self.mode_radio_button.addWidget(self.rename_radio_button)
        self.copy_radio_button = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.copy_radio_button.setObjectName("copy_radio_button")
        self.mode_radio_button.addWidget(self.copy_radio_button)
        self.mode_layout.addLayout(self.mode_radio_button)
        self.line_2_layout.addLayout(self.mode_layout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.line_2_layout.addItem(spacerItem)
        self.prefix_layout = QtWidgets.QHBoxLayout()
        self.prefix_layout.setObjectName("prefix_layout")
        self.prefix_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.prefix_label.setObjectName("prefix_label")
        self.prefix_layout.addWidget(self.prefix_label)
        self.prefix_line_edit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.prefix_line_edit.setObjectName("prefix_line_edit")
        self.prefix_layout.addWidget(self.prefix_line_edit)
        self.line_2_layout.addLayout(self.prefix_layout)
        self.suffix_layout = QtWidgets.QHBoxLayout()
        self.suffix_layout.setObjectName("suffix_layout")
        self.suffix_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.suffix_label.setObjectName("suffix_label")
        self.suffix_layout.addWidget(self.suffix_label)
        self.suffix_line_edit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.suffix_line_edit.setObjectName("suffix_line_edit")
        self.suffix_layout.addWidget(self.suffix_line_edit)
        self.line_2_layout.addLayout(self.suffix_layout)
        self.options_layout.addLayout(self.line_2_layout)
        self.line_3_layout = QtWidgets.QHBoxLayout()
        self.line_3_layout.setObjectName("line_3_layout")
        self.string_to_find_layout = QtWidgets.QHBoxLayout()
        self.string_to_find_layout.setObjectName("string_to_find_layout")
        self.string_to_find_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.string_to_find_label.setObjectName("string_to_find_label")
        self.string_to_find_layout.addWidget(self.string_to_find_label)
        self.string_to_find_line_edit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.string_to_find_line_edit.setObjectName("string_to_find_line_edit")
        self.string_to_find_layout.addWidget(self.string_to_find_line_edit)
        self.line_3_layout.addLayout(self.string_to_find_layout)
        self.string_to_replace_layout = QtWidgets.QHBoxLayout()
        self.string_to_replace_layout.setObjectName("string_to_replace_layout")
        self.string_to_replace_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.string_to_replace_label.setObjectName("string_to_replace_label")
        self.string_to_replace_layout.addWidget(self.string_to_replace_label)
        self.string_to_replace_line_edit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.string_to_replace_line_edit.setObjectName("string_to_replace_line_edit")
        self.string_to_replace_layout.addWidget(self.string_to_replace_line_edit)
        self.line_3_layout.addLayout(self.string_to_replace_layout)
        self.extension_layout = QtWidgets.QHBoxLayout()
        self.extension_layout.setObjectName("extension_layout")
        self.extension_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.extension_label.setObjectName("extension_label")
        self.extension_layout.addWidget(self.extension_label)
        self.extension_drop_down = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.extension_drop_down.setObjectName("extension_drop_down")
        self.extension_drop_down.addItem("")
        self.extension_layout.addWidget(self.extension_drop_down)
        self.line_3_layout.addLayout(self.extension_layout)
        self.options_layout.addLayout(self.line_3_layout)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(parent=self.central_widget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 510, 671, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.button_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setObjectName("button_layout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.button_layout.addItem(spacerItem1)
        self.run_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_8)
        self.run_button.setObjectName("run_button")
        self.button_layout.addWidget(self.run_button)
        self.reset_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_8)
        self.reset_button.setObjectName("reset_button")
        self.button_layout.addWidget(self.reset_button)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(parent=self.central_widget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 160, 671, 341))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.file_view_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.file_view_layout.setContentsMargins(0, 0, 0, 0)
        self.file_view_layout.setObjectName("file_view_layout")
        self.file_view_list_widget = QtWidgets.QListWidget(parent=self.horizontalLayoutWidget_9)
        self.file_view_list_widget.setAcceptDrops(True)
        self.file_view_list_widget.setObjectName("file_view_list_widget")
        self.file_view_layout.addWidget(self.file_view_list_widget)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file_path_label.setBuddy(self.file_path_line_edit)
        self.prefix_label.setBuddy(self.prefix_line_edit)
        self.suffix_label.setBuddy(self.suffix_line_edit)
        self.string_to_find_label.setBuddy(self.string_to_find_line_edit)
        self.string_to_replace_label.setBuddy(self.string_to_replace_line_edit)
        self.extension_label.setBuddy(self.extension_drop_down)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File renamer"))
        self.option_group.setTitle(_translate("MainWindow", "Options"))
        self.file_path_label.setText(_translate("MainWindow", "Folder Path"))
        self.file_path_line_edit.setToolTip(_translate("MainWindow", "File path of the file you want to rename"))
        self.browse_button.setToolTip(_translate("MainWindow", "Browse the file"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.mode_label.setText(_translate("MainWindow", "Mode"))
        self.rename_radio_button.setToolTip(_translate("MainWindow", "Replace the files with the new name"))
        self.rename_radio_button.setText(_translate("MainWindow", "Rename"))
        self.copy_radio_button.setToolTip(_translate("MainWindow", "Copy the files with the new name"))
        self.copy_radio_button.setText(_translate("MainWindow", "Copy"))
        self.prefix_label.setText(_translate("MainWindow", "Prefix"))
        self.prefix_line_edit.setToolTip(_translate("MainWindow", "Prefix for file name"))
        self.suffix_label.setText(_translate("MainWindow", "Suffix"))
        self.suffix_line_edit.setToolTip(_translate("MainWindow", "Suffix for the file name"))
        self.string_to_find_label.setText(_translate("MainWindow", "String to find"))
        self.string_to_find_line_edit.setToolTip(_translate("MainWindow", "Comma separated strings in file name that you want to replace"))
        self.string_to_replace_label.setText(_translate("MainWindow", "String to replace"))
        self.string_to_replace_line_edit.setToolTip(_translate("MainWindow", "Replacement string"))
        self.extension_label.setText(_translate("MainWindow", "Extensions"))
        self.extension_drop_down.setToolTip(_translate("MainWindow", "The file type you want to modify"))
        self.extension_drop_down.setItemText(0, _translate("MainWindow", "all"))
        self.run_button.setToolTip(_translate("MainWindow", "Run the renamer"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.reset_button.setToolTip(_translate("MainWindow", "Reset all inputs"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.file_view_list_widget.setToolTip(_translate("MainWindow", "Shows the list of files to rename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
