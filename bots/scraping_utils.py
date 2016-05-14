import urllib2
from bs4 import BeautifulSoup

def get_site_html(url):

    '''
    Read an html page with the right settings.
    '''

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    try:
        req = urllib2.Request(url, headers = hdr)
        source = urllib2.urlopen(req).read()
    except urllib2.HTTPError, e:
        print e.fp.read()
        source = []

    return source


def get_tree(url):

    '''
    Parse an HTML page into a BeautifulSoup tree.
    '''

    source = get_site_html(url)
    tree = BeautifulSoup(source,'html.parser')
    return tree