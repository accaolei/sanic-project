import os
import loadcf
import logging
config_env = os.environ.get('APPNAME_ENV', 'env')

logger = logging.getLogger(__name__)

BASR_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

loadcf.load(f'{BASE_DIR}/config/{config_env}.json')  # noqa
from loadcf import *  # noqa
