from bs4 import BeautifulSoup


with open ("website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")

# #get title tag in html
# print(soup.title)

# #get string in title tag
# print(soup.title.string)

# #get anchor tag
# print(soup.a)

#get all anchor tags
anchor_tags = (soup.find_all(name="a")) # a list 

#to get all text in anchor tags

# for tag in anchor_tags:
#     # print(tag.getText()) # get name of tag
#     print(tag.get("href")) # get link
    
#to search for a particular value, when there are multiple types
#i.e multiple h1 you can specify with id and class_

heading = soup.find(name="h1", id="name")

print(heading)