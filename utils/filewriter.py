import os
import json
import pathlib
from jproperties import Properties


class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.folder_path = os.path.dirname(filename)
        print("FileWriter:", self.folder_path)

    @staticmethod
    def get(filename):
        table = {
            '.json': JsonFileWriter,
            '.properties': PropertiesFileWriter
        }
        file_extension = pathlib.Path(filename).suffix
        if file_extension in table:
            return table[file_extension](filename)
        else:
            return BadFileWriter(filename)


class BadFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, bin_name, dict_obj):
        print("bad file writer")


class JsonFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, dict_obj):
        json_obj_str = json.dumps(dict_obj, indent=4)
        with open(self.filename, 'w') as outputHandle:
            outputHandle.write(json_obj_str)


class PropertiesFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, dict_obj):
        properties = Properties()
        for message_id, message in dict_obj.items():
            properties[message_id] = message['message']

        with open(self.filename, "wb") as f:
            properties.store(f, encoding="utf-8")
