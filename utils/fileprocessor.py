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

        # lookup table that maps a message to its findings
        findings = {}
        for message_id, message in self.content.items():
            if message is None:
                continue
            print("processing....message_id:", message_id)
            print("processing....message:", message)

            if type(message) is dict and message['message'] is not None:
                message = message['message']
            elif type(message) is not str:
                continue
            else:  # type(message) is str
                pass

            findings[message_id] = {
                "message": message,
                "linted": []
            }

            print("'{0}': \"{1}\"\n".format(message_id, message))

            found_something = lint(message)
            if len(found_something):
                print("found_something:", found_something)
                print("'{0}': >>> \"{1}\"\n".format(message_id, message))

                for something in found_something:
                    findings[message_id]["linted"].append(something['desc'])
                # print(self.reader.filename)
                # pp.pprint(findings)
                self.writer.write(findings)
        return findings

