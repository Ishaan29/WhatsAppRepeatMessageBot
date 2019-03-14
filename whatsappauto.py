from progress.bar import Bar
import time
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options

class WhatsAppBot():
    MESSAGE = 'BHAI KOI COOLER BHAR DO PLZ' 
    REPEAT = 20
    PERSON = 'Roomies'
    ENTER_KEY = u'\ue007'
    URL = 'https://web.whatsapp.com/'
    def __init__(self):
        '''
        initilizes headless browser and chrome instace.
        '''
        opts = Options()
        opts.set_headless()
        self.browser = Chrome(options = opts)
        self.browser.get(self.URL) 

    def send_message(self):
        '''
        send_message: finds search bar, PERSON identifier
                      and message box.
                      sends a message REPEAT times.
        '''
        time.sleep(10)
        search = self.browser.find_element_by_class_name('jN-F5')
        search.send_keys(self.PERSON)
        time.sleep(10)
        search_result = self.browser.find_element_by_class_name('Qgzj8')
        search_result.click()
        text_box = self.browser.find_element_by_class_name('_2S1VP')
        bar = Bar("Processing", max = 20)
        for i in range(self.REPEAT):
            text_box.send_keys(self.MESSAGE)
            text_box.send_keys(self.ENTER_KEY)
            bar.next()
        bar.finish()

if __name__ == '__main__':
    bot = WhatsAppBot()
    bot.send_message()
