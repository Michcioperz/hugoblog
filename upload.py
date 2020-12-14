#!/usr/bin/env python3
import hashlib
from pathlib import Path

import requests

with open("en.key") as f:
    en_key = f.read().strip()
with open("pl.key") as f:
    pl_key = f.read().strip()

def upload(key: str, root: Path):
    print("starting", root)
    auth_headers = {"Authorization": f"Bearer {key}"}
    r = requests.get("https://neocities.org/api/list", headers=auth_headers)
    r.raise_for_status()
    sums = {x["path"]: x["sha1_hash"].lower() for x in r.json()["files"] if "sha1_hash" in x and not x["is_directory"]}
    def hash_path(p: Path) -> str:
        m = hashlib.sha1()
        m.update(p.read_bytes())
        return m.hexdigest().lower()
    changed = {p for p in root.rglob("*") if p.is_file() and hash_path(p) != sums.get(str(p.relative_to(root)))}
    def folder(it, files):
        try:
            p = next(it)
        except StopIteration:
            return requests.post("https://neocities.org/api/upload", headers=auth_headers, files=files)
        print(p)
        stripped = str(p.relative_to(root))
        with p.open("rb") as f:
            files.append((stripped, (stripped, f, "application/octet-stream")))
            return folder(it, files)

    if changed:
        r = folder(iter(changed), [])
        print(r)
        print(r.text)
        r.raise_for_status()


upload(en_key, Path("public/en"))
upload(pl_key, Path("public/pl"))
