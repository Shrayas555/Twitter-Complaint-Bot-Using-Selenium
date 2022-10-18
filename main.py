from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_UP=150
PROMISED_DOWN=10
CHROMEDRIVER='/Users/shrayasraju/Desktop/chromedriver'
TWITTEREMAIL='shrayas5555@gmail.com'
TWITTERPASS='********'

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=CHROMEDRIVER)
        self.upload=0
        self.download=0


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/result/13819165338')
        time.sleep(5)
        self.go=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go.click()
        time.sleep(120)
        self.downloadnum=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.download=self.downloadnum.text
        self.uploadnum = self.driver.find_element(By.XPATH,
                                                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.upload = self.uploadnum.text


    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        self.email=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.email.send_keys(TWITTEREMAIL)
        time.sleep(3)
        self.next=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        self.next.click()
        time.sleep(5)
        self.password=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password.send_keys(TWITTERPASS)
        time.sleep(3)
        self.login=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        self.login.click()
        time.sleep(5)
        self.tweet=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        self.tweet.click()
        time.sleep(3)
        self.content=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        self.content.send_keys('Hey iternet provider , my internet is slow.')
        self.tweet2=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        self.tweet2.click()



internet=InternetSpeedTwitterBot()
internet.get_internet_speed()
if float(internet.upload)<PROMISED_UP or float(internet.download)<PROMISED_DOWN:
    internet.tweet_at_provider()

