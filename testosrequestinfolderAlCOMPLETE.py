# python -m venv john
# .\john\Scripts\activate
# pip install requests
# pip install validators

import os
import requests
import re
import validators

directory = "./testFolder"

successCodeFloor = 200
successCodeCeiling = 400

urls = []
filteredUrls = []
files = []
exemptUrls = ['https://aaaaaaaaaaaaaa.corn', 'https://google.corn']


for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith(".md")]:
        file_path = f"{dirpath}/{filename}"
        with open(file_path, 'r') as f:
            text = f.read()
            for url in re.findall(r'(https?://[^\s]+)', text):
                urls.append(url)
                if url not in exemptUrls:
                    try:
                        if validators.url(url):
                            response = requests.get(url)
                            if response.status_code not in range(successCodeFloor, successCodeCeiling):
                                filteredUrls.append(url)
                                files.append(filename)
                        else:
                            filteredUrls.append(url)
                            files.append(filename)
                    except requests.exceptions.RequestException:
                        filteredUrls.append(url)
                        files.append(filename)
        
if len(filteredUrls) > 1:
    raise SystemExit(f"The following broken URLs were found:\n\tURLs: {filteredUrls}\n\tLocations: {files}")
elif len(filteredUrls) > 0:
    raise SystemExit(f"The following broken URL was found:\n\tURL: {filteredUrls}\n\tLocation: {files}")
else:
    print("No broken URLs found.")