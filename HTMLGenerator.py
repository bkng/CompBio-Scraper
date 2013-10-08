import Entry

from lxml import etree


class HTMLGenerator:
    """
    Generates an HTML document styled with CSS for easy printout of the trading cards.
    """

    def __init__(self, entry):
        self._entry = entry

    def get_html(self):
        """
        Returns html document for entry.
        """
        html_root = etree.Element("html")
        css = etree.SubElement(html_root, "link")
        css.attrib["rel"] = "stylesheet"
        css.attrib["href"] = "../card.css"
        div_root = etree.SubElement(html_root, "div")
        body = etree.SubElement(div_root, "body")
        title = etree.SubElement(body, "h1")
        title.text = self._entry.get_name()
        card_type_element = etree.SubElement(body, "h2")
        card_type = self._entry.get_entry_type()
        if card_type == Entry.VIRUS:
            card_type_element.text = "VIRUS"
        elif card_type == Entry.GENOME:
            card_type_element.text = "GENOME"
        img = etree.SubElement(body, "img")
        paragraph = etree.SubElement(body, "p")
        img.attrib["src"] = self._entry.get_picture_url()
        if self._entry.get_entry_type() == Entry.VIRUS:
            paragraph.text = "Genome Modifier:{0}".format(self._entry.get_entry_value())
        elif self._entry.get_entry_type() == Entry.GENOME:
            paragraph.text = "Genome:{0}".format(self._entry.get_entry_value())
        return html_root

