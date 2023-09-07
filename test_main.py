import unittest
from main import find_files_googleoauth2

class TestFindFilesGoogleOAuth2(unittest.TestCase):
    def test_find_google_oauth2_files(self):

        test_directory = "/Users/jadenlaborete/PycharmProjects/storyline"

        # Call the function to find files
        google_oauth2_files = find_files_googleoauth2(test_directory)

        expected_files = [

            '/Users/jadenlaborete/PycharmProjects/storyline/main.py',
            '/Users/jadenlaborete/PycharmProjects/storyline/test_main.py',
            '/Users/jadenlaborete/PycharmProjects/storyline/testFiles/file1.py',
            '/Users/jadenlaborete/PycharmProjects/storyline/testFiles/testDirectory/file2.py',

        ]

        # Assert that the function returns the expected list of files
        self.assertEqual(google_oauth2_files, expected_files)

    def test_find_unexpected_files(self):
        # Provide a test directory
        test_directory = "/Users/jadenlaborete/PycharmProjects/storyline"


        unexpected_files = find_files_googleoauth2(test_directory)

        # Define a list of files that should NOT contain 'google.oauth2'
        unexpected_files_should_not_contain = [

            '/Users/jadenlaborete/PycharmProjects/storyline/testFiles/testDirectory2/file3.py'

        ]


        for file_path in unexpected_files_should_not_contain:
            self.assertNotIn(file_path, unexpected_files)

if __name__ == '__main__':
    unittest.main()
