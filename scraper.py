import requests
from lxml import html
from lxml import etree
from secret import cookie

def main(url):
	r = requests.get(url, cookies=cookie, verify=False)
	tree = html.fromstring(r.content)
	postURI = tree.xpath('.//a[text()="Full Story"]')
	nextPage = tree.xpath('.//a/span[text()="See More Posts"]')[0]

	for x in postURI:
		print x.xpath('@href')

	curUrl = nextPage.getparent().xpath('@href')[0]
	finURL = "/groups/625191517538301?bacr=1388816159%3A633308973393222&refid=18"

	if curUrl == finURL:
		for x in postURI:
			print x.xpath('@href')[0]
	main("https://mbasic.facebook.com" +curUrl)

if __name__ == "__main__":
	main("https://mbasic.facebook.com/groups/625191517538301")