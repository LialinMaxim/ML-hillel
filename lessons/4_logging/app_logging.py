#!/usr/bin/env python3

# This module created for logging some app.
# It's not used as a separate one module for logging, but from other main modules for myapplication.
# The app process will be stopped in case of logging module initialization failed.

# Logging process include 3(three) logging output source:
# - terminal output (INFO level)
# - into file (DEBUG level, path to log file /var/log/my_app)
# - system log (INFO level, write to debian system log file). Access from System Logs of Management Console page


# The Easy way

# import logging
# #
# LEVEL = 40
# logging.basicConfig(format='%(asctime)s: %(module)s: %(levelname)s: %(message)s', level=LEVEL)
# #
# #
# print('This message should appear on the console')
#
# logging.debug('This message should appear on the console in debug mode')
# logging.info('This message should appear on the console in INFO mode')
# logging.warning('My App warning')
# logging.critical('My App Critical message')
#
#
# logging.info('So should this')
#
#
# if logging.INFO > LEVEL:
#     print('So should this')


import logging
import logging.handlers
import os
import sys
import string
import random


class Logger:
    """
    Class for configure logging module with DEBUG level for logfile and INFO level for user output
    """
    LOG_DIR = '/var/log/my_app'  # Folder for master and agent log file
    LOG_FILENAME = 'MyApplication'  # Log file name
    LOG_NAME = 'MyApp'  # Log name
    MAX_LOG_SIZE = 10 * 1024  # Log file maximum size (10Kb)
    ROTATING_COUNT = 10  # Maximum log files count for rotating
    SD_MP_ERR = "/var/log/my_app' not found!"

    def __init__(self, filename=LOG_FILENAME):
        """ Set logging handlers for all output sources """
        self.logger = logging.getLogger(self.LOG_NAME)
        self.set_logging_stream()
        self.set_debian_system_log()
        self.logger.exception = self.exception
        self.set_logging_file(filename)

    def set_logging_file(self, filename):

        """ Set logging handler for writing debug level data to file """
        self.check_logfile_path()
        self.LOG_FILE = os.path.join(self.LOG_DIR, "{}.log".format(filename.lower()))

        file_formatter = logging.Formatter('%(asctime)s: %(threadName)s: %(module)s: %(levelname)s: %(message)s')
        self.file_handler = logging.handlers.RotatingFileHandler(self.LOG_FILE, maxBytes=self.MAX_LOG_SIZE,
                                                                 backupCount=self.ROTATING_COUNT)
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(file_formatter)
        self.logger.addHandler(self.file_handler)

    def set_logging_stream(self):
        # logging.basicConfig(format='%(asctime)s: %(module)s: %(levelname)s: %(message)s', level=LEVEL)
        """ Set logging handler for writing info level data to terminal """
        stream_formatter = logging.Formatter('%(asctime)s: %(message)s', '%H:%M:%S') # %d/%m/%Y
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.DEBUG)
        self.stream_handler.setFormatter(stream_formatter)
        self.logger.addHandler(self.stream_handler)

    def set_debian_system_log(self):
        """ Set logging handler for writing info level data to terminal/console"""
        syslog_formater = logging.Formatter(f'%(levelname)s: {self.LOG_NAME}: %(message)s')
        self.syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
        self.syslog_handler.setLevel(logging.DEBUG)
        self.syslog_handler.setFormatter(syslog_formater)
        self.logger.addHandler(self.syslog_handler)

    def check_logfile_path(self):
        """ Check for requested log file directory exists.
         Raise FileNotFoundError if no parent directory(avid/mnt/system directory(mount point)) not exists,
         Creating 'log' directory if it does not exist and possible to create """
        parrent_logdir = os.path.dirname(self.LOG_DIR)
        if not os.path.exists(parrent_logdir):
            logging.critical('No such directory: "{}"'.format(parrent_logdir))
            logging.critical(self.SD_MP_ERR)
            raise FileNotFoundError('No such directory: "{}"'.format(parrent_logdir))
        if not os.path.exists(self.LOG_DIR):
            os.mkdir(self.LOG_DIR)

    def syslog_off(self):
        """ Turn off logging to debian system journal """
        self.logger.removeHandler(self.syslog_handler)

    def __getattr__(self, item):
        """
        :return: logger.item if logging.item else self.item
        """
        try:
            return self.logger.__getattribute__(item)
        except AttributeError:
            return self.__getattribute__(item)

    def exception(self, msg, *args, **kwargs):
        """
        Convenience method for logging an DEBUG with exception information.
        Changed logging.exception method from ERROR to DEBUG level.
        Use this method for writing to exception to file.
        """
        kwargs['exc_info'] = True
        self.logger.debug(msg, *args, **kwargs)


try:
    log = Logger()
    log.debug('This message should appear on the console in debug mode')
    log.info('This message should appear on the console in INFO mode')
    log.warning('My App warning')
    log.critical('My App Critical message')

    while True:
        log.warning("_".join(random.sample(string.ascii_lowercase, 15)))

except FileNotFoundError:
    log.critical('My App Critical message. File/Directory not Found')
    sys.exit(1)

