from selenium import webdriver
import time

kullanıcı_adı = str(input("Kullanıcı adı : "))

şifre = str(input("Şifre : "))

time.sleep(2)

tarayıcı = webdriver.Firefox()

tarayıcı.get("https://www.instagram.com")

username = tarayıcı.find_element_by_name("username")

passwd = tarayıcı.find_element_by_name("password")

username.send_keys(kullanıcı_adı)

time.sleep(1)

passwd.send_keys(şifre)

time.sleep(1)

giriş = tarayıcı.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")

giriş.click()

time.sleep(8)

tarayıcı.refresh()