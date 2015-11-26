#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# yrtemp 0.1
# this script grabs the current temperature from the YR URL (html_doc) below.
# in the unlikely event that you do not live in Gothenburg, please
# go ahead and change it to another URL.
#

from bs4 import BeautifulSoup
import requests
import re

# Example html that can be used when debugging

#html_doc = """
#<tr>
#    <td title="Temperature: -12°.  Feels like 4°.  For the period: 12:00" class="temperature plus">4°</td>
#    <td title="Precipitation: 0 mm.  For the period: 12:00–18:00.  ">0 mm</td>
#    <td title="Light air, 1 m/s from west.  For the period: 12:00" class="txt-left">
#</tr>
#"""

html_doc = requests.get('http://www.yr.no/place/Sweden/V%C3%A4stra_G%C3%B6taland/Gothenburg/')

if html_doc.status_code == 200:
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    line = soup.find('td', class_="temperature")
    # regexp black magic to search that line for the first "[int]" OR "-[int]"
    value = re.search('(?<=Temperature: )-?\w+', str(line))

    # ...and Bob's your uncle
    print value.group(0)

else:
    print 'HTTP error: ', int(html_doc.status_code)
