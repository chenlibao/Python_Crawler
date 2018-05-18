from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://www.jianshu.com/p/aa4a1829840f')
driver.implicitly_wait(10)
include_title = []
author = driver.find_element_by_xpath('//span[@class="name"]/a').text
publish_time = driver.find_element_by_xpath('//span[@class="publish-time"]').text
word = driver.find_element_by_xpath('//span[@class="wordage"]').text
view = driver.find_element_by_xpath('//span[@class="views-count"]').text
comments = driver.find_element_by_xpath('//span[@class="comments-count"]').text
likes = driver.find_element_by_xpath('//span[@class="likes-count"]').text
included_names = driver.find_elements_by_xpath('//div[@class="include-collection"]/a/div')
print(included_names)
for i in included_names:
    include_title.append(i.text)
print(author,publish_time,word,view,comments,likes,include_title)