#------------------------------------------------------------------
# For the code to work, you need to remove zoom from your computer.
#------------------------------------------------------------------

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


zoom_url = str(input('Enter the link to the zoom conference -> '))

chromedriver_path=r'   Enter the chromdriver folder   '

# This is where you set the permissions with google.
opt = Options()

opt.add_argument("--disable-infobars")

opt.add_argument("start-maximized")

opt.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block

opt.add_experimental_option("prefs", { \

    "profile.default_content_setting_values.media_stream_mic": 1, 

    "profile.default_content_setting_values.media_stream_camera": 1,

    "profile.default_content_setting_values.geolocation": 1, 

    "profile.default_content_setting_values.notifications": 1 

  })

driver = webdriver.Chrome(executable_path=chromedriver_path,  options=opt)

# The code itself and working with the site zoom
try:
    driver.get(url=zoom_url)

    sleep(3)

    click_to_crest = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[3]/button').click()

    sleep(10)
    driver.find_element(By.CSS_SELECTOR, '.mbTuDeF1').click()
    sleep(5)
    try:
          driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/h3[2]/span/a').click()
    except:
          driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/h3[2]/span/a').click()
    

    sleep(5)
    
    #Disabling the camera and microphone
    micro = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[5]/div[1]/button[1]').click()
    sleep(1)
    cam = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[5]/div[2]/button/i').click()

    sleep (3)
    
    user_name = driver.find_element('id', 'inputname')
    user_name.clear()
    user_name.send_keys(' Enter your name. ')

    sleep(3)

    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block.btn-lg.submit').click()


except Exception as ex:
    pass

#If you do not want the bot to close the browser after 30 seconds, then delete it.
finally:
        sleep(30)
        driver.close()

#Thanks
