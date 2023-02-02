import os
import sys
import pathlib
import time
from .logger import Logger

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

import utils
from .fileprocessor import FileProcessor


def derive_output_target(filename, target_path) -> dict:
    def get_filename_info(fname: str) -> dict:
        abspath = os.path.abspath(fname)
        p = pathlib.Path(abspath)

        return {
            "abspath_folder": p.parents[0],
            "filename":  p.name
        }

    info = get_filename_info(filename)

    if target_path:
        folder_path = os.path.abspath(target_path)
    else:
        folder_path = info['abspath_folder']
    folder_path = os.path.join(folder_path, "message_lint_reports")

    str_time = time.strftime("%Y%m%d-%H%M%S")
    filename = str_time + "_" + info['filename']

    file_path = os.path.join(folder_path, filename)

    if pathlib.Path(file_path).suffix == ".properties":
        file_path = file_path + ".json"

    return {
        "folder_path": folder_path,
        "file_path": file_path
    }


def main(args):
    startup_logger = Logger().get(verbose=True)
    startup_logger.log_info(f"Input files: {args.files}")
    startup_logger.log_info(f"Output folder path: {args.output_folder}")
    startup_logger.log_info(f"Verbose: {args.verbose}")

    logger = Logger().get(verbose=args.verbose)

    for file in args.files:
        reader = utils.FileReader.get(file)

        # build file path for the output folder
        output_target: dict = derive_output_target(file, args.output_folder)

        print(f"The lint report for file \"{file}\" will be saved here: {output_target['file_path']}")

        writer = utils.FileWriter.get(output_target["file_path"])

        FileProcessor(reader, writer, output_target, logger).execute()

        print(f"The lint report for file \"{file}\" has been saved here: {output_target['file_path']}")
