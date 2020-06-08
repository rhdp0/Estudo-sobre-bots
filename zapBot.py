from selenium import webdriver
import time 

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Olá, você está falando com um robô!!"
        self.grupos = ["Thamara"]
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()

            chatBox = self.driver.find_element_by_class_name("_1Plpp")
            time.sleep(3)
            chatBox.click()
            chatBox.send_keys(self.mensagem)

            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)

            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()