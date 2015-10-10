import requests
from lxml import html
from lxml import etree
from secret import cookie
import peewee
from models import Permalink

def collect(url):
	r = requests.get(url, cookies=cookie, verify=False)
	tree = html.fromstring(r.content)
	postURI = tree.xpath('.//a[text()="Full Story"]')
	nextPage = tree.xpath('.//a/span[text()="See More Posts"]')[0]

	for x in postURI:
		print x.xpath('@href')

	curUrl = nextPage.getparent().xpath('@href')[0]
	finURL = "/groups/625191517538301?bacr=1388816159%3A633308973393222&refid=18"

	if curUrl != finURL:
		for x in postURI:
			link = x.xpath('@href')[0]
			newLink = Permalink.create(slug = link)
			newLink.save()
	print ""
	print curUrl
	print ""

	collect("https://mbasic.facebook.com" +curUrl)

def scrape(url):
	r = requests.get(url, cookies=cookie, verify=False)
	tree = html.fromstring(r.content)
	# print r.content
	base = tree.xpath('//div[@class="bd"]')[0]
	print etree.tostring(base, pretty_print=True)
	# print etree.tostring(base, pretty_print=True)
if __name__ == "__main__":
	# collect("https://mbasic.facebook.com/groups/625191517538301")
	scrape("https://m.facebook.com/groups/625191517538301?view=permalink&id=973505226040260&refid=18&_ft_#footer_action_list")
