import unittest
import filewriter as fw


class FileWriterTest(unittest.TestCase):
    def test_json_filewriter(self):
        filename = "../test_files/test.json"
        reader = fw.FileWriter.get(filename)
        self.assertEqual(type(reader), type(fw.JsonFileWriter(filename)))

    def test_null_filewriter(self):
        filename = "../test_files/test.j"
        reader = fw.FileWriter.get(filename)
        self.assertEqual(type(reader), type(fw.BadFileWriter(filename)))

    def test_properties_filewriter(self):
        filename = "../test_files/test.properties"
        reader = fw.FileWriter.get(filename)
        self.assertEqual(type(reader), type(fw.PropertiesFileWriter(filename)))


if __name__ == '__main__':
    unittest.main()
