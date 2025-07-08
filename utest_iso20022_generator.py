import unittest
from lxml import etree
from iso20022_generator import generate_pacs008_message
import html

LOG_FILE = "pipeline_log.html"

# Start the HTML log file with header and styles
with open(LOG_FILE, "w") as log_file:
    log_file.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Pipeline Log</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        pre { background-color: #f4f4f4; padding: 10px; border: 1px solid #ccc; }
    </style>
</head>
<body>
<h1>Pipeline Log</h1>
<pre>
""")

def log_message(message):
    escaped = html.escape(message)
    with open(LOG_FILE, "a") as log_file:
        log_file.write(escaped + "\n")
    print(message)

class MyTestCase(unittest.TestCase):
    def test_generate_pacs008_message(self):
        debtor = "Johnny Dean"
        creditor = "Jane Smith"
        amount = 415.47
        currency = "EUR"
        log_message("=================== Unit Testing Output logs ================ \n")
        log_message("Generating PACS.008 message.....")
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

    # Close the HTML tags after tests complete
    with open(LOG_FILE, "a") as log_file:
        log_file.write("</pre>\n</body>\n</html>")
