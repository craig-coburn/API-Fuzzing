# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:30:13 2023

@author: craig
"""

import requests
import json
from bs4 import BeautifulSoup

# Base URL: https://cve.mitre.org/cve/search_cve_list.html
# Search URL: https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=sip

keywords = [
"Cellcrypt",
"Cellcrypt Android Mobile Client",
"STUN",
"Vocoder",
"Voice communication",
"Text messaging",
"SRTP",
"TLS",
"Vault",
"TCP",
"UDP",
"TLS 1.2",
"HTTPS",
"Openssl",
"VVoIP",
"Enterprise Communications Service",
"Enterprise Management Portal",
"ESC",
"EMP",
"API",
"Authentication Server API",
"SIP Server",
"SDP",
"Message Attachment Server",
"Authentication Server",
"SIP",
"SDES",
"Android keystore",
"SQLCipher",
"CCoreV4",
"PJSIP",
"OpenH264",
"Mp3lame",
"Libq",
"Rxcpp",
"Opus",
"libc++",
"libvphone"]

url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=sip"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all elements containing the term "CVE"
    cve_entries = soup.find_all(lambda tag: tag.name == 'a' and 'CVE-' in tag.get_text())
    
    # Extract and print the text from each matching element
    for entry in cve_entries:
        print(entry.get_text(strip=True))
else:
    print("Failed to retrieve the page.")
    
