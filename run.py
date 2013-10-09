from lxml import etree
from Scraper import Scraper
from HTMLGenerator import HTMLGenerator

def write_entries(entries, type_of_entry):
    gen = HTMLGenerator(entries)
    html = gen.get_html()
    with open("cards/file_{0}.html".format(type_of_entry), mode="w") as f:
        f.write(etree.tostring(value, pretty_print=True))

def main():
    scraper = Scraper("")
    ventries = scraper.getVirusEntries(20, 0)
    gentries = scraper.getGenomeEntries(60, 0)
    write_entries(ventries, "virus")
    write_entries(gentries, "genome")

if __name__ == "__main__":
    main()
