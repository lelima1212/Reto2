from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class InstagramScraper:
    def __init__(self, post_url):
        self.post_url = post_url
        self.comments = []
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.chrome = webdriver.Chrome(chrome_options=chrome_options)
    
    def scrape_comments(self):
        browser = self.chrome.get(self.post_url)
        content = self.chrome.page_source
        time.sleep(3)

        while True:
            try:
                self.load_more_comments = self.browser.find_element_by_class_name("XQXOT")
                self.action = ActionChains(self.browser)
                self.action.move_to_element(self.load_more_comments)
                self.load_more_comments.click()
                time.sleep(4)
                self.body_elem = self.browser.find_element_by_class_name('Mr508')
                for _ in range(100):
                    self.body_elem.send_keys(Keys.END)
                    time.sleep(3)
            except Exception as e:
                pass

        time.sleep(5)
        self.comment = self.browser.find_elements_by_class_name('gElp9 rUo9f')
        for c in self.comment:
            self.container = c.find_element_by_class_name('C4VMK')
            self.name = self.container.find_element_by_class_name('_6lAjh ').text
            self.content = self.container.find_element_by_tag_name('span').text
            self.content = self.content.replace('\n', ' ').strip().rstrip()
            self.time_of_post = self.browser.find_element_by_xpath('//a/time').get_attribute("datetime")
            self.comment_details = {'profile name': self.name, 'comment': self.content, 'time': self.time_of_post}
            print(self.comment_details)
            time.sleep(5)
        return self.comment_details
    
post_url = "https://www.instagram.com/p/B166OkVBPJR/"
x = InstagramScraper(post_url)
x.scrape_comments()