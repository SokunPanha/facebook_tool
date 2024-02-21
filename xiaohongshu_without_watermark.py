# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import threading
# import time
# from screeninfo import get_monitors
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import random

# def get_screen_width():
#     monitors = get_monitors()
#     if monitors:
#         return monitors[0].width
#     else:
#         return 800  # Default width if screen information is not available

# def wait_for_element(driver, by, value, timeout=10):
#     return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# def wait_and_click(driver, by, value, timeout=10):
#     element = wait_for_element(driver, by, value, timeout)
#     ActionChains(driver).move_to_element(element).click().perform()
#     time.sleep(random.uniform(1.0, 3.0))  # Increase delay

# def wait_and_type(driver, by, value, text, timeout=20):
#     element = wait_for_element(driver, by, value, timeout)

#     # Wait for the element to be clickable
#     wait = WebDriverWait(driver, timeout)
#     wait.until(EC.element_to_be_clickable((by, value)))

#     for char in text:
#         element.send_keys(char)
#         time.sleep(random.uniform(0.2, 0.5))  # Increase delay

# def run_chrome(window_size, window_position, email, password):
#     options = Options()
#     options.add_argument(f'--window-size={window_size}')
#     options.add_argument(f'--window-position={window_position}')
    
#     driver = webdriver.Chrome(options=options)
#     driver.get("https://facebook.com")
    
#     # wait_and_click(driver, By.XPATH, "//button[text()='sign up for free']")
#     # wait_and_click(driver, By.XPATH, "//button[text()='Continue with VPN Free']")
#     # time.sleep(2)
   
#     # # wait_and_click(driver, By.XPATH, "Email address")
#     # # driver.find_element(By.CLASS_NAME, "input-element").send_keys(email)
#     # wait_and_click(driver, By.XPATH, "//button[text()='Start using Proton VPN']")
#     # time.sleep(5)
#     # driver.find_element(By.ID, "email").send_keys(email)
#     # time.sleep(5)

#     # wait_and_click(driver, By.XPATH, "//button[text()='Start using Proton VPN']")

#     # wait_and_click(driver, By.XPATH, "//button[text()='Choose my own password']")
#     wait_and_type(driver, By.ID, "email", email)

#     wait_and_type(driver, By.ID, "pass", password)


#     # Do whatever operations you need on this instance of Chrome
#     time.sleep(100)  # For demonstration purposes, wait for 100 seconds
    
#     driver.quit()

# # Rest of the code remains the same

# # Set the path to your ChromeDriver executable
# # chrome_driver_path = '/path/to/chromedriver'

# # URLs to open in each Chrome instance along with corresponding emails
# url_email_pairs = [
#     ('nhebpanha40@gmail.com', "JackSon@#$") # Add more URL-email pairs as needed
# ]

# # Calculate the number of rows
# browsers_per_row = 1  # Four browsers in each row
# num_rows = (len(url_email_pairs) + browsers_per_row - 1) // browsers_per_row

# # Get the screen width dynamically
# screen_width = get_screen_width()

# # Window size for each Chrome instance
# window_width = screen_width // browsers_per_row
# window_size = f'{window_width},600'  # You can adjust the height as needed

# # Create threads for each Chrome instance
# threads = []
# for i, (email, password) in enumerate(url_email_pairs):
#     row = i // browsers_per_row
#     col = i % browsers_per_row
#     window_position = f'{col * window_width},0'  # Assuming all browsers have the same height
    
#     thread = threading.Thread(target=run_chrome, args=(window_size, window_position, email, password))
#     threads.append(thread)

# # Start the threads
# for thread in threads:
#     thread.start()

# # Wait for all threads to finish
# for thread in threads:
#     thread.join()



# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# # import threading
# # import time
# # from screeninfo import get_monitors
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import Select
# # from selenium.webdriver.common.action_chains import ActionChains
# # import random

# # def get_screen_width():
# #     monitors = get_monitors()
# #     if monitors:
# #         return monitors[0].width
# #     else:
# #         return 800  # Default width if screen information is not available

# # def run_chrome( window_size, window_position, email, password):
# #     options = Options()
# #     options.add_argument(f'--window-size={window_size}')
# #     options.add_argument(f'--window-position={window_position}')
    
# #     driver = webdriver.Chrome(options=options)
# #     def move_mouse_to_element(driver, element):
# #         ActionChains(driver).move_to_element(element).perform()
# #         time.sleep(random.uniform(1.0, 3.0))  # Increase delay

# #     def simulate_typing(element, text):
# #         for char in text:
# #             element.send_keys(char)
# #             time.sleep(random.uniform(0.2, 0.5))  # Increase delay

# #     def click_with_movement(element):
# #         action = ActionChains(driver)
# #         action.move_to_element(element).click().perform()
# #         time.sleep(random.uniform(1.0, 3.0))  # Increase delay
    
# #     driver.get("https://account.protonvpn.com/signup")
    
# #     # Use the provided email for login or any other operations
# #     # For example, you can locate the email input field and fill it with the provided email
# #     # Replace the following line with your actual code
# #     time.sleep(10)
# #     click_with_movement(driver.find_element(By.XPATH, "//button[text()='sign up for free']"))
# #     time.sleep(4)
# #     click_with_movement(driver.find_element(By.XPATH, "//button[text()='Continue with VPN Free']"))
# #     time.sleep(4)

# #     simulate_typing(driver.find_element(By.ID, "email"), email)
# #     time.sleep(4)
  
# #     click_with_movement(driver.find_element(By.XPATH, "//button[text()='Start using Proton VPN']"))
# #     time.sleep(4)

# #     click_with_movement(driver.find_element(By.XPATH, "//button[text()='Choose my own password']"))
# #     simulate_typing(driver.find_element(By.ID, "password"), password)
# #     simulate_typing(driver.find_element(By.ID, "password-repeat"), password)

    
   
# #     # Do whatever operations you need on this instance of Chrome
# #     time.sleep(100)  # For demonstration purposes, wait for 100 seconds
    
# #     driver.quit()

# # # Set the path to your ChromeDriver executable
# # # chrome_driver_path = '/path/to/chromedriver'

# # # URLs to open in each Chrome instance along with corresponding emails
# # url_email_pairs = [
# #     ('nhebpanha40@gmail.com',"JackSon@#$"), # Add more URL-email pairs as needed
# # ]

# # # Calculate the number of rows
# # browsers_per_row = 4  # Four browsers in each row
# # num_rows = (len(url_email_pairs) + browsers_per_row - 1) // browsers_per_row

# # # Get the screen width dynamically
# # screen_width = get_screen_width()

# # # Window size for each Chrome instance
# # window_width = screen_width // browsers_per_row
# # window_size = f'{window_width},400'  # You can adjust the height as needed

# # # Create threads for each Chrome instance
# # threads = []
# # for i, (email, password) in enumerate(url_email_pairs):
# #     row = i // browsers_per_row
# #     col = i % browsers_per_row
# #     window_position = f'{col * window_width},0'  # Assuming all browsers have the same height
    
# #     thread = threading.Thread(target=run_chrome, args=(window_size, window_position, email, password))
# #     threads.append(thread)

# # # Start the threads
# # for thread in threads:
# #     thread.start()

# # # Wait for all threads to finish
# # for thread in threads:
# #     thread.join()
# import requests

# url = "https://edith.xiaohongshu.com/api/sns/web/v1/user_posted?num=30&cursor=6166f98d000000000102af72&user_id=5dd8d9250000000001008548&image_formats=jpg,webp,avif"

# payload = {}
# headers = {
#   'authority': 'edith.xiaohongshu.com',
#   'accept': 'application/json, text/plain, */*',
#   'accept-language': 'en-US,en;q=0.9',
#   'cookie': 'abRequestId=a641440d-88aa-5d7e-ba16-2826de34d73f; a1=18cf41a863eh1i47tjm0bjgwmjckyib9g73nbesxe50000602252; webId=a09739a18f024fab0f3fbbde88916ba9; gid=yYSi4y0Y0jkDyYSi4y0YKWdMqdxy34W9V68DqCdVkE6VSI28Tv3DjD888K8JJ2J8fJJy8DD4; web_session=040069b4ea8258da3d833c8aab374ba86b4cbc; webBuild=4.1.6; xsecappid=xhs-pc-web; websectiga=8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee; sec_poison_id=19359621-8782-4b7a-9d88-c9015d598c71',
#   'origin': 'https://www.xiaohongshu.com',
#   'referer': 'https://www.xiaohongshu.com/',
#   'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-site',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#   'x-b3-traceid': 'f0b48efa1e933357',
#   'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImU5YmE0MTRkMDA0MzJlYjE3NTRlNGMxNjExNWFiNjllMGZlYmRkZjUwOGNmYTM4MmY0NTk5OTA5YmJkNzdkZDRhNTFmODFjOGYwMWIxNjQzYTQ2MDg5NmU4MGE1YTYzMmM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNWEyZjBhNjI4MTc5MzljNTlhNTM1YzcxMjJiNmNjYzFhNDFjZWVkYWQ1MGEwMjk0NzJjNTJlZWIxNTczYzljYjk2ZTQ5ZjNjMjg1ZTc1NjdkMjg4ODcyNmNiMTQwYTQyNDRhY2EyOWI1MDNmOWVkMTIwNmFjNmNmZDY2YzNlNjI4MmUzMWFmYmMxODQxNWE4NTlkZTJmNWIyYTBlNmJmNzZlZmIzZmM2NGY0NmZhZWZkMzg5OWQ0OGNmMWI0ZWNlYyJ9',
#   'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhhHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHFN0r1+jHVHdWMH0ijP/Y080clG/W9P9piPnDF+7zxJ/mjyf47Jnk0y7SkG0Sd+A+1GfpA2BLMPeZIPeGIP0HMPjHVHdW9H0il+AZ9+0WU+0rhPAZANsQh+UHCHSY8pMRS2LkCGp4D4pLAndpQyfRk/SzbyLleadkYp9zMpDYV4Mk/a/8QJf4hanS7ypSGcd4/pMbk/9St+BbH/gz0zFMF8eQnyLSk49S0Pfl1GflyJB+1/dmjP0zk/9SQ2rSk49S0zFGMGDqEybkea/8QJpLMnnMbPrMLLfT+zrrI/gktJbSxz/+wpbQV/D4+2rExzgYwpF8k/fkVJrMonfl8JpQ3nfkp4FRo/fM8prFF/nM8PrELyApOprrMnnMtyFEC8BTyzbQi/SzBJLRrzfkOzMS7/p4Q2rExLgk8pbrU/Lzd+LETp/z+zFLlnpz82DMT//pyprEknfMayrMgnfY8pr8Vnnk34MkrGAm8pFpC/p4QPLEo//++JLE3/L4zPFEozfY+2D8k/SzayDECafkyzF8x/Dzd+pSxJBT8pBYxnSznJrEryBMwzF8TnnkVybDUnfk+PS8i/nkyJpkLcfS+ySDUnpzyyLEo/fk+PDEk/S4b2pkxcfYwyDDF/pz0+LMCJBkwpBli/Sz+PpSCG7Y+yDkk/fMwySSCzfYwzr8xnS4nyMSgL/b+zFp7/nk3PrECafkwprkVnS4Q2rELG7k82flxnnk3PSkLL/pyyDEx/nkdPpkLGAbwyfz3/nkd+rRrG7SwJLEk/pzz4MSLLgSwzbQin/Qb2LRga/b+zrET/M4nyFMLag4wJL8x/fMwJpkrn/Q82DEV/fkQ+rMTpgk+pF8TnnM+2rRrLgYwpFLF/SzVyMkLafMwpFSEnpzsJrETafMw2SkVnfMQ2SkT//QwzMDI/fMyybkgnfT+2fqM/M4zPrRo/fM+pFDInS4wJbSEa0DjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+Dy7Ylqg4Dag8mqM4sG9Y7LozF89FF+DTp2dYQyemAPrlNq9kl49EE+Fzyag86q7YjLBkEG7pmanYN8LzY+7+fySzLadbFLjTl4FbI8rlIagG3aAYrL94sLoq9a/P98nTM4rY7qg4raLpVqFSiPBph/b+DagY/PFS9+g+g4g4atA4ILok0/d+DJe+S8SmFcLS3/9LApd4dqgbF/omM4oYN2f4APp4C8LSepS4QysVINMmFLLTM4bzQ2BlyqBQt8gYc4BYQcFkA2bmFGDS3y74QyLpFJ7+6qM4dzApsy0pA8S8F+bkj/9p/Jgbi20Z78p4yzF4Q2e4SpMm7JFSk8npf4g4xGDzQpLTd/BEQ2epAP7bFLfEy+9pn80YNanYVGFSbyAYw87bfa/+++obTLpmQyn+k8pmF+LSendGFcDEAzomw8nTM4BlQ2BRAyjRmq9kspAzQyepAynlyLAYl4MpQz/4APnGAqA8gcnpkpdqhnfu7qM4n4e+QcFMc/B468n8M4FbCJ0pApM87qDDAL9EQP7iAqdp7aBbl4AYsGp4CwoQOqFcI/9ph4gzTanVA8pSYN7+h20Y+anYD8nkgPo+3pAzoanDIqAbn4AbQzaTgLopFqDRl4ALjNsQhwaHCP/GUPArUPArA+sIj2erIH0il+/zR',
#   'x-t': '1706682618303'
# }
# response = requests.request("GET", url, headers=headers, data=payload)

# if response.status_code == 200:
#     # Parse the JSON response
#     json_data = response.json()

#     # Extract note_id from each note and create an array of URLs
#     note_ids = [note.get("note_id") for note in json_data.get("data", {}).get("notes", []) if note.get("note_id")]

#     # Create an array of URLs by appending note_id to the base URL
#     xiaohongshu_urls = [f"https://www.xiaohongshu.com/explore/{note_id}" for note_id in note_ids]

#     # Print the array of URLs
#     print("Xiaohongshu URLs:")
#     for url in xiaohongshu_urls:
#         print(url)
# else:
#     print("Error:", response.status_code)
# import requests
# from urllib.parse import quote

# # Original URLs as an array

# # Encode the URLs

# # Encode the URLs
# encoded_urls = [quote(url) for url in original_urls]

# # Initialize an empty list to store video URLs
# all_video_urls = []

# for encoded_url in encoded_urls:
#     url = f"https://api.tiqu.cc/api/all/?url={encoded_url}&token=a49570ecec3848e49474057963f7a211"
#     payload = {}
    # headers = {
    #     'authority': 'api.tiqu.cc',
    #     'accept': 'application/json, text/plain, */*',
    #     'accept-language': 'en-US,en;q=0.9',
    #     'origin': 'https://tiqu.cc',
    #     'referer': 'https://tiqu.cc/',
    #     'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-site',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    # }

#     response = requests.get(url, headers=headers, data=payload)

#     try:
#         # Parse JSON response
#         json_response = response.json()

#         # Extract video URL from the response
#         video_url = json_response.get('url', '')

#         if video_url:
#             all_video_urls.append(video_url)
#             print(f"Video URL for {encoded_url}: {video_url}")
#         else:
#             print(f"No video URL found for {encoded_url}.")
#     except Exception as e:
#         print(f"Error parsing JSON response for {encoded_url}: {e}")
# import requests
# import time
# import ujson
# import logging
# from urllib.parse import quote
# from concurrent.futures import ThreadPoolExecutor, as_completed

# def get_video_url(encoded_url):
#     url = f"https://api.tiqu.cc/api/all/?url={encoded_url}&token=a49570ecec3848e49474057963f7a211"
#     payload = {}
#     headers = {
#         'authority': 'api.tiqu.cc',
#         'accept': 'application/json, text/plain, */*',
#         'accept-language': 'en-US,en;q=0.9',
#         'origin': 'https://tiqu.cc',
#         'referer': 'https://tiqu.cc/',
#         'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
#     }

#     try:
#         with requests.Session() as session:
#             response = session.get(url, headers=headers, data=payload)
#             response.raise_for_status()  # Check for HTTP errors

#             # Parse JSON response
#             json_response = ujson.loads(response.text)

#             # Extract video URL from the response
#             video_url = json_response.get('url', '')

#             if video_url:
#                 logging.debug(f"Video URL for {encoded_url}: {video_url}")
#                 return video_url
#             else:
#                 logging.warning(f"No video URL found for {encoded_url}.")
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error processing {encoded_url}: {e}")
#     except ujson.JSONDecodeError as e:
#         logging.error(f"Error parsing JSON response for {encoded_url}: {e}")

#     return None

# def get_video_urls(original_urls):
#     # Set up logging
#     logging.basicConfig(level=logging.DEBUG)  # Set desired log level

#     # Encode the URLs
#     encoded_urls = [quote(url) for url in original_urls]

#     # Initialize an empty list to store video URLs
#     all_video_urls = []

#     # Use a ThreadPoolExecutor to fetch URLs concurrently
#     with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
#         futures = [executor.submit(get_video_url, url) for url in encoded_urls]

#         # Wait for all futures to complete
#         for future in as_completed(futures):
#             video_url = future.result()
#             if video_url:
#                 all_video_urls.append(video_url)

#     return all_video_urls



# # Example usage:

# # Original URLs as an array
# original_urls = [
#     "https://www.xiaohongshu.com/explore/6117f6960000000021037e33",
#     "https://www.xiaohongshu.com/explore/659e99a6000000001e00b137",
#     "https://www.xiaohongshu.com/explore/659e9992000000001d0165a9",
#     "https://www.xiaohongshu.com/explore/659e9988000000001e0067a1",
#     "https://www.xiaohongshu.com/explore/659e99810000000015001460",
#     "https://www.xiaohongshu.com/explore/659e9973000000001a0281d3",
#     "https://www.xiaohongshu.com/explore/659e9967000000001802b9f6",
#     "https://www.xiaohongshu.com/explore/659e9954000000001d028485",
#     "https://www.xiaohongshu.com/explore/659e9942000000001101df0a",
#     "https://www.xiaohongshu.com/explore/659cb59a000000001d026066",
#     "https://www.xiaohongshu.com/explore/65997a1000000000150027f6",
#     "https://www.xiaohongshu.com/explore/659979fa000000001802872c",
#     "https://www.xiaohongshu.com/explore/659979e80000000018028700",
#     "https://www.xiaohongshu.com/explore/659979d30000000011032fd7",
#     "https://www.xiaohongshu.com/explore/659979be000000001e008094",
#     "https://www.xiaohongshu.com/explore/659979a800000000110157fe",
#     "https://www.xiaohongshu.com/explore/659979920000000011032f45",
#     "https://www.xiaohongshu.com/explore/6596a0eb000000001802a579",
#     "https://www.xiaohongshu.com/explore/6596a0d3000000001d025bf9",
#     "https://www.xiaohongshu.com/explore/6596a0bc000000001102e1aa",
#     "https://www.xiaohongshu.com/explore/6596a09e000000001c01220b",
#     "https://www.xiaohongshu.com/explore/6596a07e0000000015000a06",
#     "https://www.xiaohongshu.com/explore/6596a01c000000001c012077",
#     "https://www.xiaohongshu.com/explore/65969ff8000000001102df7b",
#     "https://www.xiaohongshu.com/explore/65969fdf000000001e005d24",
#     "https://www.xiaohongshu.com/explore/65969fc80000000011030f3e",
#     "https://www.xiaohongshu.com/explore/65969fa8000000001d0158cf",
#     "https://www.xiaohongshu.com/explore/65969f87000000001102de39",
# ]

# video_urls = get_video_urls(original_urls)
# print("All Video URLs:")
# print(video_urls)

# Now, all_video_urls contains the video URLs for each original URL in the array


# Now, all_video_urls contains the video URLs for each original URL in the array

# Encode the URLs

# Now, all_video_urls contains the video URLs for each original URL in the array


# Now, all_video_urls contains the video URLs for each original URL in the array


# import requests
# from urllib.parse import urlparse

# def download_video(url, output_path='.'):
#     try:
#         # Send a GET request to the URL
#         response = requests.get(url)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Extract the file name from the URL using the urlparse method
#             file_name = urlparse(url).path.split('/')[-1]

#             # Combine the output path and file name
#             output_file_path = f"{output_path}/{file_name}"

#             # Save the video content to the specified output path
#             with open(output_file_path, 'wb') as f:
#                 f.write(response.content)

#             print(f"Video downloaded successfully to {output_file_path}")
#         else:
#             print(f"Failed to download video. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# # video_url = 'http://v.xiaohongshu.com/stream/110/258/01e5b72379a18ff2010377038d53634418_258.mp4?sign=0f8a336011f10f97549ce7a709fe45e6&t=65bbc000'
# download_video(video_url)
