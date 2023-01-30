import logging


class Logger:
    def __init__(self):
        self._verbose = False

    def log_info(self, text: str):
        pass

    @property
    def verbose(self):
        return self._verbose

    @verbose.setter
    def verbose(self):
        pass

    @staticmethod
    def get(verbose=False):
        if verbose:
            return AppLogger()
        else:
            return NullLogger()


class AppLogger(Logger):
    def __init__(self):
        self._verbose = True
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            datefmt="%Y-%m-%d %H:%M:%S",
            filename='message_lint.log', level=logging.INFO)

    def log_info(self, text: str):
        logging.info(text)


class NullLogger(Logger):
    def __init__(self):
        pass
