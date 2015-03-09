u"""
@author: xieyanfen1990@126.com
@attention: this is PhantomJS about webdriver and settings User-Agent

"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url="http://m.dianping.com/forum/note/7868689"

ua1=("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) ""Gecko/20100101 Firefox/25.0")

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ua1

driver=webdriver.PhantomJS(desired_capabilities=dcap)
driver.get(url)
current_url=driver.current_url

print "the first url is :"+current_url

ua2=('Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53')
dcap["phantomjs.page.settings.userAgent"] = ua2

driver=webdriver.PhantomJS(desired_capabilities=dcap)
driver.get(url)
current_url=driver.current_url

print "the second url is :"+current_url
