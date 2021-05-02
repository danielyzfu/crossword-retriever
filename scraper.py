
'''
Web automation tool to take and save a screenshot of LA Times crossword using Selenium

TODO: improve input validation
'''

import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Change this line depending on your chosen browser
from selenium.common.exceptions import SessionNotCreatedException

from chronos import getDailyURL, getURL, getParsedDate, wait

#Set up webdriver options
chrome_options = Options()
chrome_options.add_argument('--headless') #Might be helpful to turn this off if debugging, but otherwise should be kept on for proper screenshots and general ease of use
chrome_options.add_argument("--window-size=1200,1400")
chrome_options.add_argument("--hide-scrollbars")

webdriver_path = r"/PATH/to/webdriver"
#Path to webdriver

folder_path = r"/PATH/to/folder"
#Path to folder where .pngs are saved

try:
    #My chosen browser is headless Chrome, match webdriver to match your chosen browser and change path
    driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
except SessionNotCreatedException:
    print("Failed to make session. Check that Chromedriver is up to date.")
    sys.exit()
except:
    print("Unknown error when creating session. Check that path to webdriver is correct.")
    exit()

def error(message):
    print(message)
    driver.quit()
    return

def getCrossword(code):
    try:
        print('GO TO CROSSWORD ID: ' + code)
        driver.get(getURL(code))
        wait()
        print('ARRIVED AT ' + driver.title)
        filename = driver.title
    except:
        error("ERR NAVIGATION FAILED")
        return

    wait()

    #4/25/21: LA Times removed info modal
    # try:
    #     driver.find_element_by_xpath('//*[@id="info-modal"]/div/div/div[1]/button').click()
    #     print("CLOSE INFO MODAL")
    # except:
    #     error("ERR FAIL CLOSE INFO MODAL")

    # wait()

    try: 
        driver.find_element_by_link_text('Print').click()
        print("OPEN PRINT MODAL")
    except:
        error("FAIL OPEN PRINT MODAL")
        return
        
    wait()

    try: 
        driver.find_element_by_id('print-button').click()
        print("OPEN PRINT FRIENDLY")
    except:
        error("FAIL OPEN PRINT FRIENDLY")
        return

    wait()

    try:
        driver.switch_to.window(driver.window_handles[1]) #Switch active window to print-friendly page
        print("SWITCH ACTIVE WINDOW")
    except:
        error("FAIL SWITCH ACTIVE WINDOW FAIL")
        return

    wait()

    try:
        #Save screenshot to designated folder as .png
        driver.save_screenshot(folder_path + filename + '.png')
        print("SCREENSHOT")
        
    except:
        error("FAIL SCREENSHOT")
        return

    driver.quit()
    print("QUIT DRIVER") #Done

def main():
    kick=False
    while kick==False: #Clunky input validatioon
        try:
            x = input('Enter ID (yymmdd) for specific crossword or any string of letters for daily crossword: ')
            if(x.isdigit()):
                print('is int')
                if (len(x) == 6):
                    print('ID IS ' + x)
                    print('RETRIEVING CROSSWORD ID ' + x)
                    getCrossword(x)
                    kick=True
                else:
                    print('INVALID ID')
            else:
                print('RETRIEVING DAILY CROSSWORD')
                getCrossword(getParsedDate())
                kick=True
        except:
            print('INVALID INPUT')
            continue

if __name__ == '__main__':
    main()