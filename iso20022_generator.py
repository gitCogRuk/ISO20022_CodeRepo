from lxml import etree

def generate_pacs008_message(debtor_name, creditor_name, amount, currency="EUR"):
    root = etree.Element("Document", xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.02")
    fi_to_fi = etree.SubElement(root, "FIToFICstmrCdtTrf")
    cdt_trf_tx_inf = etree.SubElement(fi_to_fi, "CdtTrfTxInf")

    pmt_id = etree.SubElement(cdt_trf_tx_inf, "PmtId")
    etree.SubElement(pmt_id, "EndToEndId").text = "E2E123456789"

    amt = etree.SubElement(cdt_trf_tx_inf, "Amt")
    instd_amt = etree.SubElement(amt, "InstdAmt", Ccy=currency)
    instd_amt.text = str(amount)

    cdtr = etree.SubElement(cdt_trf_tx_inf, "Cdtr")
    etree.SubElement(cdtr, "Nm").text = creditor_name

    dbtr = etree.SubElement(cdt_trf_tx_inf, "Dbtr")
    etree.SubElement(dbtr, "Nm").text = debtor_name

    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")
