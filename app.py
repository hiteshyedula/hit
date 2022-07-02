import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests
from bs4 import BeautifulSoup


class Zen:

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    
    
    def sign_in(self, url):
        username = "yadulahitesh@gmail.com"
        password = "Mytestpass@123"
        self.driver.get(url)
        time.sleep(5)

#sign in process
        username_input_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
        password_input_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
        submit_button_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'

        username1 = self.driver.find_element(by=By.XPATH, value=username_input_xpath)
        password1 = self.driver.find_element(by=By.XPATH, value=password_input_xpath)
        submit_button = self.driver.find_element(by=By.XPATH, value=submit_button_xpath)

        username1.send_keys(username)
        password1.send_keys(password)
        submit_button.click()
        time.sleep(3)

# # method to get data from left panel using BeautifulSoup
    def getLhsData(self):
        url = self.driver.current_url
        data = requests.get(url)
        soup = BeautifulSoup(data.content,'lxml')

        details=[]
        for data in self.soup.findAll('div', class_='ml-4'):
            details.append(data.text)
        return details

#method for creating a Query process
    def query_creation(self, querytitle, querydes):
        
#query button selection from side pane
        queryicon = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[1]/nav/ul/div[6]")
        queryicon.click()
        time.sleep(2)
#selecting the create query button
        createQueryBtn = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[2]/div/div[1]/div[1]/button")
        self.driver.execute_script("arguments[0].click();", createQueryBtn)
        time.sleep(1)
#selecting cancel button
        cancelBtn = self.driver.find_element(by=By.XPATH,
                                             value="/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section["
                                                   "3]/div[2]/button[1]")
        cancelBtn.click()
        time.sleep(2)
#selecting category
        select = Select(
        self.driver.find_element(by=By.XPATH, value="//select[@class='formInputs'and @name='category']"))
        select.select_by_index(1)
#select subcategory
        select = Select(
            self.driver.find_element(by=By.XPATH, value="//select[@class='formInputs'and @name='subcategory']"))
        select.select_by_index(1)
#select language
        select = Select(
            self.driver.find_element(by=By.XPATH, value="//select[@class='formInputs'and @name='language']"))
        select.select_by_index(1)

#enterin the queryTitle
        title = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[2]/div/div[2]/div/div/form/div[5]/div/input")
        title.send_keys(querytitle)

#entering the queryDescription
        description = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[2]/div/div[2]/div/div/form/div[5]/textarea")
        description.send_keys(querydes)
#selecting the create button
        createBtn = self.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[2]/div/div[2]/div/div/form/div[13]/div/button")
        createBtn.click()
#closing the browser
        self.driver.close()
