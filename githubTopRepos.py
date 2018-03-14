import urllib.request
import urllib.parse 
import urllib.error
import http.cookiejar
import requests
import lxml from html
from bs4 import BeautifulSoup
import re
import operator

top_limit = 9;

def enterIntoWebsite():

	#enter the github username
	username = str(input("Enter the github username:  "))

    #dictionary to store key value pair of 
    # repository and corresponding no. of stars 
	repo_dict = {}

	url = "https://github.com/ " + username + "?tab=repositories"

	while True:

		#open the website and get the html of 
		#webpage into doc
		cj = http.cookiejar.CookieJar()
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
		resp = opener.open(url)
		doc = html.fromstring(resp.read)


		repository_name = doc.xpath('//li[@class="col-12 d-block width-full py-4 border-bottom public source"]/div[@class="d-inline-block mb-1"]/h3/a/text()')

		#repo list, to store repository names
		repo_list = []

		for name in repository_name:
			name = ' '.join(''.join(name).split())
			repo_list.append(name)
			repo_dict[name] = 0;


		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		div = soup.find_all('li', {'class': 'col-12 d-block width-full py-4 border-bottom public source'})

		for d in div:
			temp = d.find_all('div',{'class':'f6 text-gray mt-2'})

			for t in temp:

				#get the number of stars of a repo
				x = t.find_all('a', attrs = {'href': re.compile("^\/[a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\.\-\_]+\/stargazers")})

				