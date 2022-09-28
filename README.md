<p align="center">
  <img src="http://logos.u2d.ai/msaServer_logo.png?raw=true" alt="msaServer Logo"/>
</p>

------
<p align="center">
    <em>msaServer - Helper & Wrapper around Uvicorn/Gunicorn for FastAPI based apps</em>
<br>
    Optimized for use with FastAPI/Pydantic.
<br>
  <a href="https://pypi.org/project/msaServer" target="_blank">
      <img src="https://img.shields.io/pypi/v/msaServer?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypi.org/project/msaServer" target="_blank">
      <img src="https://img.shields.io/pypi/pyversions/msaServer.svg?color=%2334D058" alt="Supported Python versions">
  </a>
</p>

------

**Documentation**: <a href="https://msaServer.u2d.ai/" target="_blank">msaServer Documentation (https://msaServer.u2d.ai/)</a>

------

## Features
- **Uvicorn Wrapper**: MSAServerUvicorn.
- **Gunicorn Wrapper**: MSAServerGunicorn.

## Main Dependencies

- **gunicorn~=20.1.0**: WSGI HTTP Server for UNIX
- **uvicorn~=0.18.3**: The lightning-fast ASGI server.


## License Agreement

- `msaServer`Based on `MIT` open source and free to use, it is free for commercial use, but please show/list the copyright information about msaServer somewhere.


## How to create the documentation

We use mkdocs and mkdocsstring. The code reference and nav entry get's created virtually by the triggered python script /docs/gen_ref_pages.py while ``mkdocs`` ``serve`` or ``build`` is executed.

### Requirements Install for the PDF creation option:
PDF Export is using mainly weasyprint, if you get some errors here pls. check there documentation. Installation is part of the msaServer, so this should be fine.

We can now test and view our documentation using:

    mkdocs serve

Build static Site:

    mkdocs build


## Build and Publish
  
Build:  

    python setup.py sdist

Publish to pypi:

    twine upload dist/*
