import os
import sys
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication
# import PyQt6.QtCore 

from batch_renamer_ui import Ui_main_window 
from batch_rename_backend import BatchRenamer


class BatchRenamerWindow(QMainWindow, Ui_main_window):
    def __init__(self):
        
        # Initialise class variables
        self.file_list = []
        
        # UI setup
        super().__init__()
        super(Ui_main_window).__init__()
        self.setupUi(self)
        
        # Instance the "back end"
        self.batch_renamer = BatchRenamer(print_to_screen=True)
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
        self.file_path_line_edit.setText("")
        self.string_to_find_line_edit.setText("")
        self.string_to_replace_line_edit.setText("")
        self.prefix_line_edit.setText("")
        self.suffix_line_edit.setText("")
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
        Create a list of file currently in the selected file path
        """
        for file in range(self.file_view_list_widget.count()):
            self.file_list.append(self.file_view_list_widget.item(file).text())


    def update_file_view(self):
        """
        Clear listwidget
        read files in filepath with os.walk
        Add files as new items
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
            except TypeError or ValueError:
                available_extensions.append("")
                continue
            except Exception as e:
                self.logger.error(
                    "Error occurred when updating extension drop down, "
                    f"error: {e} ")
        
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

            folder_path = self.get_element_value(self.file_path_line_edit.text())
            
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
            
            # rename = self.rename_radio_button.isChecked()
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
            self.logger.critical(f"Error: {e}")
        
        finally:
            # After every run, automatically update the file list
            self.update_file_view()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BatchRenamerWindow()
    sys.exit(app.exec())
 