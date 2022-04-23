import os
import re
from typing import NamedTuple
import datetime
import diskcache as dc
import argparse


ROOTNAME = "/nfs/nas4.irisa.fr/temp_transfert/bouge/Sauvegarde_OVH_2022-04-21/"

cachepath = "/udd/bouge/Perso_Archives/Cache/make_stat_cache.dc"


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
        dest="root",
    )
    parser.add_argument(
        "--action",
        type=str,
        dest="action",
    )
    args = parser.parse_args()
    return args


def main():
    os.chdir(ROOTNAME)
    print(f"Cache: {cachepath}")
    with dc.Cache(cachepath, size_limit=int(400e9)) as cache:
        process(cache)


def process(cache):
    args = parse()
    root = args.root
    print(f"Starting from {root}\n\n")
    action = args.action
    assert action in ("scan", "delete")
    if action == "scan":
        process_scan(cache=cache, root=root)
    if action == "delete":
        process_delete(cache=cache, root=root)
    assert AssertionError("Unexpected action")


################################################################################


def process_delete(*, cache=None, root=None):
    assert cache is not None
    assert root is not None
    key_to_file_dict = dict()
    for path in cache:
        file = cache[path]
        name = file.name
        size = file.size
        mod_date = file.mod_date
        path = file.path
        key = (name, size, mod_date)
        if key not in key_to_file_dict:
            key_to_file_dict[key] = file
            continue
        old_file = key_to_file_dict[key]
        assert old_file.name == file.name
        assert old_file.size == file.size
        assert old_file.mod_time == file.mod_time
        print(f"{file.path} ==> {old_file.path}")


################################################################################


def process_scan(*, cache=None, root=None):
    assert cache is not None
    assert root is not None
    for (i, (dirpath, dirnames, filenames)) in enumerate(os.walk(root)):
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
