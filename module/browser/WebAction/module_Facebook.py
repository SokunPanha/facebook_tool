import random
import time
import requests
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .module_webaction_interface import WebsiteActions
from selenium.webdriver.support import expected_conditions as EC
from utils import WebDriverHelper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
import threading

class FacebookActions(WebsiteActions):
    def __init__(self):
        self.keyboard = Controller()
        self.lock = threading.Lock()


    def perform_actions(self, driver, task_info):
        self.bot = WebDriverHelper()
        action = task_info.get("action")
        params = task_info.get("params", {})
        if action in self.actions_mapping:
            self.actions_mapping[action](self,driver, params)
    def Get2FACode(self,code):
        url = f"https://2fa.live/tok/{code}"

        payload = {}
        headers = {
        'authority': '2fa.live',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_gcl_au=1.1.594402403.1706617983; _gid=GA1.2.1934874214.1706617983; _gat_gtag_UA_78777107_1=1; _ga_R2SB88WPTD=GS1.1.1706617982.1.1.1706618345.0.0.0; _ga=GA1.2.1777250095.1706617983',
        'if-none-match': 'W/"12-rDHV9VRhFRYjso2EuHBUd/z6Yyc"',
        'referer': 'https://2fa.live/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        token = json.loads(response.text)
        return token["token"]
    def login_with_2fa(self, driver, params):
        key = params["key"]
        code = self.Get2FACode(key)
        driver = self.close_vpn_page(driver, "https://www.facebook.com")        
        time.sleep(random.uniform(0.5, 0.1))
        self.bot.wait_and_type(driver, By.ID, "email",params["email"])
        self.bot.wait_and_type(driver, By.ID, "pass",params["password"])
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//button[@data-testid='royal_login_button']").click()
        driver.implicitly_wait(5)
        self.bot.wait_and_type(driver, By.ID, "approvals_code", code)
        time.sleep(2)
        self.bot.wait_and_click(driver, By.ID, "checkpointSubmitButton")
        time.sleep(2)
        self.bot.wait_and_click(driver, By.ID, "checkpointSubmitButton")
        time.sleep(10000)
        
   
# Add a short delay for demonstration purposes
    def login(self, driver, params):
        driver = self.close_vpn_page(driver, "https://www.facebook.com")        
        time.sleep(random.uniform(0.5, 0.1))
        self.bot.wait_and_type(driver, By.ID, "email",params["email"])
        self.bot.wait_and_type(driver, By.ID, "pass",params["password"])
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//button[@data-testid='royal_login_button']").click()
        time.sleep(1000)
    def wait_for_content_load(self, driver, timeout=10):
        # Wait for the document.readyState to be 'complete'
        WebDriverWait(driver, timeout).until(lambda d: driver.execute_script("return document.readyState") == "complete")
    def smooth_scroll(self, driver, scroll_direction, pixels_to_scroll):
        duration = random.uniform(0.8, 1.5)  # Randomize the duration of the scroll
        current_scroll_y = driver.execute_script("return window.scrollY")
        end = current_scroll_y + pixels_to_scroll if scroll_direction == "down" else current_scroll_y - pixels_to_scroll

        script = f"""
            var start = window.scrollY;
            var end = {end};
            var startTime = performance.now();

            function scroll() {{
                var currentTime = performance.now();
                var progress = (currentTime - startTime) / ({duration * 1000});

                if (progress < 1) {{
                    window.scrollTo(0, start + progress * (end - start));
                    requestAnimationFrame(scroll);
                }} else {{
                    window.scrollTo(0, end);
                }}
            }}

            scroll();
        """
        driver.execute_script(script)

    def scroll_randomly(self, driver, scrolling=True):
        while scrolling:
            # Randomly determine whether to scroll up, down, or not at all
            scroll_decision = random.choices(["up", "down", "none"], weights=[0.2, 0.6, 0.2])[0]

            if scroll_decision in ["up", "down"]:
                # Scroll up or down with a faster speed
                pixels_to_scroll = int(random.uniform(3000, 8000) / 10)
                self.smooth_scroll(driver, scroll_direction=scroll_decision, pixels_to_scroll=pixels_to_scroll)

            time.sleep(random.uniform(1, 2))  # Random delay between scrolls

            # Wait for content to load before continuing
            self.wait_for_content_load(driver)

            # Use WebDriverWait to wait for the stopping condition
            try:
                WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.XPATH, "//some-xpath")))
                print("Stopping condition met. Exiting scroll loop.")
                break
            except:
                pass
    def active_on_facebook(self, driver, scrolling=True):
        
        
        driver.get("https://www.whoer.com")
        element = self.bot.wait_for_element(driver, By.XPATH, "//*[contains(text(), 'United States')]")
        # print(driver.current_url)
        original_tab_handle = driver.window_handles[1]
        driver.switch_to.window(original_tab_handle)
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        if element:
           driver.get("https://www.facebook.com")
           driver.implicitly_wait(4)           
        # Wait for the initial content to load before starting scrolling
           self.scroll_randomly(driver, scrolling=True)
           time.sleep(10000)

    def close_vpn_page(self,driver, url):
        driver.get(url)
        # print(driver.current_url)
        original_tab_handle = driver.window_handles[1]
        driver.switch_to.window(original_tab_handle)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return driver

    def custom_action(self, driver, params):
        # Add your custom action logic here
        print(f"Executing custom action with parameters: {params}")
    def post_and_active(self,driver,param):
            driver = self.close_vpn_page(driver,"https://www.facebook.com")
            driver.implicitly_wait(4)           
            driver.find_element(By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft' and text()='Photo/video']").click()
           
            driver.implicitly_wait(20)
            paragraph_element = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
            driver.implicitly_wait(20)
    # Input text into the <p> element
            paragraph_element.send_keys("Have a good day!")
            with self.lock:
                drag_and_drop_element = driver.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1pg5gke xvq8zen xo1l8bm xi81zsa x2b8uid' and text()='or drag and drop']")
                driver.implicitly_wait(20)
                drag_and_drop_element.click()
                time.sleep(random.uniform(2, 5))
                self.keyboard.type("D:\\facebook\\group-post\\auto_post\\app\\image\\pic2.jpeg")
                self.keyboard.press(Key.enter)
                self.keyboard.release(Key.enter)
                time.sleep(4)

        # Find the post_button and perform the action within a lock
            with self.lock:
                post_button = driver.find_element(By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft' and (text()='Post' or text()='Next')]")
                if post_button.text == "Next":
                    post_button.click()
                    driver.implicitly_wait(10)
                    driver.find_element(By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft' and text()='Post']").click()
                else:
                    driver.implicitly_wait(10)
                    time.sleep(3)
                    post_button.click()
                # span_element.send_keys(os.getcwd()+"\\image\\pic1.jpg")
            driver.implicitly_wait(10)
            self.scroll_randomly(driver, scrolling=True)
            print("scrolled")
                # driver.find_element(By.XPATH, "//div[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h']/span").click()
            time.sleep(1000000)    
    # Define the mapping of actions to methods
    actions_mapping = {
        'active': active_on_facebook,
        'custom': custom_action,
        "login" : login,
        "login_2fa" : login_with_2fa,
        "post_active": post_and_active
        # Add more actions as needed
    }
