from bs4 import BeautifulSoup
import requests
import csv


page = requests.get('https://github.com/trending')

# Create a beautiful soup object

soup = BeautifulSoup(page.text, 'html.parser')

# get repo list

repo = soup.find(class_="Box")

# find all instances of that class

repo_list = soup.find_all(class_="Box-row")

print(len(repo_list))

# Open writer with name
file_name = "github_trending_today.csv"

# set newline to be '' so that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

# write a new row as a header

f.writerow(['Developer', 'Repo Name', 'Number of Stars'])

for repo in repo_list:
    full_repo_name = repo.find('a').text.split('/')
    developer = full_repo_name[0].strip()
    repo_name = full_repo_name[1].strip()
    stars = repo.find(class_='octicon oticon-star').parent.text.strip()

    print('developer', developer)
    print('name', repo_name)
    print('stars', stars)
    print('Writing rows')

    f.writerow([developer, repo_name, stars])









