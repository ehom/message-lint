import os
import json
from jproperties import Properties
from .str_lint import lint


class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.bins = {}

    def process(self):
        print("process {}".format(self.filename))

    @staticmethod
    def get(filename):
        table = {
            'json': JsonFileProcessor,
            'properties': JavaPropertiesProcessor,
        }

        if filename.endswith('.json'):
            return table['json'](filename)
        elif filename.endswith('.properties'):
            return table['properties'](filename)
        else:
            return NullFileProcessor(filename)


class NullFileProcessor(FileProcessor):
    def __init__(self, filename):
        super().__init__(filename)

    def process(self):
        print("Can not process '{0}'".format(self.filename))

# TODO: This class needs work


class JavaPropertiesProcessor(FileProcessor):
    def __init__(self, filename):
        super().__init__(filename)

    def process(self) -> dict:
        with open(self.filename, "rb") as f:
            properties = Properties()
            properties.load(f, "utf-8")
            for item in properties.items():
                message_id, message = item[0], item[1][0]
                found_something = lint(message)
                if len(found_something) > 0:
                    for something in found_something:
                        output_filename = something['outputFile']
                        if output_filename not in self.bins:
                            self.bins[output_filename] = Properties()
                        self.bins[output_filename][message_id] = message
        return self.bins


class JsonFileProcessor(FileProcessor):
    def __init__(self, filename):
        super().__init__(filename)

    def process(self) -> dict:
        print("filename: ", self.filename)
        folder_path = os.path.dirname(self.filename)
        print("folder_path: ", folder_path)

        # try block?
        with open(self.filename) as f:
            content = json.load(f)

        for item in content.items():
            if item[1] is None or 'message' not in item[1]:
                continue
            message_id, message = [item[0], item[1]['message']]
            print("'{0}': \"{1}\"\n".format(message_id, message))
            found_something = lint(message)
            if len(found_something):
                print("found_something:", found_something)
                print("'{0}': >>> \"{1}\"\n".format(message_id, message))
                for something in found_something:
                    bin_name = something['outputFile']
                    if bin_name not in self.bins:
                        self.bins[bin_name] = {}
                    self.bins[bin_name][message_id] = message
        return self.bins
