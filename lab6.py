import unittest
from helpers import *


class TestClass(unittest.TestCase):
    def test_1(self):
        # check to change to txt
        file_path = "file1.txt"
        absolute_path = os.path.abspath(file_path)
        result = changeToTxt(absolute_path)

        self.assertEqual(result, "Already a .txt")

    def test_2(self):
        # check if its not empty
        os.mkdir("toDelete2")
        with open("toDelete2/myfile.txt", "w") as f:
            f.write("Hello, world!")
        folder_path = os.path.abspath("toDelete2")
        result = emptyDirectory(folder_path)

        self.assertEqual(result, "The directory exists.")

    def test_3(self):
        # check if empty
        if not os.path.exists("toDelete"):
            os.mkdir("toDelete")
        folder_path = os.path.abspath("toDelete")
        result = emptyDirectory(folder_path)

        self.assertEqual(result, "The directory is empty")

    def test_4(self):
        # check if folder does not exist
        folder_path = os.path.abspath("temp")
        result = emptyDirectory(folder_path)

        self.assertEqual(result, "The directory does not exist.")


if __name__ == "__main__":
    unittest.main()
