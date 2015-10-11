import requests
from lxml import html
from lxml import etree
from secret import cookie
import peewee
from models import Potato, Comment, Permalink

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
	try:
		base = tree.xpath('//div[@id="m_story_permalink_view"]/div[1]')[0]
		bottom = tree.xpath('//div[@id="m_story_permalink_view"]/div[2]/div/div[3]')[0]
		traveller = base.xpath('.//h3[1]/a/strong/a/text()')[0]
		traveller_slug = base.xpath('.//h3[1]/a/strong/a/@href')[0]
		description = base.xpath('.//div/div[2]/p')
		# print description
		descriptions = []

		for p in description:
			descriptions.append(etree.tostring(p))

		status = "".join(descriptions)
		timestamp = base.xpath('.//abbr/text()')[0]


		# print timestamp
		# pot = Potato(slug = url,
		# 		     traveler = traveller,
		# 		     traveler_slug = traveller_slug,
		# 		     question = status,
		# 		     timestamp = timestamp)
		# pot.save()

		helper = bottom.xpath('.//div[contains(@id,"")]')
		for x in helper:
			try:
				if len(x.get('id')) == 15:
					name = x.xpath('.//h3/a[1]/text()')[0]
					link = x.xpath('.//h3/a[1]/@href')[0]
					comment = x.xpath('.//div[1]')[0]
					c = etree.tostring(comment)
					try:
						like = x.xpath('.//a[@aria-label="Like"]/text()')[0]
					except IndexError:
						like = str(0)
					timestamp = x.xpath('.//abbr/text()')[0]
					# commentt = Comment(potato=pot,
					# 				   helper=name,
					# 				   helper_slug=link,
					# 				   power=like,
					# 				   timestamp=timestamp,
					# 				   answer=c)
					# commentt.save()
					print c
					# print name, link, like, timestamp, c
					# print etree.tostring(x, pretty_print=True)
			except:
				pass

		# print etree.tostring(description, pretty_print=True)
		# print etree.tostring(base, pretty_print=True)
	except:
		pass

if __name__ == "__main__":
	# collect("https://mbasic.facebook.com/groups/625191517538301")
	# scrape("https://m.facebook.com/groups/625191517538301?view=permalink&id=973219502735499&refid=18&_ft_=qid.6204099145172029259%3Amf_story_key.973219502735499%3Atl_objid.973219502735499#footer_action_list")
	for i, x in enumerate(Permalink.select()):
		print i, x.slug
		scrape("https://mbasic.facebook.com" + x.slug)