"""
Test the dcompressee module.
"""

import dcompressee


def test_no_compression(non_compressed_file):
    """Test that a non-compressed file is not decompressed."""
    path = dcompressee.unpack(non_compressed_file)
    assert path.read_text(encoding="utf8") == "hello world."
    assert dcompressee.unpack(non_compressed_file) == non_compressed_file


def test_gzip(gzip_file):
    """Test that a gzip compressed file is decompressed."""
    path = dcompressee.unpack(gzip_file)
    print(path)
    assert path.read_text(encoding="utf8") == "hello world."
    assert dcompressee.unpack(gzip_file) != gzip_file


def test_bzip2(bzip2_file):
    """Test that a bzip2 compressed file is decompressed."""
    path = dcompressee.unpack(bzip2_file)
    assert path.read_text(encoding="utf8") == "hello world."
    assert dcompressee.unpack(bzip2_file) != bzip2_file


def test_lz4(lz4_file):
    """Test that a lz4 compressed file is decompressed."""
    path = dcompressee.unpack(lz4_file)
    assert path.read_text(encoding="utf8") == "hello world."
    assert dcompressee.unpack(lz4_file) != lz4_file


def test_xz(xz_file):
    """Test that a xz compressed file is decompressed."""
    path = dcompressee.unpack(xz_file)
    assert path.read_text(encoding="utf8") == "hello world."
    assert dcompressee.unpack(xz_file) != xz_file
