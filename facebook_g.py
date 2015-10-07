import requests
import lxml
from secret import cookie

def main(url):
	r = requests.get(url, cookies=cookie, verify=False)
	print r.text

if __name__ == "__main__":
	main("https://mbasic.facebook.com/groups/625191517538301")