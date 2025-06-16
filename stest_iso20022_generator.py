import unittest
from iso20022_generator import generate_pacs008_message
import html
import os

LOG_FILE = "pipeline_log.html"

# Initialize the log file if it doesn't exist
if not os.path.exists(LOG_FILE):
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

class TestSystem(unittest.TestCase):
    def test_end_to_end_message(self):
        log_message("\n =================== System Testing Output logs ================ \n")
        log_message("Generating PACS.008 message for Alice to Bob...")
        xml = generate_pacs008_message("Alice", "Bob", 250.00, "USD")

        log_message("Checking if XML starts with declaration...")
        self.assertTrue(xml.startswith(b"<?xml"))

        log_message("Checking if currency USD is present in the XML...")
        self.assertIn(b"USD", xml)

        log_message("System test passed.")

if __name__ == '__main__':
    unittest.main()

    # Close the HTML tags after tests complete
    with open(LOG_FILE, "a") as log_file:
        log_file.write("</pre>\n</body>\n</html>")
