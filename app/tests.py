import unittest

from main import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_search_with_name(self):
        response = self.app.get('/genes/samuel')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_search_with_name_species(self):
        response = self.app.get('/genes/samuel/drosophila_melanogaster')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)


if __name__ == "__main__":
    unittest.main()