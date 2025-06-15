import unittest
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from lxml import etree
from iso20022_generator import generate_pacs008_message

class MyTestCase(unittest.TestCase):
    def test_generate_pacs008_message(self):
        debtor = "John Dean"
        creditor = "Jane Smith"
        amount = 1000.00
        currency = "EUR"

        xml_output = generate_pacs008_message(debtor, creditor, amount, currency)
        root = etree.fromstring(xml_output)

        # Check if debtor name is in the XML
        self.assertIn(debtor, xml_output.decode())
        # Check if creditor name is in the XML
        self.assertIn(creditor, xml_output.decode())
        # Check if amount is in the XML
        self.assertIn(str(amount), xml_output.decode())
        # Check if currency attribute is correct
        instd_amt = root.find(".//{urn:iso:std:iso:20022:tech:xsd:pacs.008.001.02}InstdAmt")
        self.assertEqual(instd_amt.attrib.get("Ccy"), currency)
=======
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd
=======
>>>>>>> cdcf208f1c8b9b2e66a0d562b0345cfc43b17acd

if __name__ == '__main__':
    unittest.main()
