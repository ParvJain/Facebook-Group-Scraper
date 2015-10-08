import requests
from lxml import html
from lxml import etree
from secret import cookie

def main(url):
	r = requests.get(url, cookies=cookie, verify=False)
	tree = html.fromstring(r.content)
	traveler = tree.xpath('//div[@id="m_group_stories_container"]')[0]
	status = tree.xpath('//div[@id="m_group_stories_container"]//span')[0]
	nextPage = tree.xpath('.//a/span[text()="See More Posts"]')[0]
	print nextPage.getparent().xpath('@href')[0]
	print(etree.tostring(nextPage, pretty_print=True))


if __name__ == "__main__":
	main("https://mbasic.facebook.com/groups/625191517538301")