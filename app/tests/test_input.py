import unittest
import pandas
from app.io.input import readfile, readfilepandas


class TestIO(unittest.TestCase):
    def test_readfile(self):
        file_path = r"../../data/test.txt"

        with open(file_path):
            res = readfile(file_path)

        with open(file_path) as file:
            string = file.read()

        self.assertEqual(res, string)

    def test_readfile_2(self):
        file_path = r"../../data/test2.txt"
        with open(file_path):
            res = readfile(file_path)

        with open(file_path) as file:
            string = file.read()

        self.assertEqual(res, string)

    def test_readfile_3(self):
        file_path = r"../../data/test3.txt"
        with open(file_path):
            res = readfile(file_path)

        with open(file_path) as file:
            string = file.read()

        self.assertEqual(res, string)

    def test_readfilepandas(self):
        file_path = r"../../data/test.txt"

        with open(file_path):
            res = readfilepandas(file_path)

        with open(file_path) as file:
            data_frame = pandas.read_table(file)

        self.assertEqual(res.to_string(), data_frame.to_string())

    def test_readfilepandas_2(self):
        file_path = r"../../data/test2.txt"

        with open(file_path):
            res = readfilepandas(file_path)

        with open(file_path) as file:
            data_frame = pandas.read_table(file)

        self.assertEqual(res.to_string(), data_frame.to_string())

    def test_readfilepandas_3(self):
        file_path = r"../../data/test3.txt"

        with open(file_path):
            res = readfilepandas(file_path)

        with open(file_path) as file:
            data_frame = pandas.read_table(file)

        self.assertEqual(res.to_string(), data_frame.to_string())


if __name__ == '__main__':
    unittest.main()
