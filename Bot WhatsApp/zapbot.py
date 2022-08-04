from pandas import options
from selenium import webdriver
import time

class whatsappbot:
    def __init__(self):
        self.messagem = "Bom dia pessoal, veja o vídeo que acabou de sair: "
        self.grupos = ['BB Seguros','⚠️❇️🟠 TAREFAS 🅿️📛❇️','Lista de política']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)


    def EnviarMensagens(self):
        #BB SEGUROS
        #<span dir="auto" title="BB Seguros" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">BB Seguros</span>
        #<div tabindex="-1" class="p3_M1">
        #<span data-testid="send" data-icon="send" class="">
        #TAREFAS
        #<span dir="auto" title="⚠️❇️🟠 TAREFAS 🅿️📛❇️" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="⚠️" draggable="false" class="b4 emoji wa i0jNr" style="background-position: -20px -40px;"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="❇️" draggable="false" class="b7 emoji wa i0jNr" style="background-position: -20px -60px;"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🟠" draggable="false" class="b95 emoji wa i0jNr" style="background-position: -20px -40px;"> TAREFAS <img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🅿️" draggable="false" class="b9 emoji wa i0jNr" style="background-position: -20px 0px;"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="📛" draggable="false" class="b74 emoji wa i0jNr" style="background-position: -40px -20px;"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="❇️" draggable="false" class="b7 emoji wa i0jNr" style="background-position: -20px -60px;"></span>
        #LISTA DE POLÍTICA
        #<span dir="auto" title="Lista de política" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr"><span class="matched-text i0jNr">Lista de</span> política</span>
        print('teste 04.ago.22')
        self.driver.get('https://web.whatsapp.com')
        time.sleep(40)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            time.sleep(3)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(5)
            botao_enviar.click()
            time.sleep(5)

bot = whatsappbot()
bot.EnviarMensagens()