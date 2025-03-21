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

#4.) Keywords 

keyword = input("Enter a keyword: ").lower()
text_content = soup.get_text().lower()
count_keyword = text_content.count(keyword)
print(f"The keyword {keyword} appears {count_keyword} times in the webpage!")

#5.) 

#6.) Longest Paragraphs

paragraphs = soup.find_all('p')

longest_paragraph = ""
longest_word_count = 0

for paragraph in paragraphs:
        text = paragraph.get_text().strip()
        word_count = len(text.split())

        if word_count >= 5 and word_count > longest_word_count:
            longest_paragraph = text
            longest_word_count = word_count





if longest_paragraph:
    print("\nLongest Paragraph Found:\n")
    print(longest_paragraph)
    print(f"\nThis paragraph contains {longest_word_count} words.")
else:
    print("No paragraph with 5 or more words was found.")



