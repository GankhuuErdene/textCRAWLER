from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('http://humanz.mn/i/381').text
soup = BeautifulSoup(source, 'lxml')
body = soup.find('body')

#print(body.prettify())
#title = body.h2.text
print(title)
summary = body.find('div', class_='entry-content-inner').p.text
print(summary)
# with open('csvfile.csv','UTF-8', 'w') as file:
#     for line in summary:
#         file.write(line)
#         file.write('\n')
with open('C:/Users/pc/Desktop/crawler.csv', "w", encoding='utf8' ) as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in summary:
            writer.writerow(line)