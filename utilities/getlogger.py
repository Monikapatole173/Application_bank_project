import datetime
import logging
from pathlib import Path

class GetLogger:
    @staticmethod
    def get_filename():
        now = datetime.datetime.today().strftime("%Y_%m_%d")
        file_name = "app_" + str(now) + ".log"
        file_path = Path(f".\\Logs\\{file_name}")
        if not file_path.exists() :
            file_path.touch()
            final_name = file_name
        else:
            final_name = file_name
        return final_name

    @staticmethod
    def get_logger():
        log_file = logging.FileHandler(f".\\Logs\\{GetLogger.get_filename()}")
        log_format= logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s")
        log_file.setFormatter(log_format)
        logger = logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger