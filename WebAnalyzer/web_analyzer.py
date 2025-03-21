import requests 
from bs4 import BeautifulSoup 
url = "https://en.wikipedia.org/wiki/University_of_Calgary" 
try: 
    response = requests.get(url) 
    response.raise_for_status()  # Ensures the request was successful 
    soup = BeautifulSoup(response.text, 'html.parser') 
    print(f"Successfully fetched content from {url}") 
except Exception as e: 
    print(f"Error fetching content: {e}") 

print(soup.prettify())

#3.) Data Analysis
headings = sum(len(soup.find_all(f'h{i}')) for i in range(1,7))
links = len(soup.find_all('a'))
paragraphs = len(soup.find_all('p'))

print(f'Number of headings: {headings}')
print(f'Number of links: {links}')
print(f'Number of paragraphs: {paragraphs}')

# 4.) Keywords 


# 5.) Word Frequency Analysis

txt = soup.get_text().lower()
words = txt.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

top_5_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

print(top_5_words)


# 7.)

import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group SIGMA')
plt.ylabel('Count')
plt.show()