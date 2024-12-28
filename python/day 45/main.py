# from bs4 import BeautifulSoup
# import requests
# import lxml
# with open("day 45/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents,"html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.prettify())

# to get all tages 

# all_anchor_tags = soup.find_all(name="a"))

# for tag in all_anchor_tags:
#     print(tag.getText())
    #   pirnt(tag.get("href"))


# heading = soup.find(name="h1",id= "name") to find class we use class_
# print(heading)

# company_url = soup.select_one(selector="# p a")

# response = requests.get(url="https://news.ycombinator.com/")
# yc = response.text
# soup = BeautifulSoup(yc,"html.parser")

# headline = soup.find(name="span",class_ = "titleline")

# print(headline.getText())

# response = requests.get("https://news.ycombinator.com/news")
# y_website = response.text
 
# soup = BeautifulSoup(y_website, "html.parser")
# articles = soup.find_all(name="span", class_="titleline")
# scores_list = soup.find_all(name="span", class_="score")
 
# scores = [score.getText() for score in scores_list]
# links = [article.find("a").get("href") for article in articles]
# article_names = [article.getText().split(" (")[0] for article in articles]
# print(article_names)
# print(links)
# print(scores)


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)