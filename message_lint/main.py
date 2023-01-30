import os
import sys
import pathlib
import time
import logging

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
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S",
        filename='message_lint.log', level=logging.INFO)

    logging.info(f"Input files: {args.files}")
    logging.info(f"Output folder path: {args.output_folder}")

    for file in args.files:
        reader = utils.FileReader.get(file)

        # build file path for the output folder
        file_path = build_file_path(file, args.output_folder, extra_folder="message_lint_reports")

        # print("output file path:", file_path)

        if pathlib.Path(file_path).suffix == ".properties":
            file_path = file_path + ".json"

        print("The output will be written here:", file_path)

        writer = utils.FileWriter.get(file_path)

        FileProcessor(reader, writer).execute()
