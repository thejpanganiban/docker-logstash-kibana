from logging.handlers import SysLogHandler
import logging

logger = logging.getLogger()
logger.addHandler(SysLogHandler(address=('192.168.99.100', 5141)))
logging.warn("Hello world")
