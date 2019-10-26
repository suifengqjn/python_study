from selenium import webdriver



if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = 'https://www.baidu.com'
    driver.get(base_url)