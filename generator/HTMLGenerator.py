from lxml impoer etree

class HTMLGenerator:
    """
    Generates an HTML document styled with CSS for easy printout of the trading cards.
    """

    def __init__(self, entry):
        self._entry = entry

    def get_div(self):
        div_root = etree.Element("div")
        div_root.attrib["name"] = self._entry.get_name()
        head = etree.SubElement(div_root, "head")
        title = etree.SubElement(head, "title")
        title.text = self._entry.get_name()
        body = etree.SubElement(div_root, "body")
        img = etree.SubElement(body, "img")
        img.attrib["src"] = self._entry.get_picture_url()
        if self._entry.get_entry_type() == VIRUS:
            body.text = "Genome Modifier:{0}".format(self._entry.get_entry_value())
        elif self._entry.get_entry_type() == GENOME:
            body.text = "Genome:{0}".format(self._entry.get_entry_value())
        return div_root

