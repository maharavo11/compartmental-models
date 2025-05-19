from utilities import custom_install_cmdstan
custom_install_cmdstan()

# Load packages used in this installation
import os
import json
import shutil
import urllib.request

from cmdstanpy import CmdStanModel

import logging

cmdstanpy_logger = logging.getLogger("cmdstanpy")
cmdstanpy_logger.disabled = True
