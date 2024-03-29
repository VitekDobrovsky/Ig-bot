from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from moviepy.editor import *
import glob

# TODO:
# meantion author in descriptions
# call download when run out of videos


# selenium init
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=/home/server/.config/google-chrome/")
driver = webdriver.Chrome(options=chrome_options)

reelUrl = []

def unsaveAndDownload(num):
    
    # find post in your saved collection
    driver.get('https://www.instagram.com/vitek.dobrovsky/saved/all-posts/')
    sleep(4)
    div = driver.find_elements(by=By.XPATH, value='//div[@class="_aabd _aa8k  _al3l"]')
    div[0].find_element(by=By.TAG_NAME, value='a').click()

    # unsave videos and save URL to list
    for i in range(num):
        sleep(2)
        reelUrl.append(driver.current_url)
        sleep(1)
        driver.find_element(by=By.XPATH, value='(//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81"])[5]').click()
        if i == 0:
            index = 1
        else:
            index = 2
        driver.find_element(by=By.XPATH, value=f'(//button[@class="_abl-"])[{str(index)}]').click()
    
    print('-------URLs COLLECTED-------')
    # download videos
    download(reelUrl)

def download(reelUrl):

    # get to ig source page
    reelUrl = deepHtmlLinks(reelUrl)

    index = 0
    for link in reelUrl:
        driver.get(link)
        sleep(4)

        # finding video source URL and downloading it
        text = driver.find_element(by=By.XPATH, value='//pre').get_attribute("innerHTML")
        text = str(text)
        try:
            text = text.split('"type":101')[1]
            text = text.split('","id"')[0]
            text = text.split('"url":"')[1]
            downloadUrl = text.replace('amp;', '')
            urllib.request.urlretrieve(downloadUrl, f'videos/{str(index)}.mp4')
            index += 1
            print(f'done - {link}')
        except:
            print(f'error - {link}')
    
    print('-------DOWNLOADED-------')

def edit():
    rawPath = 'raw/'
    editedPath = 'edited/'
        
    for name in os.listdir(rawPath):
        # complete locations
        fullRawPath = rawPath + name
        fullEditedPath = editedPath + name

        # import (from raw)
        video = VideoFileClip(fullRawPath)
        audio = video.audio

        # adding potato and audio
        potato = ImageClip("sources/potato.png").set_start(0).set_duration(video.duration).set_pos(("left","center")).resize(height=130)      
        potato = potato.fx( vfx.colorx, 0.5)
        final = CompositeVideoClip([video, potato])
        sound = AudioFileClip('sources/boom.mp3').set_start(0)

        new_audio = CompositeAudioClip([audio, sound])
        final.audio = new_audio

        # export (to edited)
        final.write_videofile(fullEditedPath)

    print('-------EDITED-------')

def deepHtmlLinks(links):
    
    # getting link to IG source code
    newLinks = []
    for link in links:
        newLink = link + '?__a=1&__d=1'
        newLinks.append(newLink)
    
    return newLinks

def deleteAll(path):
    dir = path
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

# call functions
def run():
    deleteAll('raw/')
    unsaveAndDownload(120)
    edit()

run()
