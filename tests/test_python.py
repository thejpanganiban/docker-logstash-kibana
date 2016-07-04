from logging.handlers import SysLogHandler
import logging

logger = logging.getLogger()
logger.addHandler(SysLogHandler(address=('54.169.175.36', 5141)))
logging.warn("Hello world")
