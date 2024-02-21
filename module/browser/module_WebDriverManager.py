from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import threading
import os
from .WebAction import FacebookActions
from .utils import config
from ..profileManager import ProfileManager
class WebDriverManager:
    def __init__(self):
        self._threads = []
        self._facebook_actions = FacebookActions()
        self._user_tasks = {}
        self._upload_tasks = ProfileManager()

    def initialize_webdriver(self, folder_name):
        options = webdriver.ChromeOptions()
        path = os.path.join(os.getcwd(), f'profile\\{folder_name}')
        options.add_argument(f"user-data-dir={path}")
        options.add_extension(config.env["vpn"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_experimental_option("excludeSwitches",["enable-automation"])
        # print(path)
        service = Service(config.env["driver"])  # Path to your chrome profile
        driver = webdriver.Chrome(service=service, options=options)
        # driver.maximize_window()
        driver.set_window_size(400,800)
        # driver.set_window_size(600,800)
        return driver

    def run_instance(self, profile_path, website_actions, user_tasks):
        driver = self.initialize_webdriver(profile_path)
        
        for task_info in user_tasks.get(profile_path, []):
          
            
            # if action == "post_active":
            #     # Ensure post_and_active runs sequentially
            #     website_actions.post_and_active(driver, params)
            # else:
                # For other actions, run them concurrently
            thread = threading.Thread(target=website_actions.perform_actions, args=(driver, task_info))
            self._threads.append(thread)
            thread.start()

        # Wait for all other threads to finish before quitting the driver
        for thread in self._threads:
            thread.join()

        driver.quit()

    def create_threads(self, user_tasks, website_actions):
        for profile_path in user_tasks.keys():
            thread = threading.Thread(target=self.run_instance, args=(profile_path, website_actions, user_tasks))
            self._threads.append(thread)

    def start_threads(self):
        for thread in self._threads:
            thread.start()

    def wait_for_threads(self):
        for thread in self._threads:
            thread.join()
    def upload_user_tasks(self, tasks):
        self._user_tasks = self._upload_tasks.initial_task(tasks)
        print(self._user_tasks)

    def start_service(self):
    # Create an instance of the WebDriverManager clas  
        # Create threads for each user and perform Facebook actions
        try: 
               if self._user_tasks["data"] != None:
                    self.create_threads(self._user_tasks['data'], self._facebook_actions)

                    # Start the threads
                    self.start_threads()

                    # Wait for all threads to finish
                    self.wait_for_threads()
               else:
                   raise ValueError("user task not found!")
        except ValueError as err: 
            print(err)
# Example usage:
# user_tasks = {
#     "SokunICT": [
#         {"action": "post_active", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
#         # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
#     ],
#     "Alison": [
#         {"action": "post_active", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
#         # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
#     ],
#     "JameSmith":[
#      {"action": "post_active", "params": {"email": "jack.jack.son96@outlook.com", "password":"JackSon@#$", "key":"Y36C5TCV5XCPYYX2LOHDX6P3YWSYMHHQ"}},    # "john": {"action": "post", "params": {"username": "https://www.youtube.com/"}},
#     ],
#     "OliverJonh":[
#      {"action": "post_active", "params": {"email": "jack.jack.son98@outlook.com", "password":"JackSon@#$", "key":"WBX4BLYYJGCERM5755VJHOO34XP6HKLE"}},    # "john": {"action": "post", "params": {"username": "https://www.youtube.com/"}},
#     ]
#     # ... Other profiles
# }
            
            

# Create an instance of the WebsiteActions class for Facebook
