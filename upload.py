from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from pynput.keyboard import Key, Controller
import os
from random import randint

sleep(randint(59, 3539))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=/home/server/.config/google-chrome/")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.instagram.com/')

for i in range(1):
    driver.implicitly_wait(10)
    sleep(5)
    driver.find_element(by=By.XPATH, value='(//div[@class="x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1lq5wgf xgqcy7u x30kzoy x9jhf4c"])[7]').click()
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element(by=By.XPATH, value='//button[@class="_acan _acap _acas _aj1-"]').click()
    sleep(3)

    def getVid():
        with open('vidCounter.txt') as f:
            latestVid = f.readline()

        currentVid = int(latestVid) + 1
        
        return currentVid


    currentVid = getVid()
    sleep(1)
    keyboard = Controller()
    keyboard.type(f'/home/server/Downloads/ig-bot/videos/{currentVid}.mp4')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)

    driver.find_element(by=By.XPATH, value='(//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1y1aw1k x1sxyh0 xwib8y2 xurb0ha x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh xl56j7k"])[1]').click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='(//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz"])[3]').click()
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Next')]").click()
    driver.implicitly_wait(20)
    driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Next')]").click()
    driver.implicitly_wait(20)
    sleep(1)
    driver.find_element(by=By.XPATH, value='//div[@class="xw2csxc x1odjw0f x1n2onr6 x1hnll1o xpqswwc xl565be x5dp1im xdj266r x11i5rnm xat24cr x1mh8g0r x1w2wdq1 xen30ot x1swvt13 x1pi30zi xh8yej3 x5n08af notranslate"]').send_keys(f'posting daily until I won nobel price, day {currentVid} \n\n #meme #memes #fun #funny #joke #jokes #memepage #memepages #haha')
    sleep(1)
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//*[contains(text(), "Share")][@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37"]').click()
    sleep(45)

    print('----POSTED----')
    os.remove(f'videos/{currentVid}.mp4')
    with open('vidCounter.txt', 'w') as f:
        f.writelines(str(currentVid))
    
    driver.find_element(by=By.XPATH, value='(//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81"][@role="button"])[9]').click()
