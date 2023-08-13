import unittest
import tempfile
import os
from main import find_files_googleoauth2

class TestFindFilesGoogleOAuth2(unittest.TestCase):
    """
    Test class for find_files_googleoauth2 function.
    """
    def setUp(self):
        """
        Set up temporary directory and file paths for testing.
        """
        self.test_dir = tempfile.mkdtemp()
        self.fake_file_path = os.path.join(self.test_dir, "fake_file.py")
        self.real_file_path = os.path.join(self.test_dir, "real_file.py")

    def tearDown(self):
        """
        Clean up temporary directory after each test.
        """
        os.rmdir(self.test_dir)

    def create_fake_file(self, content):
        """
        Create a fake file with the given content.
        """
        with open(self.fake_file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def test_no_files_with_google_oauth2(self):
        """
        Test that no files with google.oauth2 imports are found.
        """
        self.create_fake_file("import requests\nprint('Testing')\n") #could be customized
        files_with_oauth2 = find_files_googleoauth2(self.test_dir)
        self.assertEqual(len(files_with_oauth2), 0)

    def test_files_with_google_oauth2(self):
        """
        Test that files with google.oauth2 imports are correctly found.
        """
        self.create_fake_file("import google.oauth2\nprint('Using google.oauth2')\n")
        self.create_fake_file("import google.auth\nprint('Using google.auth')\n")
        files_with_oauth2 = find_files_googleoauth2(self.test_dir)
        self.assertEqual(len(files_with_oauth2), 1)
        self.assertEqual(files_with_oauth2[0], self.fake_file_path)

if __name__ == '__main__':
    unittest.main()
