
#Enum for entry type
GENOME, VIRUS = range(2)

class Entry():
    """
    Entry class. Will contain card name, type, payload, and picture.
    name should be name of entry.
    entry_type will be either GENOME or VIRUS constant
    entry_value will be value of the entry, either chromosome count for genomes or base pair addition for viruses
    picture will be a link to the picture to use for the cards
    """

    def __init__(self, name, entry_type, entry_value, picture_url):
        self._name = name
        self._entry_type = entry_type
        self._entry_value = entry_value
        self._picture_url = picture_url

    def get_name(self):
        return self._name

    def get_entry_type(self):
        return self._entry_type

    def get_entry_value(self):
        return self._entry_value

    def get_picture_url(self):
        return self._picture_url

class EntryBuilder():
    """
    Builder pattern class for Entry object.
    """

    def __init__(self):
        """
        Initializes all values to defaults.
        """
        self._name = ""
        self._entry_type = GENOME
        self._entry_value = 0
        self._picture_url = ""

    def set_name(self, name):
        """
        Sets name object.
        """
        self._name = name
        
    def set_entry_type(self, entry_type):
        """
        Sets entry type
        """
        self._entry_type = entry_type;

    def set_entry_value(self, entry_value):
        """
        Sets entry value.
        """
        self._entry_value = entry_value

    def set_picture_url(self, picture_url):
        """
        Sets picture url.
        """
        self._picture_url = picture_url

    def build_entry(self):
        return Entry(self._name, self._entry_type, 
                self._entry_value, self._picture_url)
