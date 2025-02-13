import requests
from bs4 import BeautifulSoup
import pandas as pd

TEST_URL = "https://en.wikipedia.org/wiki/Web_scraping"

response = requests.get(TEST_URL)

if response.status_code == 200:
    print("✅ Successfully fetched the webpage!")
else:
    print(f"❌ Failed to fetch webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

data = []
for para in soup.find_all("p"):
    text = para.get_text(strip=True)
    if text: 
        data.append(text)

df = pd.DataFrame(data, columns=["Extracted Text"])

df.to_excel("test_scraped_data.xlsx", index=False)

print("✅ Data successfully saved to test_scraped_data.xlsx!")
