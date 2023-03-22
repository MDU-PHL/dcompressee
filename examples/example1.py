"""
Example demonstrating the use of dcompressee
"""

import os
import pathlib
import time
import dcompressee


# get path to local file
path = os.path.dirname(os.path.abspath(__file__))
files_uncmp = os.path.join(path, "example_Seq0000.fasta")
files_gz = [os.path.join(path, f"example_Seq000{i}.fasta.gz") for i in range(1, 5)]
files_lz4 = [os.path.join(path, f"example_Seq000{i}.fasta.lz4") for i in range(5, 9)]
files_bz2 = os.path.join(path, "example_Seq0009.fasta.bz2")
files = [pathlib.Path(p) for p in [files_uncmp] + files_gz + files_lz4 + [files_bz2]]

now = time.perf_counter()

for f in files:
    # unpack file
    unpacked = dcompressee.unpack(f)
    # do something with unpacked file
    print(f"Unpacked file: {unpacked}")
    print(unpacked.read_text(encoding="utf8"))

print(f"Time taken: {time.perf_counter() - now}")
