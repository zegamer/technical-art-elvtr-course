"""
Backend module.

Renames files of a specific extension in a folder
"""

import os
import shutil
import logging


class BatchRenamer:
    """
    A class to handle batch renaming of files in a specified directory.

    Attributes:
        filepath (str): The path to the directory containing files to rename.
        copy_files (bool): Whether to copy files instead of renaming them.
        filetypes (list[str]): List of file extensions to target for renaming.
        strings_to_find (list[str]): List of strings to find in filenames.
        string_to_replace (str): String to replace found strings with.
        prefix (str): Prefix to add to filenames.
        suffix (str): Suffix to add to filenames.
        print_to_screen (bool): Whether to print log messages to the console.

    Methods:
        initialize_logger(print_to_screen=False):
            Initializes the logger for the class.
        
        get_file_constituents(file_path: str) -> str:
            Returns the constituents of a file given its path.
        
        get_renamed_file_path(
            existing_name: str,
            string_to_find: str,
            string_to_replace: str,
            prefix: str, suffix: str
        ) -> str:
            Returns the target file path given an existing file name
            and string operations.
        
        get_files_with_extension(folder_path: str, extension: str) -> list[str]:
            Returns a collection of files in a given folder with an extension
            that matches the provided extension.
        
        rename_file(existing_name: str, new_name: str, copy=False) -> None:
            Renames a file if it exists.
        
        rename_files_in_folder(
            folder_path: str,
            extension: str,
            string_to_find: str,
            string_to_replace: str,
            prefix: str,
            suffix: str,
            copy=False
        ):
            Renames all files in a folder with a given extension.
    """
    def __init__(
            self, 
            filepath          = None,
            copy_files        = False,
            filetypes         = None,
            strings_to_find   = None,
            string_to_replace = "",
            prefix            = None,
            suffix            = None,
            print_to_screen   = False
        ):
        self.filepath          = filepath
        self.copy_files        = copy_files
        self.filetypes         = filetypes
        self.strings_to_find   = strings_to_find
        self.string_to_replace = string_to_replace
        self.prefix            = prefix
        self.suffix            = suffix
        self.print_to_screen   = print_to_screen

        self.__initialize_logger(self.print_to_screen)


    def __initialize_logger(self, print_to_screen = False):
        """
        Creates a logger

        Args:
            print_to_screen: for printing to screen as well as file
        """

        ###############
        # Basic Setup #
        ###############
        app_title = 'Test'
        version_number = '1.0.0'
        # get the path the script was run from, storing with forward slashes
        source_path = os.path.dirname(os.path.realpath(__file__))
        # create a log filepath
        logfile_name = f'{app_title}.log'
        logfile = os.path.join(source_path, logfile_name)

        # tell the user where the log file is
        print(f'Logfile is {logfile}')

        # more initialization
        self.logger = logging.getLogger(f'{app_title} Logger')
        self.logger.setLevel(logging.INFO)
        
        ###############################
        # Formatter and Handler Setup #
        ###############################
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.INFO)
        # formatting information we want (time, self.logger name, version, etc.)
        formatter = logging.Formatter(
            f'%(asctime)s - %(name)s {version_number} - '
            '%(levelname)s - %(message)s'
        )
        # setting the log file format
        file_handler.setFormatter(formatter)
        # clean up old handlers
        self.logger.handlers.clear()

        # add handler
        self.logger.addHandler(file_handler)

        # allowing to print to screen
        if print_to_screen:
            # create a new "stream handler" for logging/printing to screen
            console = logging.StreamHandler()
            self.logger.addHandler(console)
            # setting the print log format
            console.setFormatter(formatter)

        self.logger.info('Logger Initiated')


    def __get_file_constituents(self, file_path: str) -> str:
        """
        Return the constituents of a file given its path.

        Args:
            file_path: the path of the file whose name you'd like to get
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        folder_path = os.path.dirname(file_path)
        file_name, extension = os.path.basename(file_path).split(".")
        return folder_path, file_name, extension


    def __get_renamed_file_path(
            self,
            existing_name: str,
            string_to_find: str,
            string_to_replace: str,
            prefix: str,
            suffix: str
        ) -> str:
        """
        Return the target file path given an existing file name
        and string operations.

        Args:
            log: logger instance
            existing_name: the existing file's name
            string_to_find: string to find and replace in the existing filename
            string_to_replace: the string you'd like to replace it with
            prefix: a string to insert at the beginning of the file path
            suffix: a string to append to the end of the file path
        """
        if isinstance(string_to_find, str):
            string_to_find = [string_to_find]

        try:
            folder_name, file_name, extension = self.__get_file_constituents(
                existing_name
            )

            # Set the prefix and suffix of the file name (if exists)
            if prefix != "":
                file_name = f"{prefix}_{file_name}"
            if suffix != "":
                file_name = f"{file_name}_{suffix}"

            for string in string_to_find:
                file_name = file_name.replace(string, string_to_replace)

            return os.path.join(folder_name, f"{file_name}.{extension}")
        
        except FileNotFoundError as file_exception:
            self.logger.error(
                "File does not exist. Make sure the path is correct."
            )
            self.logger.error(f"Exception: {file_exception}")
            return ""


    def __get_files_with_extension(
            self,
            folder_path: str,
            extension: str
        ) -> list[str]:
        """
        Return a collection of files in a given folder with an extension
        that matches the provided extension.

        Args:
            log: logger instance
            folder_path: The path of the folder to search the files
            extension: The extension of file to be searched
        """
        try:
            if not os.path.isdir(folder_path):
                raise FileNotFoundError(
                    f"The folder {folder_path} does not exist."
                )

            # Make sure the extension starts with a dot
            if not extension.startswith("."):
                extension = "." + extension

            # Find files in the directory with the given extension
            files = [
                os.path.join(folder_path, file)
                for file in os.listdir(folder_path)
                if file.endswith(extension)
            ]

            return files

        except FileNotFoundError as file_exception:
            self.logger.error(
                "Folder does not exist. Make sure the path is correct."
            )
            self.logger.error(f"Exception: {file_exception}")
            return []

        except Exception as exception:
            self.logger.critical(
                f"An unknown error occurred when getting files with extension: "
                f"{exception}"
            )
            return []


    def __rename_file(
        self,
        existing_name: str,
        new_name: str,
        copy=False
    ) -> None:
        """
        Rename a file if it exists.

        By default, should move the file from its original path to its new path
        removing the old file
        If copy is set to True, duplicate the file to the new path

        Args:
            log: logger instance
            existing_name: full filepath a file that should already exist
            new_name: full filepath for new name
            copy_mode: copy instead of rename
        """
        try:
            if not os.path.isfile(existing_name):
                raise FileNotFoundError(
                    f"The file {existing_name} does not exist."
                )

            if copy:
                shutil.copy(existing_name, new_name)
            else:
                shutil.move(existing_name, new_name)

        except FileNotFoundError:
            self.logger.error(
                "File does not exist. Make sure the path is correct."
            )

        except Exception as exception:
            self.logger.critical(
                f"An unknown error occurred when renaming file: "
                f"{exception}"
            )


    def rename_files_in_folder(
        self,
        folder_path: str,
        extension: str,
        string_to_find: str,
        string_to_replace: str,
        prefix: str,
        suffix: str,
        copy=False,
    ):
        """
        Rename all files in a folder with a given extension.

        This should operate only on files with the provided extension
        Every instance of string_to_find in the filepath should be replaced
        with string_to_replace
        Prefix should be added to the front of the file name
        Suffix should be added to the end of the file name

        Args:
            log: logger instance
            folder_path: the path to the folder the renamed files are in
            extension: the extension of the files you'd like renamed
            string_to_find: the string in the filename you'd like to replace
            string_to_replace: the string you'd like to replace it with
            prefix: a string to insert at the beginning of the file path
            suffix: a string to append to the end of the file path
            copy: whether to rename/move the file or duplicate/copy it
        """
        try:
            # Get all files in the folder with the given extension
            files = self.__get_files_with_extension(folder_path, extension)

            if files == []:
                self.logger.warning(
                    "No files found in the folder with the given extension."
                )
                return

            self.logger.info(f"Files found: {files}")

            for file in files:
                new_path = self.__get_renamed_file_path(
                    existing_name=file,
                    string_to_find=string_to_find,
                    string_to_replace=string_to_replace,
                    prefix=prefix,
                    suffix=suffix,
                )
                self.__rename_file(file, new_path, copy)
                self.logger.info(f"File {file} renamed to {new_path}")

        except Exception as exception:
            self.logger.critical(
                f"An unknown error occurred when renaming file: "
                f"{exception}"
            )


if __name__ == "__main__":
    x = BatchRenamer(print_to_screen=False)

    x.rename_files_in_folder("testing_files", "ma",
                             ("_file_01", "_file_final_new_02b"), "",
                             "M", "C", True
                            )