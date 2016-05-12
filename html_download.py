#coding=UTF-8
'''
Created on 2016年4月26日

@author: Feng Yujie
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self,url):
        #print 'start download'
        if url is None:
            #print 'url id none'
            return None
        else:
            #print 'urllib2'
            response=urllib2.urlopen(url)
            #print 'urllib2 seccesful'
            #print response.getcode()
            if response.getcode()!=200:
                return None
            return response.read()
        
    
    



