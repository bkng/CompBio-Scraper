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
        css.attrib["href"] = "card.css"
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

        image_results = self._entry.get_picture_url()
        if type(image_results) == type([]):
            for img_url in image_results:
                img = etree.SubElement(body, "img")
                img.attrib["src"] = img_url
        else:
            img = etree.SubElement(body, "img")
            img.attrib["src"] = image_results

        paragraph = etree.SubElement(body, "p")
        if self._entry.get_entry_type() == Entry.VIRUS:
            paragraph.text = "Genome Modifier:{0}".format(self._entry.get_base_count())
        elif self._entry.get_entry_type() == Entry.GENOME:
            paragraph.text = "Genome:{0}".format(self._entry.get_chromosome_count())
        description = etree.SubElement(body, "p")
        description.text = self._entry.get_description()
        return html_root

