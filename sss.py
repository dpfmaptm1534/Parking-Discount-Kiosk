

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui


class cargo:
    def __init__(self, param):
        self.a=[param]
        self.countnum=0
        self.numlist=[]
    def rcn(self):
        return self.numlist
    def start(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "C:/carinterface/chromedriver.exe" # Your Chrome Driver path
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        driver.get('제어할 웹페이지주소')
        driver.implicitly_wait(1)

        try:
            driver.implicitly_wait(1)
            elem=driver.find_element_by_id("schCarNo") #click_exemptionbutton
        except:
            driver.implicitly_wait(1)
            password=driver.find_element_by_xpath("//*[@id='loginForm']/li[3]/input")
            password.send_keys('4321')
            loginb=driver.find_element_by_xpath("//*[@id='btnLogin']")
            driver.execute_script("arguments[0].click();", loginb)

        try:
            driver.implicitly_wait(1)
            ok=driver.find_element_by_id("//*[@id='modal-window']/div/div/div[1]/a") #okclick
            driver.execute_script("arguments[0].click();", ok)
        except:
            driver.implicitly_wait(1)
            elem=driver.find_element_by_id("schCarNo") #click_exemptionbutton
            elem.clear()
            elem.send_keys(self.a) #numberinput@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


        driver.implicitly_wait(1)
        searchbox=driver.find_element_by_xpath("//*[@id='sForm']/input[3]") #click_searchbutton
        driver.execute_script("arguments[0].click();", searchbox)

        #searchbox.click()
        #time.sleep(2)

        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='gridMst']/div[2]/table/tbody")))
        table=driver.find_element_by_xpath("//*[@id='gridMst']/div[2]/table/tbody").text
        print('print table = '+table)
        slist=table.split('\n')
        numlist=list()
        self.numlist=numlist
        try:
            for i in slist:
                sslist=i.split(' ')
                numlist.append(sslist[1])
        except:
            print("no car")         #if car doesn't exist 
        countnum=len(self.numlist)  #searched car list 
        self.countnum=countnum
        print("numlist = "+ str(self.numlist))  
        print("car count ="+ str(self.countnum))
    
    def exempt(self):
        if countnum==0:
            print('there is no car')

        elif countnum==1:       
            try:
                driver.implicitly_wait(3)
                exbox=driver.find_element_by_xpath("//*[@id='3']")
                driver.execute_script("arguments[0].click();", exbox)
                #exbox.click()  #click_exemptionbutton
                
            except:
                print('exempt error')



        #exbox.click()
   
    if __name__ == "__main__":
        __init__(self,param)
        start(self)
    if __name__ == "__main__":
        __init__(self,param)
        exempt(self)
#class countcarnumber:
