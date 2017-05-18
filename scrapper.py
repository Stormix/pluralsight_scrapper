# @Author: Anas Mazouni <Stormix>
# @Date:   2017-05-17T23:59:31+01:00
# @Email:  madadj4@gmail.com
# @Project: PluralSight Scrapper V1.0
# @Last modified by:   Stormix
# @Last modified time: 2017-05-18T03:21:42+01:00

import selenium as sl
import os,time,inspect
from sys import platform
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import config
from slugify import slugify
from clint.textui import progress
import requests
link = "https://app.pluralsight.com/player?course=nodejs-express-web-applications&author=jonathan-mills&name=nodejs-express-web-applications-m1&clip=0&mode=live"



class PluralCourse:
    """
        Course Class.
    """
    link = ""
    title = ""
    browser = ""
    delay = 3
    Username = config.Username
    Password = config.Password
    output = "Download" #output folder
    def __init__(self,link):
        self.link = link

    def launchBrowser(self):
        assert not self.browser, "Browser already set !"
        # Initiate the Browser webdriver
        currentfolder = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        # Check which operating system is being used !
        if platform == "linux" or platform == "linux2":
            # linux
            chrome_driver = currentfolder+"/chromedriver"
        elif platform == "win32":
            # Windows
            chrome_driver = currentfolder+"/chromedriver.exe"
        self.browser = webdriver.Chrome(chrome_driver)
        Browser = self.browser
        Website = self.link
        # Open Pronote
        Browser.get(Website)
        print("Browser Initiated !")
        print("Loading .. " + Website, end =' ')
        time.sleep(self.delay)
        print(u'\u2713')

    def checkLoginAlert(self):
        try:
            self.browser.find_element_by_css_selector(".ps-button-primary-md.mr-lg")
        except NoSuchElementException:
            return False
        return True

    def pausePlayback(self):
        body = self.browser.find_element_by_css_selector("body");
        body.send_keys(Keys.SPACE);

    def login(self):
        assert self.checkLoginAlert(), "Already logged in !"
        loginButton = self.browser.find_element_by_css_selector(".ps-button-primary-md.mr-lg")
        # Go to login page
        loginButton.click()
        # Define the login form
        Browser = self.browser
        usernameInput = "Username"
        passwordInput = "Password"
        LoginButtonClass = ".button.primary"
        # Fill in the login form
        username_log = Browser.find_element_by_id(usernameInput)
        password_log = Browser.find_element_by_id(passwordInput)
        username_log.send_keys(self.Username)
        password_log.send_keys(self.Password)
        # Click the connect buttun
        print("Logging in ...",end=" ")
        Browser.find_element_by_css_selector(LoginButtonClass).click()
        time.sleep(self.delay)
        self.pausePlayback()
        print(u'\u2713')

    def fetchModules(self):
        #Create output folder
        self.createDir(self.output)

        titlesClass = ".m-0.p-0.ps-color-white.ps-type-sm.ps-type-weight-medium"
        moduleClass = ".module"
        episodesListClass = "ul.clips.m-0.p-0"
        modules = {}
        modulesSections = [elt.click() for elt in self.browser.find_elements_by_css_selector(moduleClass)] # Click all sections
        ModuleTitles = [element.text for element in self.browser.find_elements_by_css_selector(titlesClass)] # Looping through each title
        #Fetching the modules episodes lists
        Modules = self.browser.find_elements_by_css_selector(episodesListClass)
        for i in range(len(Modules)):
            #Create output folder
            self.createDir(self.output+"/"+slugify(ModuleTitles[i]))
            #For each list items(li) in the each list(ul) ,Get the titles (h3)
            ModuleEpisodesList = [elt.find_element_by_tag_name('h3').text for elt in [elt for elt in Modules[i].find_elements_by_tag_name('li')]]
            for j in range(len(ModuleEpisodesList)):
                self.createDir(self.output+"/"+slugify(ModuleTitles[i])+"/"+slugify(ModuleEpisodesList[j]))
                # Get the episode elemnt
                self.browser.find_element_by_xpath("//*[contains(text(), '"+ModuleEpisodesList[j]+"')]").click()
                time.sleep(self.delay*1.5)
                print("Downloaded : ",self.getVideoLink())
            # Store the module title and episodes list
            modules[ModuleTitles[i].replace(" ", "_")] = ModuleEpisodesList
        self.pausePlayback()
        return modules

    def getVideoLink(self):
        video_elt = self.browser.find_element_by_tag_name('video')
        link = video_elt.get_attribute("src")
        return link

    def createDir(self,Dir):
        if not os.path.exists(Dir):
            os.makedirs(Dir)
            print("<"+Dir+"> folder created !")

    def download(self,url,path):
        r = requests.get(url, stream=True)
        with open(path, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
# Testing !
test = PluralCourse(link)
test.launchBrowser()
test.login()
down = test.getVideoLink()
print(down)
test.download(down,"test.mp4")
