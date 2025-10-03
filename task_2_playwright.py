from html.parser import HTMLParser
import urllib.request as urllib2


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "title":
            print("tag:", tag)

    def handle_endtag(self, tag):
        if tag == "title":
            print("endtag:", tag)

    def handle_data(self, data):
        value = "Fast and reliable end-to-end testing for modern web apps | Playwright"
        if data == value:
            print("data:", data)


page = urllib2.urlopen("https://playwright.dev/")
parser = MyHTMLParser()
parser.feed(str(page.read()))
