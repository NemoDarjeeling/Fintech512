import unittest
import sys
import io
import kwic

class TestKeywords(unittest.TestCase):
    def test_standard(self):
        # Test input
        test_input = "the\na\nand\n::descent of man\nthe ascent of man\nthe old man and the sea\na portrait of the artist as a young man\na man is a man but bubblesort is a dog"
        # Expected output
        expected_output = "a portrait of the ARTIST as a young man\nthe ASCENT of man\na man is a man but BUBBLESORT is a dog\nDESCENT of man\na man is a man but bubblesort is a DOG\ndescent of MAN\nthe ascent of MAN\nthe old MAN and the sea\na portrait of the artist as a young MAN\na MAN is a man but bubblesort is a dog\na man is a MAN but bubblesort is a dog\nthe OLD man and the sea\na PORTRAIT of the artist as a young man\nthe old man and the SEA\na portrait of the artist as a YOUNG man"

        # redirect stdin
        sys.stdin = io.StringIO(test_input)
        # capture stdout
        sys.stdout = io.StringIO()
        # run the code
        kwic.main()

        # get stdout
        output = sys.stdout.getvalue()
        # compare stdout and expected output
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()


