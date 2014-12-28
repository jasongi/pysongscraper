# -*- coding: utf-8 -*-

"""
pysongscraper.py.

Python script to download a list of songs in csv format from youtube

https://github.com/jasongi/pysongscraper

Copyright (C)  2014 Jason Giancono

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
    
"""
__version__ = "0.1"
__author__ = "Jason Giancono"
__license__ = "GPLv2"

import csv
from pygoogle import pygoogle
import pafy
import sys
import os

def scrape(urls):
    for song in urls:
        print song
        video = pafy.new(song)
        print '''Downloading ''' + video.title
        video.getbestaudio().download()


def main():
    urls = []
    if sys.argv[1] == '-csv':
        with open(sys.argv[2], 'rb') as csvfile: 
            csvreader = csv.reader(csvfile)
            csvarray = []
            for row in csvreader:
                csvarray.append(row)
            for row in csvarray:
                for song in row:
                    googsearch = pygoogle(song + ' site:youtube.com/watch')
                    googsearch.pages = 1
                    ytlink = googsearch.get_urls()[0]
                    urls.append(ytlink)
            scrape(urls)
if __name__ == "__main__":
    main()

