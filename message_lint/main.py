import os
import sys
import pathlib
import time
from .logger import Logger

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

import utils
from .fileprocessor import FileProcessor


def build_file_path(filename, target_path, extra_folder=None) -> str:
    """ build a file_path """
    file_path = os.path.abspath(filename)
    p = pathlib.Path(file_path)
    src_path = p.parents[0]
    filename = p.name

    # print(src_path, filename)

    if target_path is None:
        target_path = src_path
    else:
        target_path = os.path.abspath(target_path)

    if extra_folder is not None:
        target_path = os.path.join(target_path, extra_folder)

    # print("path of target folder:", target_path)

    os.makedirs(target_path, exist_ok=True)

    # prefix output filename with timestamp
    str_time = time.strftime("%Y%m%d-%H%M%S")
    filename = str_time + "_" + filename

    file_path = os.path.join(target_path, filename)

    # print("path of target file:", file_path)

    return file_path


def main(args):
    startup_logger = Logger().get(verbose=True)
    startup_logger.log_info(f"Input files: {args.files}")
    startup_logger.log_info(f"Output folder path: {args.output_folder}")
    startup_logger.log_info(f"Verbose: {args.verbose}")

    logger = Logger().get(verbose=args.verbose)

    for file in args.files:
        reader = utils.FileReader.get(file)

        # build file path for the output folder
        file_path = build_file_path(file, args.output_folder, extra_folder="message_lint_reports")

        # print("output file path:", file_path)

        if pathlib.Path(file_path).suffix == ".properties":
            file_path = file_path + ".json"

        print(f"The lint report for file \"{file}\" will be saved here: {file_path}")

        writer = utils.FileWriter.get(file_path)

        FileProcessor(reader, writer, logger).execute()

        print(f"The lint report for file \"{file}\" has been saved here: {file_path}")
