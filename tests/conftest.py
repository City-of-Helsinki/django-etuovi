import os
import shutil

from pytest import fixture


@fixture()
def test_folder():
    temp_file = "tests/temp_files"
    if not os.path.exists(temp_file):
        os.mkdir(temp_file)
    yield temp_file
    shutil.rmtree(temp_file)
