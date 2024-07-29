from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

#Login and Password input

login = input("Digite o CPF: ")
senha = input("Digite a Senha: ")

#Configuração do WebDriver
firefox_service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service = firefox_service)

#Actual automation

browser.get("https://siga.cps.sp.gov.br/ALUNO/login.aspx")

browser.find_element('xpath','//*[@id="vSIS_USUARIOID"]').send_keys(login)
browser.find_element('xpath','//*[@id="vSIS_USUARIOSENHA"]').send_keys(senha)
browser.find_element('xpath',
                     '/html/body/form/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input').click()
time.sleep(2)
browser.find_element('xpath', '//*[@id="gxp0_cls"]').click()
time.sleep(10)
