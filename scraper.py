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
	traveller = base.xpath('.//h3[1]/a/strong/a/text()')[0]
	traveller_slug = base.xpath('.//h3[1]/a/strong/a/@href')[0]
	description = tree.xpath('//div[@class="bi"]/p')

	descriptions = []

	for p in description:
		descriptions.append(etree.tostring(p, pretty_print=True))

	status = "".join(descriptions)
	timestamp = base.xpath('.//abbr/text()')[0]


	print traveller, traveller_slug, status, timestamp
	# print etree.tostring(description, pretty_print=True)
	# print etree.tostring(base, pretty_print=True)

if __name__ == "__main__":
	# collect("https://mbasic.facebook.com/groups/625191517538301")
	scrape("https://m.facebook.com/groups/625191517538301?view=permalink&id=973219502735499&refid=18&_ft_=qid.6204099145172029259%3Amf_story_key.973219502735499%3Atl_objid.973219502735499#footer_action_list")
