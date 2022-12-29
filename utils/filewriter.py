import os
import json


class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.folder_path = FileWriter.build_output_folder(filename)
        print("FileWriter:", self.folder_path)

    @staticmethod
    def build_output_folder(filename) -> str:
        folder_path = os.path.dirname(filename)
        basename = os.path.basename(filename)
        basename = os.path.splitext(basename)[0]
        folder_path = os.path.join(folder_path, "output", basename)
        exists = os.path.isdir(folder_path)
        if not exists:
            os.makedirs(folder_path, exist_ok=True)
        return folder_path

    @staticmethod
    def get(filename):
        table = {
            'json': JsonFileWriter,
            'properties': PropertiesFileWriter
        }

        if filename.endswith('.json'):
            return table['json'](filename)
        elif filename.endswith('.properties'):
            return table['properties'](filename)
        else:
            return BadFileWriter(filename)


class BadFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)

    def write(self, bin_name, dict_obj):
        pass


class JsonFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)
        self.file_extension = ".json"

    def write(self, bin_name, dict_obj):
        output_filename = bin_name + self.file_extension
        output_path = os.path.join(self.folder_path, output_filename)

        json_obj_str = json.dumps(dict_obj, indent=4)
        with open(output_path, 'w') as outputHandle:
            outputHandle.write(json_obj_str)


class PropertiesFileWriter(FileWriter):
    def __init__(self, filename):
        super().__init__(filename)
        self.file_extension = ".properties"

    def write(self, bin_name, properties):
        output_filename = bin_name + self.file_extension
        output_path = os.path.join(self.folder_path, output_filename)
        with open(output_path, "wb") as f:
            properties.store(f, encoding="utf-8")
