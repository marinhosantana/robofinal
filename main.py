from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Firefox()
driver.get("https://etherscan.io/tx/0xcc22fc0c43eb8c6a88ce92fd344108cf8f690c21da57a3fb0d8dadcd207d5de3")