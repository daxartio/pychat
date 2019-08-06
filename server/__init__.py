import logging.config
import os

import yaml

with open('{}/logging_config.yaml'.format(os.path.dirname(__file__)), 'r') as __file:
    logging.config.dictConfig(yaml.load(__file.read(), Loader=yaml.FullLoader))

logger = logging.getLogger(__name__)
