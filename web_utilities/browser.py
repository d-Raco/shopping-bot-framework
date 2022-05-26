import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
import time

class Browser():
    '''Class used to manage a selenium webdriver.
    
    Attributes:
        - driver: selenium.webdriver.Firefox
            Firefox webdriver instance.
    
    Methods: 
        - start_driver: None
            Start a private, GUI-less, Firefox driver.
        - get_html: str
            Access a specific URL and get its HTML page source.
        - get_html_delayed: None
            Same as get_html, but waiting a few seconds in case the page requires a specific loading time.
        - stop_driver: None
            Stops the driver.'''
    
    driver = None

    def start_driver(self):
        '''Start a private, GUI-less, Firefox driver.
    
        Arguments:
            - self: web_utilities.Browser
                Instance of this class.
        
        Return: None'''
        
        opt = Options()
        opt.add_argument('--headless')
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.privatebrowsing.autostart', True)

        self.driver = webdriver.Firefox(options=opt, firefox_profile=profile)

    def get_html(self, url):
        '''Access a specific URL and get its HTML page source.
    
        Arguments:
            - self: web_utilities.Browser
                Instance of this class.
            - url: str
                Website link to access.
        
        Return: 
            - str
                HTML page source.'''
        
        self.driver.get(url)
        return self.driver.page_source

    def get_html_delayed(self, url, delay):
        '''Access a specific URL, wait for delay and get its HTML page source.
    
        Arguments:
            - self: web_utilities.Browser
                Instance of this class.
            - url: str
                Website link to access.
            - url: int
                Seconds to wait before fetching the page source.
        
        Return: 
            - str
                HTML page source.'''
        
        self.driver.get(url)
        time.sleep(delay)
        return self.driver.page_source

    def stop_driver(self):
        '''Quit the driver.
    
        Arguments:
            - self: web_utilities.Browser
                Instance of this class.
        
        Return: None'''
        
        self.driver.quit()
