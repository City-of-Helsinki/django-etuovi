import shutil

from pytest import fixture


@fixture()
def test_folder(tmp_path):
    temp_file = tmp_path / "temp_files"
    temp_file.mkdir()
    yield temp_file
    shutil.rmtree(temp_file)
