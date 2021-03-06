from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os



keywords = [ "BTS RM", "BTS 진", "BTS 슈가", "BTS 제이홉", "BTS 지민", "BTS 뷔", "BTS 정국"]

for keyword in keywords :

    if not os.path.exists(keyword):
        os.makedirs(keyword)



    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height


    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    count = 1
    for image in images:
        try:
            if count == 200: 
                break

            image.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            path = keyword + "\\" + str(count) + ".jpg"
            print(path)
            urllib.request.urlretrieve(imgUrl, path)
            print("save")
            count += 1
        except Exception as e:
            print(e)
            pass

    driver.close()