import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import BinaryIO

import pytest


class TestFiles(unittest.TestCase):
    def setUp(self):
        # Prepare dependencies for the test.
        # Dependencies can be anything: plain objects, files, connections...
        self.some_file = open("01_junit.py", "r")
        self.temp_directory = TemporaryDirectory()

    def tearDown(self):
        # Clean up all the dependencies in order.
        self.temp_directory.cleanup()
        self.some_file.close()

    def test_gzip_file(self):
        subprocess.run(
            "gzip > output.gz",
            cwd=self.temp_directory.name,
            stdin=self.some_file,
            shell=True,
        )
        new_file: Path = Path(self.temp_directory.name) / "output.gz"
        assert new_file.exists()
        assert file_type(new_file) == "application/gzip; charset=binary"


def file_type(path: Path) -> str:
    cmd = ["file", "-ib", path]
    proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, encoding="ascii")
    return proc.stdout.strip()


# with pytest:


def test_gzip_file(some_file: BinaryIO, temp_directory: Path):
    subprocess.run(
        "gzip > output.gz", cwd=str(temp_directory), stdin=some_file, shell=True
    )
    new_file: Path = temp_directory / "output.gz"
    assert new_file.exists()
    assert file_type(new_file) == "application/gzip; charset=binary"


@pytest.fixture
def some_file() -> BinaryIO:
    with open("01_junit.py", "r") as f:
        yield f


@pytest.fixture
def temp_directory() -> Path:
    with TemporaryDirectory() as tempdir:
        yield Path(tempdir)
