import logging
from logging import LogRecord
from logging.handlers import TimedRotatingFileHandler


class LoggerConfig:
    """Configure logging to display logs in terminal with showing the time, code line number, file name"""

    @staticmethod
    def setup_logging():
        """Setup logging configuration"""
        logging.basicConfig(
            format="%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO,
        )

        # Set up file handler
        file_handler = TimedRotatingFileHandler(
            filename="logs/langchain.log", when="D", interval=1, backupCount=30
        )
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s"
        )
        file_handler.setFormatter(formatter)

        # Add file handler to root logger
        logging.getLogger().addHandler(file_handler)

        # Set up logging to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            "%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s"
        )
        console_handler.setFormatter(console_formatter)

        # Add console handler to root logger
        logger = logging.getLogger()
        logger.addHandler(console_handler)
        return logger

    @staticmethod
    def get_logger():
        return logging.getLogger()
    
    @staticmethod
    def get_record_extra(record: LogRecord) -> dict:
        """Get extra information from LogRecord"""
        return {
        "file_name": record.filename,
        "line_number": record.lineno,
        "function_name": record.funcName,
    }
    
