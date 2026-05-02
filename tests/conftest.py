import os
import stat
import tempfile

import pytest


@pytest.fixture
def writeonly_file():
    """
    Create a write-only file for testing.

    Yields:
        str: The path to the write-only file.
    """
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
        file.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")
    os.chmod(file.name, stat.S_IWRITE)
    yield file.name
    os.unlink(file.name)
