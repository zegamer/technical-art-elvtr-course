import renamer_lib as renamer

"""
============================
== DO NOT EDIT THIS FILE! ==
============================
This file will be run to ensure your renamer_lib file is filled out properly
"""


def main():
    # Logger
    logger = renamer.get_logger(True)

    # Rename .ma files
    renamer.rename_files_in_folder(logger, "assignment_2/testing_files", "ma", 
                                   ("_file_01", "_file_final_new_02"),
                                   "", "M_", "", False)
    
    # Rename .txt files
    renamer.rename_files_in_folder(logger, "assignment_2/testing_files", "txt", "", "",
                                   "NOTE_", "_TEMP", True)
    
    # Rename .png files
    renamer.rename_files_in_folder(logger, "assignment_2/testing_files", "png", 
                                   ("diffuse", "color"), "C", "", "")
    renamer.rename_files_in_folder(logger, "assignment_2/testing_files", "png",
                                   ("texture", "tex"), "T", "", "")


if __name__ == '__main__':
    main()
