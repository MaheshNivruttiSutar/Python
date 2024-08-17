#Logging & Log Levels:
'''
-Logging is a very useful tool in a programmer's toolbox. It can help you develop a better understanding of the
flow of a program and discover scenarios that you might not even have thought of while developing.

Log Level:
            - DEBUG
            - INFO
            - WARNING
            - ERROR
            - CRITICAL
'''
'''
import logging
logging.basicConfig(filename="C://Drivers//SeleniumLogs//test.log")

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

'''
'''
import logging
logging.basicConfig(filename="C://Drivers//SeleniumLogs//test.log",
format='%(asctime)s: %(levelname)s: %(message)s',
level=logging.DEBUG
)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")'''
'''
import logging
logging.basicConfig(filename="C://Drivers//SeleniumLogs//test.log",
level=logging.DEBUG
)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")'''

import logging

logging.basicConfig(filename="C://Drivers//SeleniumLogs//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")