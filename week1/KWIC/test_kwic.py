import unittest
import sys
import io
import kwic

#unittest has to work with a function that "returns" sth.
class TestKeywords(unittest.TestCase):
    def test_std_input(self):
        # Test input
        test_input = "is\nthe\nof\nand\nas\na\nbut\n::\nDescent of Man\nThe Ascent of Man\nThe Old Man and The Sea\nA Portrait of The Artist As a Young Man\nA Man is a Man but Bubblesort IS A DOG"
        # Expected output
        expected_output = "a portrait of the ARTIST as a young man\nthe ASCENT of man\na man is a man but BUBBLESORT is a dog\nDESCENT of man\na man is a man but bubblesort is a DOG\ndescent of MAN\nthe ascent of MAN\nthe old MAN and the sea\na portrait of the artist as a young MAN\na MAN is a man but bubblesort is a dog\na man is a MAN but bubblesort is a dog\nthe OLD man and the sea\na PORTRAIT of the artist as a young man\nthe old man and the SEA\na portrait of the artist as a YOUNG man"

        # redirect stdin
        sys.stdin = io.StringIO(test_input)
        test_output = kwic.main()

        self.assertEqual(test_output, expected_output)

    def test_no_keyword(self):
        test_input = "is\nthe\nof\n::\nis the of\nof the is\nthe is of"
        expected_output = ""
        sys.stdin = io.StringIO(test_input)
        test_output = kwic.main()
        self.assertEqual(test_output, expected_output)        

    def test_all_keyword(self):
        test_input = "a\nb\n::\nHello Python World"
        expected_output = "HELLO python world\nhello PYTHON world\nhello python WORLD"
        sys.stdin = io.StringIO(test_input)
        test_output = kwic.main()
        self.assertEqual(test_output, expected_output)

    def test_WTI_uppercase(self):
        test_input = "Is\nThe\nOf\n::\nDescent of Man"
        expected_output = "DESCENT of man\ndescent of MAN"
        sys.stdin = io.StringIO(test_input)
        test_output = kwic.main()
        self.assertEqual(test_output, expected_output) 

    def test_no_WTI_title(self):
        with self.assertRaises(ValueError):
            test_input = "Descent of Man\nThe Ascent of Man\nThe Old Man and The Sea\nA Portrait of The Artist As a Young Man\nA Man is a Man but Bubblesort IS A DOG"
            sys.stdin = io.StringIO(test_input)
            test_output = kwic.main()
    
    def test_empty_input(self):
        with self.assertRaises(ValueError):
            test_input = ""
            sys.stdin = io.StringIO(test_input)
            test_output = kwic.main()

if __name__ == '__main__':
    unittest.main(verbosity = 2)

#5 hours for this
