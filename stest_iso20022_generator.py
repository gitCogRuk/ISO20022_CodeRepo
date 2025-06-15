import unittest
from iso20022_generator import generate_pacs008_message

class TestSystem(unittest.TestCase):
    def test_end_to_end_message(self):
        xml = generate_pacs008_message("Alice", "Bob", 250.00, "USD")
        self.assertTrue(xml.startswith(b"<?xml"))
        self.assertIn(b"USD", xml)

if __name__ == '__main__':
    unittest.main()
