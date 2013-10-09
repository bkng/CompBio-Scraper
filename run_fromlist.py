from __future__ import print_function
from lxml import etree
import Entry
from Scraper import Scraper
from HTMLGenerator import HTMLGenerator

def write_entries(entries, type_of_entry):
    gens = [HTMLGenerator(entry) for entry in entries]
    html = [gen.get_html() for gen in gens]
    for index, value in enumerate(html):
        with open("cards/file_{0}{1}.html".format(type_of_entry, index), mode="w") as f:
            f.write(etree.tostring(value, pretty_print=True))

def main():
    scraper = Scraper("bennett.k.ng@gmail.com")
    with open('gids.txt') as f:
        lines = f.read().splitlines()
    entries = [scraper.getEntry(gid, Entry.GENOME) for gid in lines]
    write_entries(entries, "genome")

if __name__ == "__main__":
    main()
