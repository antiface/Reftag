import unittest
import json
import urllib2
import re

site = "http://localhost:8080/"
#site = "http://reftag.appspot.com/"

def strip_jsonp(jsonp_string):
    return re.sub('mycallback\((.*)\);', r'\1', jsonp_string, flags=re.DOTALL)

def fetch_and_parse(url):
    jsonp_string = urllib2.urlopen(url).read()
    json_string = strip_jsonp(jsonp_string)
    return json.loads(json_string)

class TestDoiApi(unittest.TestCase):
    def test_doi(self):
        url = site + "doifetchjs.py?doi=10.1111%2Fj.1600-0404.1986.tb04634.x&callback=mycallback"
        data = fetch_and_parse(url)
        self.assertEquals(data['issn'], "00016314")

class TestGoogleBooksApi(unittest.TestCase):
    def test_gb(self):
        url = site + "googlebooksjs.py?book_url=http%3A%2F%2Fbooks.google.com%2Fbooks%3Fid%3DaqmAc2fFsAUC%26pg%3DPA90&callback=mycallback"
        data = fetch_and_parse(url)
        self.assertEquals(data['isbn'], "9780226019666")

class TestUrlApi(unittest.TestCase):
    def test_url(self):
        url = site + "urlfetchjs.py?url=http%3A%2F%2Fwww.nytimes.com%2F2009%2F03%2F26%2Fgarden%2F26slow.html&callback=mycallback"
        data = fetch_and_parse(url)
        self.assertEquals(data['title'], "Slow, Easy, Cheap And Green")


if __name__ == '__main__':
    unittest.main()
