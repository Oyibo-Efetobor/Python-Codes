from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

#print first name of article
yc_soup = BeautifulSoup(yc_webpage, "html.parser")
# Find all span tags with class titleline, then find the a tags inside them
article_tags = yc_soup.select("span.titleline > a")
print(article_tags[0].getText())  # Get the text of the first article
print(article_tags[0].get("href"))  # Get the link of the first article

# for article in article_tag:
#     article_text = article.getText()
#     artcle_link = article.get("href")
    
# print(article_tag)
# print(article_tag.getText) if article_tag else print("article not found")
# article_link = article_tag.get("href")
# article_upvote = yc_soup.find(name="span", class_="score").getText()
# print(article_link, article_upvote)




























# with open ("website.html") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")

# # #get title tag in html
# # print(soup.title)

# # #get string in title tag
# # print(soup.title.string)

# # #get anchor tag
# # print(soup.a)

# #get all anchor tags
# anchor_tags = (soup.find_all(name="a")) # a list 

# #to get all text in anchor tags

# # for tag in anchor_tags:
# #     # print(tag.getText()) # get name of tag
# #     print(tag.get("href")) # get link
    
# #to search for a particular value, when there are multiple types
# #i.e multiple h1 you can specify with id and class_

# heading = soup.find(name="h1", id="name")

# print(heading)

