import logging
import os
import tempfile


log = logging.getLogger("tsheets_logger")
log.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(levelname)-6s %(message)s")

# Log to file
filehandler = logging.FileHandler(
    os.path.join(tempfile.gettempdir(), "tsheets-log.txt"),
    "w")
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)
log.addHandler(filehandler)
