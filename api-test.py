import unittest
import HtmlTestRunner
import json
import http.client
import urllib.request
import urllib.parse
import urllib.error
import os
import time
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from http.client import responses

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-gpu")

chrome_driver = 'C:\\Python35\\selenium\\chromedriver.exe'

class RestApiTest(unittest.TestCase) :
    # # define API url
    url ="https://www.tokopedia.com/promo/wp-json/tkp/v3/posts?per_page=300"

    def test_callApi(self):
        url = self.url
        f = urllib.request.urlopen(url)
        json_string=f.read().decode('utf-8')
        post_json = json.loads(json_string)
        datas = post_json['data']
        total= len(datas)
        counter = 1
        dataErrorList = []
        for data in datas:
            title = data['title']
            dataId = str(data['id'])
            title = title.encode("ascii","ignore")
            title = title.decode("utf-8")
            urlLink = data['link']
            urlLinkApp = data['link_apps']
            urlPromoLink = data['promo_link']
            imagesThumbnail = data['images']['thumbnail']
            imagesBanner = data['images']['banner']
            imageThumbnailsize = self.GetImageSize(imagesThumbnail)
            imageBannersize = self.GetImageSize(imagesBanner)
            statusUrlLink = self.check_link(urlLink)
            statusUrlLinkApp = self.check_link(urlLinkApp)
            statusUrlPromoLink = self.check_link(urlPromoLink)
            statusimagesThumbnail = self.check_link(imagesThumbnail)
            statusimagesBanner = self.check_link(imagesBanner)

            print ('=================== data '+str(counter)+' start ============================')
            print (title)
            print ('id = '+ str(data['id']))
            print ('total category = ' + str(len(data['categories'])))
            print ('urlLink Status = ' + statusUrlLink)
            print ('urlLinkApp Status = ' + statusUrlLinkApp)
            print ('urlPromoLink = ' +  statusUrlPromoLink)
            print ('imagesThumbnail = ' + statusimagesThumbnail)
            print ('imagesBanner = '+ statusimagesBanner)
            print ('imageThumbnailSizeHeight =' + str(imageThumbnailsize.shape[0:2]))
            print ('=================== data '+str(counter)+' end =============================')
            counter += 1

        hasError = False
        # if (statusUrlLink != "200" or statusUrlLinkApp != "200" or statusUrlPromoLink != "200" or statusimagesThumbnail != "200" or statusimagesBanner != "200" or imageThumbnailsize.shape[0] < 328) :
        #     dataError = {
        #         "title" : title,
        #         "id": dataId
        #     }
        dataError = {
                "title" : title,
                "id": dataId
            } 
        if(statusUrlLink != "200"):
            hasError=True
            dataError['statusUrlLink'] = urlLink
        if(statusUrlLinkApp != "200"):
            hasError=True
            dataError['statusUrlLinkApp'] = urlLinkApp
        if(statusUrlPromoLink != "200"):
            hasError=True
            dataError['statusUrlPromoLink'] = urlPromoLink
        if(statusimagesThumbnail !="200"):
            hasError=True
            dataError['statusimagesThumbnail'] = imagesThumbnail
        if(statusimagesBanner !="200"):
            hasError=True
            dataError['statusimagesBanner'] = imagesBanner
        if(imageThumbnailsize.shape[0] < 328):
            hasError=True
            dataError['sizeThumbnail'] = "image height dibawah 328"   
           

        if(hasError == True):
            # dataError = {
            #     "title" : title,
            #     "id": dataId
            # }
            dataErrorList.append(dataError)    
        
            for dataError in dataErrorList :
                print('############### ERROR Data Start #####################')
                for k,v in dataError.items():
                    print (k+ ' = ' +v)
                print('############### ERROR Data END #####################')
        # print("total API =",total)
        # print(f.getcode())
    
    
    def check_link(self,url):
           
        try:
            r = urllib.request.urlopen(url)
            # print(r.status, r.reason)
            return str(r.getcode())
            # json_string = r.read().decode('utf-8')
            # post_json = json.loads(json_string)
            # datas = post_json['data']
            # total= len(datas)
            # for data in datas:
            #     print (str (data['id'])+' total = '+str(len(data['categories'])))
            #     print('link = '+ data['link'])
            #     print('link_apps = '+ data['link_apps'])
            #     print('app_link = '+ data['link_apps'])
        except urllib.error.HTTPError as e:
            if hasattr (e, 'code'):
                # print(e.code)
                return str(e.code)
                          
            if hasattr (e, 'reason'):
                # print(e.reason)
                return e.reason
        except urllib.error.URLError as e:
            if hasattr (e,'reason'):
                # print(e.reason)
                return(e.reason)
        except :
            return("Link Broken/Empty")        
                
    def tearDown(self):
         print("### test is over ###") 
 
    def GetImageSize(self,imageurl) :
        req = urllib.request.urlopen(imageurl)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1) # 'Load it as it is'
        # //print(img.shape[0:2])
        return img


# if __name__ == '__main__':
#         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:\Report'))         

if __name__ == "__main__":
      unittest.main()        

# not using class, code running
# url = 'https://www.tokopedia.com/promo/wp-json/wp/v2/posts?per_page=100'
# f = urllib.request.urlopen(url)
# print(f.read().decode('utf-8'))