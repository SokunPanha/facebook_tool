from module_webaction_interface import Action
from utils import WebDriverHelper
import time
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import random
from appium.webdriver.common.touch_action import TouchAction
from utils.TowFA import Get2FACode
import math
class LDPlayerActions(Action):
      def __init__(self):
            self.bot = WebDriverHelper()
            
      def perform_actions(self, task_info):
            action = task_info.get("action")
            params = task_info.get("params", {})
            if action in self.actions_mapping:
                  self.actions_mapping[action](self,params)
      def initialize_appium_server(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'automationName': 'UiAutomator2',
        }

        appium_server_url = f'http://localhost:4723/wd/hub'

        driver = webdriver.Remote(appium_server_url, 
            options=AppiumOptions().load_capabilities(desired_caps))
        return driver
      
      def coor_click(self,num_video):
            
            table = 9
            row = range(0, math.ceil(num_video / 3))
            col =range(0,3)
            # print(row)
            coord = []
            n = 0
            for i in row:
                x = 200
                y = 600 + i * 300
                for j in col: 
                    n  = n+1
                    if n<=table:
                        x = x + j*150
                        print(f'{n}ROW {i}{x,y}')
                        coord.append({"x":x, "y":y})
            return coord

      def random(self,start,end):
           time.sleep(random.uniform(start,end))
      def human_clicking(self,driver,element):
          TouchAction(driver).tap(element).perform()
          self.random(0.2,1)
      def human_typing(self, element,text):
           for char in text:
                element.send_keys(char)
                self.random(0.1,0.3)
           self.random(0.5,1)
      def reel_post(self,params):
           driver = self.initialize_appium_server()
           driver.implicitly_wait(20)
           open_facebook = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@content-desc='Facebook']")
           open_facebook.click()
           try:
                num_video  = self.coor_click(params["num_video"])
                print(type(num_video))
                print(num_video)
                # time.sleep(100)
                for coord in num_video:
                    driver.implicitly_wait(10)
                    add_btn = driver.find_element(AppiumBy.XPATH, "(//android.view.View[@resource-id='com.facebook.katana:id/(name removed)'])[1]")
                    self.human_clicking(driver, add_btn)
                    driver.implicitly_wait(10)
                    reels_btn = driver.find_element(AppiumBy.XPATH, "//android.widget.GridView/android.view.ViewGroup[2]/android.view.ViewGroup[1]")
                    self.human_clicking(driver, reels_btn)
                    driver.implicitly_wait(10)
                    # time.sleep(1000)
                    driver.tap([(coord["x"], coord["y"])])
                    driver.implicitly_wait(10)
                    next_button = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Next']")
                    time.sleep(2)
                    self.human_clicking(driver, next_button)
                    description = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Describe your reel. You can also add hashtags here…']")
                    description.send_keys(params["description"])
                    driver.implicitly_wait(10)
                    share_now = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Share now']")
                    self.human_clicking(driver, share_now)
                    time.sleep(5)



           except:
                print("error")
                
           
      def login_2fa(self, params):
            key = Get2FACode(params["key"])
            driver = self.initialize_appium_server()
            try:
                driver.implicitly_wait(20)
                open_facebook = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@content-desc='Facebook']")
                open_facebook.click()

            #     driver.implicitly_wait(10)
            #     email_box = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Mobile number or email']")
            #     self.human_clicking(driver,email_box)

            #     driver.implicitly_wait(10)
            #     email = driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.facebook.katana:id/(name removed)'])[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")
            #     email.send_keys(params["email"])

            #     pass_box = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Password']")
            #     self.human_clicking(driver,pass_box)

            #     password = driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.facebook.katana:id/(name removed)'])[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")
            #     password.send_keys(params["password"])

            #     login_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Log in']/android.view.ViewGroup")
            #     self.human_clicking(driver, login_button)

            # #     new page 
            #     driver.implicitly_wait(10)
            #     tryanother_way = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Try another way']/android.view.ViewGroup")
            #     self.human_clicking(driver, tryanother_way)

            # #     new page 
            #     driver.implicitly_wait(10)
            #     auth_button = driver.find_element(AppiumBy.XPATH, "//android.widget.RadioButton[@content-desc='Authentication app, Get a code from the app you set up.']")
            #     self.human_clicking(driver, auth_button)

            #     auth_next_btn = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Continue']/android.view.ViewGroup")
            #     self.human_clicking(driver, auth_next_btn)


            #     #new 
            #     driver.implicitly_wait(10)
            #     code = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Continue']/android.view.ViewGroup")
            #     self.human_clicking(driver, code)

            #     code_input = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            #     code_input.send_keys(key)

            #     code_next = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Continue']/android.view.ViewGroup")
            #     self.human_clicking(driver, code_next)


            # #     new page 
            #     driver.implicitly_wait(10)
            #     save_btn = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Save']/android.view.ViewGroup")
            #     self.human_clicking(driver, save_btn)
                time.sleep(300)
            #     new page 
                skip = driver.find_element(AppiumBy.XPATH, "//android.view.View[@text='Skip']")
                self.human_clicking(driver, skip)
                # Your additional actions can be added here

                time.sleep(1000)  # Example wait time, replace with your logic
            except Exception as msg:
                  print(msg)
           
      
      actions_mapping = {
        "login_2fa" : login_2fa,
        "post_reels": reel_post
        # Add more actions as needed
      }
            
            
            