from .linter import lint
from pprint import PrettyPrinter
import logging

pp = PrettyPrinter(
    indent=2,
    width=100,
    compact=True
)


class FileProcessor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.content = {}

    def execute(self) -> dict:
        try:
            self.content = self.reader.read()
            # pp.pprint(self.content)
        except FileNotFoundError:
            print("Error: File Not Found: {0}".format(self.reader.filename))
            return {}

        # lookup-table that maps a message to its findings
        findings = {}
        for message_id, message in self.content.items():
            if message is None:
                continue

            logging.info("Processing...\"{0}\": \"{1}\"".format(message_id, message))

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

            found_something = lint(message)

            if len(found_something):
                print(">>> '{0}': \"{1}\"".format(message_id, message))
                for something in found_something:
                    findings[message_id]["linted"].append(something['desc'])
                    print(">>> {0}".format(something['desc']))
                print('~' * 10)
                self.writer.write(findings)
        return findings

