
#Enum for entry type
GENOME, VIRUS = range(2)

class Entry():
    """
    Entry class. Will contain card name, description, type, payload, and picture.
	
    name 					scientific name of the organism
	description 			description of the organism
    entry_type 				GENOME or VIRUS constant
    entry_chromosome_count	number of chromoses in the organism's genome
	entry_base_count		number of bases in the organism's genome
    picture					URL of the picture to use for the cards
    """

    def __init__(self, name, description, entry_type, entry_chromosome_count, entry_base_count, picture_url):
		self._name = name
		self._description = description
		self._entry_type = entry_type
		self._entry_chromosome_count = entry_chromosome_count
		self._entry_base_count = entry_base_count
		self._picture_url = picture_url

    def get_name(self):
        return self._name
		
	def get_description(self):
		return self._description

    def get_entry_chromosome_count(self):
        return self._chromosome_count
		
	def get_entry_base_count(self):
        return self._base_count

    def get_entry_value(self):
        return self._entry_value

    def get_picture_url(self):
        return self._picture_url
