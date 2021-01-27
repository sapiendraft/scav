from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from settings import Profile

#   user input for presets and mode to execute


print("Enter navigation mode: 'q' for search, 'u' for url.")
print("*url requires a list of urls defined on the selected PRESET file.")
mode = input()
print("\nSelected mode - {}\n".format(mode))

preset = input("Enter the last digits of the PRESET file of choice: ")
print("\nSelected file 'PRESET_{}.cfg'".format(preset))

usr_profile = Profile(mode, preset)
page_elements = usr_profile.presetLoader()
print(page_elements)

#   MODE URL

def urlAccess(url_list):
    driver = Firefox() #    initialize driver (open browser)
    random_list = [] #    random list for testing purposes
    for link in url_list:
        driver.get(link) #   iterate through the list of links in urls.py
        class_title = driver.find_elements(By.CLASS_NAME, page_elements[4]) #    locate the h3 tag of the headings and store in list
        
        for title in class_title:
            post_title = title.find_element(By.TAG_NAME, "span") #  select the text in span in h3 tag
            random_list.append(post_title)

    driver.quit() #    quit browser
    return random_list



if mode.lower() == "u":
    url_file = input("Enter path to urls.py file (empty for default value): ")
    if url_file == "": #    if path is empty just set to default file path
        url_file = "core/urls.py"
    
    f = open(url_file, "r")
    url_file_list = f.readlines()
    f.close()

    print(urlAccess(url_file_list))