# -*- coding: utf-8 -*-

import os
from typing import Union, Optional

from msaServer.srv_gunicorn import MSAServerGunicorn
from msaServer.srv_uvicorn import MSAServerUvicorn

if __name__ == "__main__":
    pass

ROOTPATH = os.path.join(os.path.dirname(__file__))
server_runner: Optional[Union[MSAServerUvicorn, MSAServerGunicorn]] = None
"""The created server instance"""


def run(app_dir: str, app: str = "app:app", host: str = "127.0.0.1", port: int = 8090,
        server_type: str = "uvicorn"):
    """Creates and starts a MSAServer Instance

    Args:
        app_dir: The rootpath of your project, like: os.path.join(os.path.dirname(__file__))
        app: The module:application string, like 'app:app' or 'main:app'
        host: IP/FQDN the server runs on
        port: The port the server binds and listen to
        server_type: The string for the server type to use 'uvicorn', everything else starts a Gunicorn Server

    """
    global server_runner
    if not app_dir or len(app_dir) < 1:
        app_dir = ROOTPATH
        print("WARNING: msaServer.app_dir is None or empty, using ROOTPATH:", ROOTPATH)

    if server_type.__eq__("uvicorn"):
        server_runner = MSAServerUvicorn(
            app=app, app_dir=app_dir, host=host, port=port
        )
    else:
        server_runner = MSAServerGunicorn(
            app=app, app_dir=app_dir, host=host, port=port
        )

    if server_runner:
        server_runner.run()
    else:
        print("ERROR: msaServer.server_runner is None and not initialized")
