
import urllib.request
import os
import re
import time
import random
from bs4 import BeautifulSoup

user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36']

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent',random.choice(user_agent_list))

	response = urllib.request.urlopen(url)
	html = response.read()
	return html

def get_category(url):
	whole_html = url_open(url).decode('utf-8')
	whole_soup = BeautifulSoup(whole_html,'html.parser')
	category_soup = whole_soup.find('div',attrs={'class':'wrapper'})
	category = {link.string:link.get('href') for link in category_soup.find_all('a')}
	return category
	



def get_text_url(num_url):
	page_html = url_open(num_url).decode('utf-8')
	page_soup = BeautifulSoup(page_html,'html.parser')
	articlelink_soup = page_soup.find('div',attrs={'class':'lph-pageList list-pageList'})
	x = articlelink_soup.find_all('h3')
	urllist = []
	for u in x:
		urllist.append(u.find('a').get('href'))
	return urllist




def find_text(soup):
	new_html = soup.find('div',attrs={'class':'lph-article-comView'})
	a = [paragraph.getText() for paragraph in new_html.find_all('p')]
	regl = re.compile('<[^>]*>')
	text_content = regl.sub('',''.join(a))
	return text_content
	
	

def save_text(folder,soup):
	filename = soup.title.string.replace(' | 雷锋网','').replace('/','除以') + '.txt'
	text_content = find_text(soup)

	with open(filename,'wt') as f:
		f.write(text_content)

def download_text(folder='source',pages=10):
	print('开始爬虫...') 
	os.mkdir(folder)
	os.chdir(folder)

	url = r'http://www.leiphone.com'
	category = get_category(url)

	for c,d in category.items():
		if c == '业界' or c == 'AI+' or c == 'GAIR' or c == '开发者':
			continue
		e = c.replace('/','')
		os.mkdir(e)
		os.chdir(e)
		print('正在爬取 %s 下的文章...' % c)

		for i in range(pages):
			page_num = i + 1
			num_url = d + r'/page/'+str(page_num)
			try:
				text_url_list = get_text_url(num_url)
			except:
				continue

			for text_url in text_url_list:
				try:
					html = url_open(text_url).decode('utf-8')
				except:
					print('url_open异常')
					continue
				soup = BeautifulSoup(html,'html.parser')
				save_text(c,soup)
				time.sleep(random.choice((2,4,6,8,10)))
		print('%s 已下载完成' % c)
		os.chdir(os.path.dirname(os.getcwd()))
	print('爬虫操作结束')

if __name__ == '__main__':
	download_text()
