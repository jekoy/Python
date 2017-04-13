import urllib2
def download(url,num=2):
    print"download:",url
    headers={'user_agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print"download error:",e.reason
        html=None
        if num>0:
            if hasattr(e,'code') and 500<=e.code<=600:
                return download(url,num-1)
    return html
