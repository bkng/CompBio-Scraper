
#Enum for entry type
GENOME, VIRUS = range(2)

class Entry():
    """
    Entry class. Will contain card name, description, type, payload, and picture.
	
    name 					scientific name of the organism
	description 			description of the organism
    type 					GENOME or VIRUS constant
    chromosome_count		number of chromoses in the organism's genome
	base_count				number of bases in the organism's genome
    picture_url				URL of the picture to use for the cards
    """

    def __init__(self, name, description, type, chromosome_count, base_count, picture_url):
		self._name = name
		self._description = description
		self._type = type
		self._chromosome_count = chromosome_count
		self._base_count = base_count
		self._picture_url = picture_url

    def get_name(self):
        return self._name
		
	def get_description(self):
		return self._description
	
	def get_type(self):
		return self._type

    def get_entry_chromosome_count(self):
        return self._chromosome_count
		
	def get_entry_base_count(self):
		return self._base_count

    def get_picture_url(self):
        return self._picture_url
