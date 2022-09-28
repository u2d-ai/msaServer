# -*- encoding: utf-8 -*-
import os

from loguru import logger
ROOTPATH = os.path.join(os.path.dirname(__file__))

if __name__ == "__main__":
    from msaServer import base

    logger.info("Starting Services...")
    base.run(app_dir=ROOTPATH)
