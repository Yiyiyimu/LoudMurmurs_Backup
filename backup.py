import requests
import re
import os

response = requests.get("https://loudmurmursfm.com/feed/audio.xml")
t = response.text.replace("\n", " ")
all_links = re.findall(r'(?<=url=")(\S*.mp3)', t)
all_text = [t.strip() for t in re.findall(r'(?<=><title><!\[CDATA\[)(.*?)(?=\]\])', t)][2:]

folder_path = os.path.join(os.getcwd(), "小声喧哗-音频备份")
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
for i in range(len(all_text)):
    print(i, ": ", all_text[i])
    cleaned_name = re.sub("[\"“”/\:*?<>|]", "", all_text[i])
    filename = os.path.join(folder_path, cleaned_name + ".mp3")
    audio = requests.get(all_links[i])
    with open(filename, 'wb') as file:
        file.write(audio.content)
