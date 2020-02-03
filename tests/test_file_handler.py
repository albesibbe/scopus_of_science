from scopus_of_science.file_handler import File_Handler
import pytest

class Test_File_Handler:
    def test_nofile(self):
        with pytest.raises(TypeError):
            File_Handler()

    def test_inputs(self):
        pass