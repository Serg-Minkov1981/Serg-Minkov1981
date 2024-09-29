import requests
from bs4 import BeautifulSoup

url = 'https://yandex.com.am/weather'

response = requests.get(url)
print(response)

bs = BeautifulSoup(response.text, "lxml")

print(bs)

# st = open('file.txt', "w")
# st.write(str())
# st.close()