
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui


class cargo50:
    def __init__(self, param):
        self.a=[param]
        self.countnum=0
        #self.numlist=[]

    #def start(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.chrome_driver = "C:/carinterface/chromedriver.exe" # Your Chrome Driver path
        self.driver = webdriver.Chrome(self.chrome_driver, options=self.chrome_options)
        self.driver.get('제어할 웹페이지주소')
        #self.driver.implicitly_wait(0.1)
        #두가지입력창끄기
        try:
            okwin=WebDriverWait(self.driver, 0.3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a')))
            #ok2=driver.find_element_by_id("//*[@id='modal-window']/div/div/div[1]/a") #okclick
            self.driver.execute_script("arguments[0].click();", okwin)
            okwin.click()
        except:
            print('fail close')
        #두가지입력창끄기    
        try:
            fuckyou=WebDriverWait(self.driver, 0.3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-window"]/div/div/div[1]/a')))
            self.driver.execute_script("arguments[0].click();", fuckyou)
        except:
            print('fail')
        

        try:
            self.driver.implicitly_wait(0.1)
            self.elem=self.driver.find_element_by_id("schCarNo") #click_exemptionbutton
        except:
            self.driver.implicitly_wait(0.1)
            self.password=self.driver.find_element_by_xpath("//*[@id='loginForm']/li[3]/input")
            self.password.send_keys('4321')
            self.loginb=self.driver.find_element_by_xpath("//*[@id='btnLogin']")
            self.driver.execute_script("arguments[0].click();", self.loginb)
        
       




        try:
            self.driver.implicitly_wait(0.1)
            self.ok=self.driver.find_element_by_id("//*[@id='modal-window']/div/div/div[1]/a") #okclick
            self.driver.execute_script("arguments[0].click();", ok)
        except:
            self.driver.implicitly_wait(0.1)
            self.elem=self.driver.find_element_by_id("schCarNo") #click_exemptionbutton
            self.elem.clear()
            self.elem.send_keys(self.a) #numberinput@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




        self.driver.implicitly_wait(0.1)
        self.searchbox=self.driver.find_element_by_xpath("//*[@id='sForm']/input[3]") #click_searchbutton
        self.driver.execute_script("arguments[0].click();", self.searchbox)

        #searchbox.click()
        #time.sleep(2)

        self.wait = WebDriverWait(self.driver, 0.1).until(EC.presence_of_element_located((By.XPATH,"//*[@id='gridMst']/div[2]/table/tbody")))
        self.table=self.driver.find_element_by_xpath("//*[@id='gridMst']/div[2]/table/tbody").text
        #print('print table = '+ self.table)
        self.slist=self.table.split('\n')
        self.numli=list()
        self.numlist=self.numli
        try:
            for i in self.slist:
                self.slist=i.split(' ')
                self.numli.append(self.slist[1])
        except:
            print("no car")         #if car doesn't exist 
        countnum=len(self.numlist)  #searched car list 
        self.countnum=countnum
        #print("numlist = "+ str(self.numlist))  
        #print("car count ="+ str(self.countnum))
       
    def exempt(self):
        if self.countnum==0:
            print('there is no car')

        elif self.countnum==1:       
            try:
        
                # print('selfcountnum1start')
                # okwin=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a')))
                # #ok2=driver.find_element_by_id("//*[@id='modal-window']/div/div/div[1]/a") #okclick
                # self.driver.execute_script("arguments[0].click();", okwin)
                # okwin.click()
                
                #print('carpy exempt test ')
                exbox=self.driver.find_element_by_xpath("//*[@id='13']")
                exbox=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='13']")))
                self.driver.execute_script("arguments[0].click();", exbox)
                exbox.click()  #click_exemptionbutton
            
                self.driver.execute_script("javascript:fncSetDscntType('3');")
                self.driver.execute_script("hi")           
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
