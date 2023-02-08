import os
import sys

from .custom_output_target import customize_output_target
from .logger import Logger

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

import utils
from .fileprocessor import FileProcessor


def main(args):
    startup_logger = Logger().get(verbose=True)
    startup_logger.log_info(f"Input files: {args.files}")
    startup_logger.log_info(f"Output folder path: {args.output_folder}")
    startup_logger.log_info(f"Verbose: {args.verbose}")

    logger = Logger().get(verbose=args.verbose)

    for file in args.files:
        reader = utils.FileReader.get(file)

        # build file path for the output folder
        output_target: dict = customize_output_target(file, args.output_folder)

        print(f"The lint report for file \"{file}\" will be saved here: {output_target['file_path']}")

        writer = utils.FileWriter.get(output_target["file_path"])

        FileProcessor(reader, writer, output_target, logger).execute()

        print(f"The lint report for file \"{file}\" has been saved here: {output_target['file_path']}")
