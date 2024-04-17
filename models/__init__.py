#!/usr/bin/python3
"""
main module
"""

from os import getenv


all_rep = getenv("HBNB_TYPE_STORAGE")

if all_rep == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
