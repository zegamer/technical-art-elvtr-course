import os
import sys

from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication

from batch_renamer_ui import Ui_MainWindow
from batch_renamer_backend import BatchRenamerBackend


class BatchRenamerWindow(QMainWindow, Ui_MainWindow):
    """
    A GUI application for batch renaming files using PyQt6.

    This class provides a user interface for selecting a directory, specifying 
    renaming rules (such as find-and-replace, prefix, and suffix), and executing 
    batch renaming operations using `BatchRenamerBackend`.

    Attributes:
        file_list (list): List of file names in the selected directory.
        batch_renamer (BatchRenamerBackend): Backend instance for renaming files.
        logger (Logger): Logger for logging errors and status messages.

    Methods:
        reset_inputs():
            Resets all input fields and restores default values.

        get_file_path():
            Opens a file dialog to select a directory.

        set_file_path():
            Updates the file path input field and refreshes the file list.

        set_file_list():
            Populates `file_list` with files in the selected directory.

        update_file_view():
            Clears and repopulates the file list widget with files from the 
            directory.

        update_extension_drop_down():
            Updates the file extension filter dropdown based on available
            file types.

        get_element_value(value):
            Returns the first element if `value` is a tuple;
            otherwise, returns `value` itself.

        filter_files_by_extension():
            Filters the displayed file list based on the selected extension.

        run_renamer():
            Collects user input, applies renaming rules, and executes batch renaming.

    """
    def __init__(self):

        # Initialise class variables
        self.file_list = []
        self.file_path = ""

        # UI setup
        super().__init__()
        super(Ui_MainWindow).__init__()
        self.setupUi(self)

        # Instance the "back end"
        self.batch_renamer = BatchRenamerBackend(print_to_screen=True)
        self.logger = self.batch_renamer.logger

        # Instantiate the action buttons
        self.browse_button.clicked.connect(self.get_file_path)
        self.run_button.clicked.connect(self.run_renamer)
        self.reset_button.clicked.connect(self.reset_inputs)

        # Based on extension, change the file view
        self.extension_drop_down.currentIndexChanged.connect(
            self.filter_files_by_extension
        )

        # Show UI normal vs maximized
        self.showNormal()


    def reset_inputs(self):
        """
        Reset all inputs to default values
        """
        self.file_list = []
        self.file_path_line_edit.clear()
        self.string_to_find_line_edit.clear()
        self.string_to_replace_line_edit.clear()
        self.prefix_line_edit.clear()
        self.suffix_line_edit.clear()
        self.rename_radio_button.setChecked(True)
        self.copy_radio_button.setChecked(False)
        self.extension_drop_down.clear()
        self.extension_drop_down.addItem("all")
        self.file_view_list_widget.clear()


    def get_file_path(self):
        """
        Open a file dialog for browsing to a folder
        """
        self.file_path = QFileDialog().getExistingDirectory()
        self.set_file_path()


    def set_file_path(self):
        """
        Set lineEdit text for filepath
        """
        self.file_path_line_edit.setText(self.file_path)

        # Update list and file type drop down based on the fetched files
        self.update_file_view()
        self.set_file_list()
        self.update_extension_drop_down()


    def set_file_list(self):
        """
        Create a list of files currently in the selected folder
        """
        self.file_list = []
        for file in range(self.file_view_list_widget.count()):
            self.file_list.append(self.file_view_list_widget.item(file).text())


    def update_file_view(self):
        """
        Clear listwidget, read files in filepath with os.walk and
        add files as new items
        """
        self.file_view_list_widget.clear()
        for root, dirs, files in os.walk(self.file_path):
            self.file_view_list_widget.addItems(files)


    def update_extension_drop_down(self):
        """
        Update the extension drop down based on the files in the file view
        """
        available_extensions = ["all"]

        for file in range(self.file_view_list_widget.count()):
            try:
                file = self.file_view_list_widget.item(file).text()
                extension = os.path.basename(file).split(".")[-1]
                if extension and (extension not in available_extensions):
                    available_extensions.append(extension)
            except (TypeError, ValueError):
                available_extensions.append("")
                continue
            except Exception as exception:
                self.logger.error(
                    "Error occurred when updating extension drop down, %s",
                    exception
                )

        self.extension_drop_down.clear()
        self.extension_drop_down.addItems(available_extensions)


    def get_element_value(self, value):
        """
        Check if element is a tuple and return the first element

        Args:
            value (str|tuple): Value to check
        """
        return value[0] if isinstance(value, tuple) else value


    def filter_files_by_extension(self):
        """
        Filter the file list based on the selected extension in the dropdown.
        """
        selected_extension = self.extension_drop_down.currentText()
        self.file_view_list_widget.clear()

        if selected_extension == "all":
            self.file_view_list_widget.addItems(self.file_list)

        for file in self.file_list:
            if file.endswith(selected_extension):
                self.file_view_list_widget.addItem(file)


    def run_renamer(self):
        """
        Run back end batch renamer using self.batch_renamer
        self.batch_renamer is an instance of the BatchRenamer class
        """
        try:
            folder_path = self.get_element_value(
                self.file_path_line_edit.text()
            )

            # String to find can be a comma separated value
            string_to_find = self.get_element_value(
                self.string_to_find_line_edit.text()
            )
            string_to_find = [i.strip() for i in string_to_find.split(",")]

            string_to_replace = self.get_element_value(
                self.string_to_replace_line_edit.text()
            )
            prefix = self.get_element_value(self.prefix_line_edit.text())
            suffix = self.get_element_value(self.suffix_line_edit.text())

            copy = self.copy_radio_button.isChecked()
            extension = self.extension_drop_down.currentText()

            self.batch_renamer.rename_files_in_folder(
                folder_path=folder_path,
                extension=extension,
                string_to_find=string_to_find,
                string_to_replace=string_to_replace,
                prefix=prefix,
                suffix=suffix,
                copy=copy
            )

        except Exception as e:
            self.logger.critical(
                "Error occurred when running the batch renamer"
            )
            self.logger.critical("Error: %s", e)

        finally:
            # After every run, automatically update the file list
            self.set_file_path()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BatchRenamerWindow()
    sys.exit(app.exec())
