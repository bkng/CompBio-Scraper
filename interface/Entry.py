
#Enum for entry type
GENOME, VIRUS = range(2)

class Entry():
    """
    Entry class. Will contain card name, description, type, payload, and picture.
    name should be name of entry
	description should be a description of the entry
    entry_type will be either GENOME or VIRUS constant
    entry_value will be value of the entry, either chromosome count for genomes or base pair addition for viruses
    picture will be a link to the picture to use for the cards
    """

    def __init__(self, name, description, entry_type, entry_value, picture_url):
		self._name = name
		self._description = description
		self._entry_type = entry_type
		self._entry_value = entry_value
		self._picture_url = picture_url

    def get_name(self):
        return self._name
		
	def get_description(self):
		return self._description

    def get_entry_type(self):
        return self._entry_type

    def get_entry_value(self):
        return self._entry_value

    def get_picture_url(self):
        return self._pictuer_url
