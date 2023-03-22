"""
An example of using dcompressee to decompress files in an asynchronous manner.
"""

import asyncio
import pathlib
import os
import time
from dcompressee import unpack


async def read_files(file_paths):
    """
    Read files asynchronously
    """
    tasks = []
    for file_path in file_paths:
        tasks.append(asyncio.create_task(read_file(file_path)))
    await asyncio.gather(*tasks)


async def read_file(file_path: pathlib.Path):
    """
    Read a file asynchronously
    """
    # Unpack the file if it's compressed
    unpacked_file_path = await asyncio.to_thread(unpack, file_path)

    # Read the contents of the file
    with open(
        unpacked_file_path, "r", encoding="utf8"
    ) as f:  # pylint disable=invalid-name
        contents = f.read()

    # Print the contents of the file
    print(contents)


async def main():
    """
    Main function
    """
    path = os.path.dirname(os.path.abspath(__file__))
    files_uncmp = os.path.join(path, "example_Seq0000.fasta")
    files_gz = [os.path.join(path, f"example_Seq000{i}.fasta.gz") for i in range(1, 5)]
    files_lz4 = [
        os.path.join(path, f"example_Seq000{i}.fasta.lz4") for i in range(5, 9)
    ]
    files_bz2 = os.path.join(path, "example_Seq0009.fasta.bz2")
    files = [
        pathlib.Path(p) for p in [files_uncmp] + files_gz + files_lz4 + [files_bz2]
    ]
    now = time.perf_counter()
    await read_files(files)
    print(f"Time taken: {time.perf_counter() - now}")


if __name__ == "__main__":
    asyncio.run(main())
