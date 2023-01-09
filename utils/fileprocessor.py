from .str_lint import lint
from pprint import PrettyPrinter

pp = PrettyPrinter(
    indent=4,
    width=100,
    compact=True
)


class FileProcessor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.bins = {}
        self.content = {}

    def execute(self) -> dict:
        try:
            self.content = self.reader.read()
            pp.pprint(self.content)
        except FileNotFoundError:
            print("Error: File Not Found: {}".format(self.reader.filename))
            return {}

        for item in self.content.items():
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

        for binName, contents in self.bins.items():
            print("Printing contents of bin...")
            pp.pprint(contents)

            print("binName:", binName)
            self.writer.write(binName, contents)

        if len(self.bins):
            print("bins:", self.bins.keys())

        return self.bins

