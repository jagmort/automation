from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

url_argus = 'http://argus-ktp.pr.rt.ru:8080/argus/'
login = ''
password = ''
level = 'Без деградации'

driver = webdriver.Chrome(ChromeDriverManager().install())

text_file = open("list.txt", "r")
arr = text_file.read().split("\n")
driver.get(url_argus)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_form-username"))
    )
finally:
    driver.find_element_by_id("login_form-username").send_keys(login)
    driver.find_element_by_id("login_form-password").send_keys(password)
    driver.find_element_by_id("login_form-submit").click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mmf-main_menu_bar"]/ul/li/a/span[contains(text(), "Повреждения")]/parent::a'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="mmf-main_menu_bar"]/ul/li/a/span[contains(text(), "Повреждения")]/parent::a').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mmf-create_group_problem"]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="mmf-create_group_problem"]').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="group_interaction_info_form-tab_view-group_interaction_type"]/div[3]/span'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="group_interaction_info_form-tab_view-group_interaction_type"]/div[3]/span').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="group_interaction_info_form-tab_view-group_interaction_type_items"]/li[contains(text(), "ГП СПД-Групповое повреждение СПД")]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="group_interaction_info_form-tab_view-group_interaction_type_items"]/li[contains(text(), "ГП СПД-Групповое повреждение СПД")]').click()

time.sleep(1)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="group_interaction_rule_frame_form-selected_group_problem_rule_type_label"]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="group_interaction_rule_frame_form-selected_group_problem_rule_type_label"]').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="group_interaction_rule_frame_form-selected_group_problem_rule_type_items"]/li[contains(text(), "По сетевому узлу и типу услуги")]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="group_interaction_rule_frame_form-selected_group_problem_rule_type_items"]/li[contains(text(), "По сетевому узлу и типу услуги")]').click()

i = len(arr)
for ip in arr:
    i = i - 1
    print('{0}, {1}'.format(i, ip))

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="group_interaction_rule_frame_form-j_idt1244"]/div/div/label[contains(text(), "Ресурс:")]/parent::div/following-sibling::div/span/input'))
        )
    finally:
        driver.find_element_by_xpath('//*[@id="group_interaction_rule_frame_form-j_idt1244"]/div/div/label[contains(text(), "Ресурс:")]/parent::div/following-sibling::div/span/input').send_keys(ip)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="group_interaction_rule_frame_form-j_idt1244-node_panel"]/table/tbody/tr/td/div/span[contains(text(), "' + ip + '")]'))
        )
    finally:
        driver.find_element_by_xpath('//*[@id="group_interaction_rule_frame_form-j_idt1244-node_panel"]/table/tbody/tr/td/div/span[contains(text(), "' + ip + '")]/../../..').click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id[starts-with(., "group_interaction_rule_frame_form-j_idt")]]/following-sibling::label[contains(text(), " степень влияния")]/preceding-sibling::div/div/span'))
        )
    finally:
        driver.find_element_by_xpath('//div[@id[starts-with(., "group_interaction_rule_frame_form-j_idt")]]/following-sibling::label[contains(text(), " степень влияния")]/preceding-sibling::div/div/span').click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[starts-with(@id, "group_interaction_rule_frame_form-j_idt") and substring(@id, string-length(@id) - string-length("_panel") + 1)  = "_panel"]/div/ul/li[contains(text(), "' + level + '")])[last()]'))
        )
    finally:
        driver.find_element_by_xpath('(//div[starts-with(@id, "group_interaction_rule_frame_form-j_idt") and substring(@id, string-length(@id) - string-length("_panel") + 1)  = "_panel"]/div/ul/li[contains(text(), "' + level + '")])[last()]').click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@id[starts-with(., "group_interaction_rule_frame_form-j_idt")]]/span[contains(text(), "Добавить")]/parent::button'))
        )
    finally:
        driver.find_element_by_xpath('//button[@id[starts-with(., "group_interaction_rule_frame_form-j_idt")]]/span[contains(text(), "Добавить")]/parent::button').click()

    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="group_interaction_info_form-tab_view-group_interaction_rule_table-add_rule_button"]'))
        )
    finally:
        driver.find_element_by_xpath('//*[@id="group_interaction_info_form-tab_view-group_interaction_rule_table-add_rule_button"]').click()

