# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:30:13 2023

@author: craig
"""

import requests
import json
from bs4 import BeautifulSoup
import csv

# Base URL: https://cve.mitre.org/cve/search_cve_list.html
# Search URL: https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=

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

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Keyword', 'CVE', 'Paragraph'])  # Write headers

    for current_keyword in keywords:
        record_count = 0
        url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=" + current_keyword
        print("Scraping website: ", url)
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <td> elements with the attribute valign="top"
            td_elements = soup.find_all(lambda tag: tag.name == 'td', attrs = {'valign': 'top'})
            
            cve = None  # Initialize the CVE variable
            
            with  open("output.csv", "a", encoding="utf-8") as file:
                # file.write("\n\n\n\n\n" + word.upper() + "\n")
                for td in td_elements:
                    paragraph = td.get_text(strip=True)  # Get the paragraph text
                    if 'CVE-' in td.get_text() and len(td.get_text())<20:
                        cve = td.get_text(strip=True)  # Store the CVE text
                        # csv_writer.writerow([current_keyword, cve])  # Write data to CSV
                        # file.write("[" + current_keyword + "]: " + cve + '\n\n')
                    else:
                        # paragraph = td.get_text(strip=True)  # Get the paragraph text
                        if cve and paragraph:  # Check if both CVE and paragraph are present
                            csv_writer.writerow([current_keyword, cve, paragraph])  # Write data to CSV
                            cve = None  # Reset the CVE variable
                            record_count += 1
            print(record_count, "Records")
        else:
            print("Failed to retrieve the page.")
    
