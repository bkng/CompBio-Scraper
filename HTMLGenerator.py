import Entry

from lxml import etree


class HTMLGenerator:
    """
    Generates an HTML document styled with CSS for easy printout of the trading cards.
    """

    def __init__(self, entries):
        self._entries = entries

    def get_html(self):
        """
        Returns HTML document for all entires.
        """
        html_root = etree.Element("html")
        css = etree.SubElement(html_root, "link")
        css.attrib["rel"] = "stylesheet"
        css.attrib["href"] = "card.css"
        for entry in self._entries:
            html_root.append(self._get_html_for_entry(entry)
        return html_root

    def _get_html_for_entry(self, entry):
        """
        Returns html document for entry.
        """
        div_root = etree.Element("div")
        body = etree.SubElement(div_root, "body")
        title = etree.SubElement(body, "h1")
        title.text = entry.get_name()
        card_type_element = etree.SubElement(body, "h2")
        card_type = entry.get_entry_type()

        if card_type == Entry.VIRUS:
            card_type_element.text = "VIRUS"
        elif card_type == Entry.GENOME:
            card_type_element.text = "GENOME"

        image_results = entry.get_picture_url()
        if type(image_results) == type([]):
            for img_url in image_results:
                img = etree.SubElement(body, "img")
                img.attrib["src"] = img_url
        else:
            img = etree.SubElement(body, "img")
            img.attrib["src"] = image_results

        paragraph = etree.SubElement(body, "p")
<<<<<<< HEAD
        if entry.get_entry_type() == Entry.VIRUS:
            paragraph.text = "Genome Modifier:{0}".format(entry.get_base_count())
        elif entry.get_entry_type() == Entry.GENOME:
            paragraph.text = "Genome:{0}".format(entry.get_chromosome_count())
=======
        if self._entry.get_entry_type() == Entry.VIRUS:
            paragraph.text = "Genome Modifier (Kilobase Count):{0}".format(self._entry.get_base_count())
        elif self._entry.get_entry_type() == Entry.GENOME:
            paragraph.text = "Genome Score (Chromosome Count):{0}".format(self._entry.get_chromosome_count())
>>>>>>> 58c38cdfaacf3bb4ee48bcacd022d2520c63f502
        description = etree.SubElement(body, "p")
        description.text = entry.get_description()
        return html_root

