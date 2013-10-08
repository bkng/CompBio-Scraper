import unittest

from lxml import etree
from Entry import Entry, EntryBuilder, GENOME, VIRUS
from HTMLGenerator import HTMLGenerator

class HTMLGeneratorTest(unittest.TestCase):
    """
    Class unit tests HTML generator to ensure it outputs
    correctly.
    """
    
    def setUp(self):
        """
        Sets up entries for testing
        """
        entry1_builder = EntryBuilder()
        entry1_builder.set_name("Test1")
        entry1_builder.set_entry_type(GENOME)
        entry1_builder.set_chromosome_count(34)
        entry1_builder.set_picture_url("image1_location")
        self._entry1 = entry1_builder.build_entry()
        entry2_builder = EntryBuilder()
        entry2_builder.set_name("Test2")
        entry2_builder.set_entry_type(VIRUS)
        entry2_builder.set_base_count(-3)
        entry2_builder.set_picture_url("image2_location")
        self._entry2 = entry2_builder.build_entry()


    def test_html_generation(self):
        """
        Tests that xhtml output matches for correct objects.
        """
        first_generator = HTMLGenerator(self._entry1)
        second_generator = HTMLGenerator(self._entry2)
        first_html = first_generator.get_html()
        second_html = second_generator.get_html()
        first_example = etree.parse("test_data/test_entry1.html")
        second_example = etree.parse("test_data/test_entry2.html")
        first_string = "".join(etree.tostring(first_html).split())
        test_string = "".join(etree.tostring(first_example).split())
        second_string = "".join(etree.tostring(second_html).split())
        second_test_string = "".join(etree.tostring(second_example).split())
        self.assertEqual(first_string, test_string)
        self.assertEqual(second_string, second_test_string)

if __name__ == "__main__":
    unittest.main()
