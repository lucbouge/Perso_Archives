import os
import re
from typing import NamedTuple
import datetime
import diskcache as dc


ROOTNAME = "/Volumes/Backup_1_2019_1TB/"

cachename = "Cache/stat.cache"


class File(NamedTuple):
    path: str
    name: str
    size: int
    mod_date: float


def main():
    os.chdir(ROOTNAME)
    with dc.Cache(cachename) as cache:
        process(cache)


def process(cache):
    for (i, (dirpath, dirnames, filenames)) in enumerate(os.walk(".")):
        if i % 1 == 0:
            print(os.path.join(ROOTNAME, dirpath), i)
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if path in cache:
                continue
            stat_info = os.stat(path)
            file = File(
                path=path,
                name=filename,
                size=stat_info.st_size,
                mod_date=stat_info.st_mtime,
            )
            cache[path] = file


main()
