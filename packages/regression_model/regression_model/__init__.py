import logging

from regression_model.config import config
from regression_model.config import logging_config


VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'

with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip() 