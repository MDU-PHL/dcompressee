"""
Configure test fixtures for pytest.
"""

import pytest


@pytest.fixture
def non_compressed_file(request):
    """Return the path to a non-compressed file."""
    return request.path.parent.joinpath("data", "hello_world.txt")


@pytest.fixture
def gzip_file(request):
    """Return the path to a gzip compressed file."""
    return request.path.parent.joinpath("data", "hello_world.txt.gz")


@pytest.fixture
def bzip2_file(request):
    """Return the path to a bzip2 compressed file."""
    return request.path.parent.joinpath("data", "hello_world.txt.bz2")


@pytest.fixture
def lz4_file(request):
    """Return the path to a lz4 compressed file."""
    return request.path.parent.joinpath("data", "hello_world.txt.lz4")


@pytest.fixture
def xz_file(request):
    """Return the path to a xz compressed file."""
    return request.path.parent.joinpath("data", "hello_world.txt.xz")
