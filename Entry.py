
#Enum for entry type
GENOME, VIRUS = range(2)

class Entry():
    """
    Entry class. Will contain card name, description, type, payload, and picture.
	
    name 					scientific name of the organism
	description 			description of the organism
    type 					GENOME or VIRUS constant
    chromosome_count		number of chromosomes in the organism's genome
	base_count				number of bases in the organism's genome
    picture_url				URL of the picture to use for the cards
    """

    def __init__(self, name, description, entry_type, chromosome_count, base_count, picture_url):
        self._name = name
        self._description = description
        self._entry_type = entry_type
        self._chromosome_count = chromosome_count
        self._base_count = base_count
        self._picture_url = picture_url

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_entry_type(self):
        return self._entry_type

    def get_chromosome_count(self):
        return self._chromosome_count

    def get_base_count(self):
	    return self._base_count

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
        self._description = ""
        self._entry_type = GENOME
        self._chromosome_count = 0
        self._base_count = 0
        self._picture_url = ""

    def set_name(self, name):
        """
        Sets name object.
        """
        self._name = name

    def set_description(self, description):
        """
        Sets description for Entry.
        """
        self._description = description
        
    def set_entry_type(self, entry_type):
        """
        Sets entry type
        """
        self._entry_type = entry_type;

    def set_base_count(self, base_count):
        """
        Sets count for number of bases.
        """
        self._base_count = base_count

    def set_chromosome_count(self, chromosomes):
        """
        Sets count for number of chromosomes.
        """
        self._chromosome_count = chromosomes

    def set_picture_url(self, picture_url):
        """
        Sets picture url.
        """
        self._picture_url = picture_url

    def build_entry(self):
        return Entry(self._name, self._description, 
                self._entry_type, 
                self._chromosome_count, 
                self._base_count, self._picture_url)
