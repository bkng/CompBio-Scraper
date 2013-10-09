from __future__ import print_function
from lxml import etree
import Entry
from Scraper import Scraper
from HTMLGenerator import HTMLGenerator

def write_entries(entries, type_of_entry):
    gen = HTMLGenerator(entries)
    html = gen.get_html()
    with open("cards/file_{0}.html".format(type_of_entry), mode="w") as f:
        f.write(etree.tostring(html, pretty_print=True))

def main():
    scraper = Scraper("bennett.k.ng@gmail.com")
    with open('gids.txt') as f:
        lines = f.read().splitlines()
    entries = [scraper.getEntry(gid, Entry.GENOME) for gid in lines]
    write_entries(entries, "genome")

if __name__ == "__main__":
    main()
