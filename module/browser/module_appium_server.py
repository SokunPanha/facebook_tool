import subprocess
import threading
from appium import webdriver
from appium.options.common import AppiumOptions
from multiprocessing import Process
import time
from AppAction.LDplayerAction import LDPlayerActions
class AppiumDriver:
    def __init__(self):
        self.threads = []
        self.ldplayer_path = r'D:\LDPlayer\LDPlayer9\dnplayer.exe'
   
    def open_ldplayer_instance(self,ldplayer_index):
        ldplayer_path = r'D:\LDPlayer\LDPlayer9\dnplayer.exe'
        command = [ldplayer_path, f'index={ldplayer_index}']
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(15)  # 
    def close_ldplayer_instance(self):
        command = ['taskkill', '/F', '/IM', 'dnplayer.exe']
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
   
    def run_instance(self,app_action, user_tasks):
        for index in user_tasks.keys():
            ldplayer_process = Process(target=self.open_ldplayer_instance, args=(index))
            ldplayer_process.start()
            time.sleep(10)

            for task_info in user_tasks.get(index, []):
                action = task_info.get("action")
                params = task_info.get("params", {})
                app_action.perform_actions(task_info)
            time.sleep(15)
            self.close_ldplayer_instance()
            ldplayer_process.join()





user_tasks = {
    #  "0":[
    #  {"action": "post_reels", "params": { "num_video": 6, "description":" Trick in Agriculture!! #agriculture #farmersmarket #farmer #farming #farmlife " ,"email": "jack.jack.son98@outlook.comm", "password":"JackSon@#$", "key":"WBX4BLYYJGCERM5755VJHOO34XP6HKLE"}},    # "john": {"action": "post", "params": {"username": "https://www.youtube.com/"}},
    # ],

    # "1": [
    #     {"action": "post_reels", "params": {"num_video": 6, "description":" Do you love me! #viralvideo #viralvideo #viralreels #virals #shorts #fyp #fypシviral  #reelsvideo #reels #reelsviral #reelsfb #reels2023 #videoviral #viralpost " ,"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
    #     # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
    # ],
    #   "2": [
    #     {"action": "post_reels", "params": {"num_video": 1, "description":" It looks so amazing!! #viralvideo #viralvideo #viralreels #virals #shorts #fyp #fypシviral  #reelsvideo #reels #reelsviral #reelsfb #reels2023 #videoviral #viralpost " ,"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
    #     # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
    # ],
    #   "3": [
    #     {"action": "post_reels", "params": {"num_video": 6, "description":" It is time to collect the harvest!! #harvester1270g #harvester #harvest #harvesting #harvesterlover #woodworking #forestry #forest #made #satisfying #viralvideo #viralvideo #viralreels #virals #shorts #fyp #fypシviral  #reelsvideo #reels #reelsviral #reelsfb #reels2023 #videoviral #viralpost " ,"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
    #     # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
    # ],
      "4": [
        {"action": "post_reels", "params": {"num_video": 6, "description":" hilarious kid!! #kidsactivities #kids #kidsfashion #kidstoys #kidswear #kidsphotography #cutekidsclub #viralvideo #viralvideo #viralreels #virals #shorts #fyp #fypシviral  #reelsvideo #reels #reelsviral #reelsfb #reels2023 #videoviral #viralpost " ,"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
        # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
    ],
    # "1": [
    #     {"action": "login_2fa", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
    #     # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
    # ],
}

if __name__ == '__main__':

    Ldplayer =  LDPlayerActions()
    app_server = AppiumDriver()
    app_server.run_instance(Ldplayer, user_tasks)

