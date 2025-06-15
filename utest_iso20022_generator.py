import unittest
from lxml import etree
from iso20022_generator import generate_pacs008_message

LOG_FILE = "pipeline_log.txt"

def log_message(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")
    print(message)

class MyTestCase(unittest.TestCase):
    def test_generate_pacs008_message(self):
        debtor = "John Dean"
        creditor = "Jane Smith"
        amount = 1000.00
        currency = "EUR"

        log_message("Generating PACS.008 message...")
        xml_output = generate_pacs008_message(debtor, creditor, amount, currency)
        root = etree.fromstring(xml_output)

        log_message("Checking if debtor name is in the XML...")
        self.assertIn(debtor, xml_output.decode())

        log_message("Checking if creditor name is in the XML...")
        self.assertIn(creditor, xml_output.decode())

        log_message("Checking if amount is in the XML...")
        self.assertIn(str(amount), xml_output.decode())

        log_message("Checking if currency attribute is correct...")
        instd_amt = root.find(".//{urn:iso:std:iso:20022:tech:xsd:pacs.008.001.02}InstdAmt")
        self.assertEqual(instd_amt.attrib.get("Ccy"), currency)

        log_message("All checks passed.")

if __name__ == '__main__':
    unittest.main()
