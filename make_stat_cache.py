import os
import re
from typing import NamedTuple
import datetime
import diskcache as dc
import argparse


ROOTNAME = "/nfs/nas4.irisa.fr/temp_transfert/bouge/Sauvegarde_OVH_2022-04-21/"

cachename = "Cache/stat.cache"


class File(NamedTuple):
    path: str
    name: str
    size: int
    mod_date: float


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=str,
        dest="initial_dirname",
    )
    args = parser.parse_args()
    return args


def main():
    os.chdir(ROOTNAME)
    with dc.Cache(cachename) as cache:
        process(cache)


def process(cache):
    args = parse()
    initial_dirname = args.initial_dirname
    print(f"Starting from {initial_dirname}\n\n")
    for (i, (dirpath, dirnames, filenames)) in enumerate(os.walk(initial_dirname)):
        if i % 100 == 0:
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
