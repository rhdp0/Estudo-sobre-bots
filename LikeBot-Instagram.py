from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Login(self):
        driver = self.driver
        #Perfil
        driver.get("https://www.instagram.com/") #Este para perfis
        #Tag
        #driver.get("https://www.instagram.com/explore/tags/") #Este para tags
        time.sleep(3)

        username_Element = driver.find_element_by_xpath("//input[@name='username']")
        username_Element.clear()
        username_Element.send_keys(self.username)

        password_Element = driver.find_element_by_xpath("//input[@name='password']")
        password_Element.clear()
        password_Element.send_keys(self.password)
        password_Element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtir_fotos('PERFIL OU TAG ALVO PARA O BOT CURTIR AS FOTOS')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("pulando link inválido")
                continue
            driver.get(pic_href)
            
            try:
                driver.find_element_by_xpath(
                    '//button[@class="wpO6b "]').click()
                time.sleep(random.randint(19, 23))
            except Exception as e:
                print(e)
                time.sleep(5)


login = InstagramBot('YOUR ACCOUNT', 'YOUR PASSWORD')
login.Login()
