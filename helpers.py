import shutil
import os


def emptyDirectory(dir):
    """accepts a directory abs path that in the end gets deleted if it exists

    Args:
        dir (string): accepts the abs path to the folder

    Returns:
        string: message on completion
    """
    if os.path.exists(dir):
        directory_contents = os.listdir(dir)
        if not directory_contents:
            return "The directory is empty"
        else:
            shutil.rmtree(dir)
            return "The directory exists."
    else:
        return "The directory does not exist."


def changeToTxt(file):
    """changes the extension of given file

    Args:
        file (string): accepts abs path to the file
    """
    if os.path.exists(file):
        new_extension = ".txt"
        root, extension = os.path.splitext(file)
        if extension == ".txt":
            return "Already a .txt"
        new_file_path = root + new_extension
        os.rename(file, new_file_path)
        return "Success"

    else:
        return "Failure"
