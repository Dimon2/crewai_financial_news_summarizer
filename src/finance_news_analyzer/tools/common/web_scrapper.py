import time
from finance_news_analyzer.tools.common.user_agent_generator import UserAgentGenerator
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

class WebScrapper():
    user_agent = UserAgentGenerator()

    def get_web_data(self, url, selector):
        driver = uc.Chrome()
        driver.maximize_window()
        driver.execute_cdp_cmd(f"Network.setUserAgentOverride", {"userAgent": self.user_agent.get_next()})     
        #print(driver.execute_script("return navigator.userAgent;"))
        driver.get(url)
        time.sleep(15)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        data = soup.select(selector)
        driver.close()
        driver.quit()
        return data