import os
from .linter import lint
from pprint import PrettyPrinter

pp = PrettyPrinter(
    indent=2,
    width=100,
    compact=True
)


class FileProcessor:
    def __init__(self, reader, writer, output_target, logger):
        self.reader = reader
        self.writer = writer
        self.logger = logger
        self.output_target = output_target
        self.content = {}

    def execute(self) -> dict:
        try:
            self.content = self.reader.read()
        except FileNotFoundError:
            print("Error: File Not Found: {0}".format(self.reader.filename))
            return {}

        # lookup-table that maps a message to its findings
        findings = dict()
        for message_id, message in self.content.items():
            if message is None:
                continue

            self.logger.log_info("Processing...\"{0}\": \"{1}\"".format(message_id, message))

            if type(message) is dict and message['message'] is not None:
                message = message['message']
            elif type(message) is not str:
                continue
            else:  # type(message) is str
                pass

            findings[message_id] = dict(message=message, linted=[])

            found_something = lint(message)

            if len(found_something):
                print(">>> '{0}': \"{1}\"".format(message_id, message))
                for something in found_something:
                    findings[message_id]["linted"].append(something['desc'])
                    print(">>> {0}".format(something['desc']))
                print('~' * 10)

        if len(findings):
            os.makedirs(self.output_target['folder_path'], exist_ok=True)
            self.writer.write(findings)
        return findings

