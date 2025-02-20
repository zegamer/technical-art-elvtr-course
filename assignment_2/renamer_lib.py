"""
Library module.

Renames files of a specific extension in a folder
"""

import os
import shutil
import logger


def get_logger(print_to_screen=False):
    """
    Use the logger.py module to create a logger.

    Args:
        print_to_screen: for printing to screen as well as file
    """
    return logger.initialize_logger(print_to_screen)


def get_file_constituents(file_path: str) -> str:
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


def get_renamed_file_path(
    log,
    existing_name: str,
    string_to_find: str,
    string_to_replace: str,
    prefix: str,
    suffix: str,
) -> str:
    """
    Return the target file path given an existing file name
    and string operations.

    Args:
        log: logger instance
        existing_name: the existing file's name
        string_to_find: a string to find and replace in the existing filename
        string_to_replace: the string you'd like to replace it with
        prefix: a string to insert at the beginning of the file path
        suffix: a string to append to the end of the file path
    """
    if isinstance(string_to_find, str):
        string_to_find = list(string_to_find)

    try:
        folder_name, file_name, extension = get_file_constituents(existing_name)

        # Set the prefix and suffix of the file name (if exists)
        if prefix != "":
            file_name = f"{prefix}_{file_name}"
        if suffix != "":
            file_name = f"{file_name}_{suffix}"

        for string in string_to_find:
            file_name = file_name.replace(string, string_to_replace)

        return os.path.join(folder_name, f"{file_name}.{extension}")
    
    except FileNotFoundError as file_exception:
        log.error("File does not exist. Make sure the path is correct.")
        log.error(f"Exception: {file_exception}")
        return ""


def get_files_with_extension(
    log,
    folder_path: str,
    extension: str
) -> list[str]:
    """
    Return a collection of files in a given folder with an extension
    that matches the provided extension.

    Args:
        log: logger instance
        folder_path: The path of the folder whose files you'd like to search
        extension: The extension of files you'd like to include in the return
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
        log.error("Folder does not exist. Make sure the path is correct.")
        log.error(f"Exception: {file_exception}")
        return []

    except Exception as exception:
        log.critical(
            f"An unknown error occurred when getting files with extension: "
            f"{exception}"
        )
        return []


def rename_file(log, existing_name: str, new_name: str, copy=False) -> None:
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
        log.error("File does not exist. Make sure the path is correct.")

    except Exception as exception:
        log.critical(
            f"An unknown error occurred when renaming file: "
            f"{exception}"
        )


def rename_files_in_folder(
    log,
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
        files = get_files_with_extension(log, folder_path, extension)

        if files == []:
            log.warning(
                "No files found in the folder with the given extension."
            )
            return

        log.info(f"Files found: {files}")

        for file in files:
            new_path = get_renamed_file_path(
                log=log,
                existing_name=file,
                string_to_find=string_to_find,
                string_to_replace=string_to_replace,
                prefix=prefix,
                suffix=suffix,
            )
            rename_file(log, file, new_path, copy)
            log.info(f"File {file} renamed to {new_path}")

    except Exception as exception:
        log.critical(
            f"An unknown error occurred when renaming file: "
            f"{exception}"
        )


def main():
    """Main function tests the functions in this module.
    """
    # Logger
    log = get_logger(True)
    log.info("Logger Initiated")

    #   Here are some examples of different logger messages
    log.warning("This would be a log warning")
    log.error("This would be a logger error!!")
    log.critical("This would be a critical log")


if __name__ == "__main__":
    main()
