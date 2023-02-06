import os
import pathlib
import time
import utils


def customize_filename(func):
    def func_wrapper(filename: str, folder: str) -> dict:
        def prefix_filename_with_timestamp(filename_input: str):
            str_time = time.strftime("%Y%m%d-%H%M%S")
            return f"{str_time}_{filename_input}"

        result = func(filename, folder)

        new_filename = prefix_filename_with_timestamp(result['file_path'])
        result['file_path'] = os.path.join(result['folder_path'], new_filename)

        if pathlib.Path(result['file_path']).suffix == ".properties":
            result['file_path'] = result['file_path'] + ".json"
        return result
    return func_wrapper


def customize_folder_path(func):
    def func_wrapper(filename: str, folder: str) -> dict:
        result = func(filename, folder)
        result['folder_path'] = os.path.join(result['folder_path'], "message_lint_reports")
        return result
    return func_wrapper


@customize_filename
@customize_folder_path
def customize_output_target(filename: str, folder_path: str):
    return utils.derive_output_target(filename, folder_path)