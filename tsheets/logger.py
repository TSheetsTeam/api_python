import logging
log = logging.getLogger("tsheets_logger")
log.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(levelname)-6s %(message)s")

# Log to file
filehandler = logging.FileHandler("/tmp/log.txt", "w")
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)
log.addHandler(filehandler)
