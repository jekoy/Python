import urllib2
import re
import time
def download(url):
    print"Download:",url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print"Download error:",e.reason
        html=None
    return html

def crawl_sitemap(url):
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    for count in range(1,6):
        print"CRAW"
        for link in links:
            html=download(link)
            time.sleep(3)
    print"craw end"
