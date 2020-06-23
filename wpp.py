from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from selenium import webdriver

import re
import time 
import os



class WppBot:

    def __init__(self):
        self.nome_contato = "Mãe Tim"
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.ultimo_texto = ''
        
    
    def whatsapp(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)

        target = self.driver.find_element_by_xpath(f"//span[@title='{self.nome_contato}']")
        time.sleep(3)
        target.click()

    def escuta(self):
    #Vamos setar todos as mensagens no grupo.
        post = self.driver.find_elements_by_class_name('z_tTQ')
    #Vamos pegar o índice da última conversa.
        ultimo = len(post) - 1
    #Vamos pegar o  texto da última conversa e retornar.
        texto = post[ultimo].find_elements_by_css_selector('span.selectable-text')
        self.texto = texto[len(texto)-1].text
        return self.texto
    

    def bot(self):

        chatbot = ChatBot("Zoe")

        trainer = ChatterBotCorpusTrainer(chatbot)

        trainer.train('chatterbot.corpus.portuguese.conversations')

        while True:
            texto = self.escuta()
            texto = str(texto)
                
            if texto != self.ultimo_texto and texto[0] != ':':

                self.ultimo_texto = texto
                user_input = texto

                self.bot_response = chatbot.get_response(user_input)

                chatBox = self.driver.find_element_by_class_name("_3uMse")
                time.sleep(3)
                chatBox.click()
                chatBox.send_keys(":" + str(self.bot_response))

                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                time.sleep(3)

                botao_enviar.click()
                time.sleep(5)
    

bot = WppBot()
bot.whatsapp()
time.sleep(30)
bot.bot()

