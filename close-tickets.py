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
comment = ''
reason = ''

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

i = len(arr)
for ticket in arr:
    i = i - 1
    print('{0}, {1}'.format(i, ticket))
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mmf-bi_search_input"))
        )
    except:
        continue

    driver.find_element_by_id("mmf-bi_search_input").send_keys(ticket)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mmf-bi_search_panel"))
        )
    except:
        continue

    driver.find_element_by_id("mmf-bi_search_input").send_keys(Keys.ENTER)
    
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='gi_header-header_frame']/h3/span[contains(text(), '" + ticket + "')]"))
        )
    except:
        continue

    driver.find_element_by_id('group_def_tab-history_form-new_comment').send_keys(comment)
    driver.find_element_by_id("group_def_tab-history_form-add_comment").click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody[@id='group_def_tab-history_form-history_table_data']/tr/td[contains(text(), 'Добавлен комментарий')]/following-sibling::td/div[contains(text(), '" + comment + "')]"))
    )
    except:
        pass

    try:
        driver.find_element_by_xpath("//div[@id='signal_form-available_transitions']/div[contains(@class, 'ui-selectonemenu-trigger')]/span").click()
    except:
        continue

    try:
        driver.find_element_by_xpath("//li[@data-label='Закрыть']").click()
    except:
        continue

    time.sleep(1)
    driver.find_element_by_xpath("//button[@id='signal_form-compleate']").click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "signal_process_dialog"))
        )
    except:
        continue

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "signal_process_dialog"))
        )
    except:
        continue

    driver.find_element_by_xpath("//label[contains(@id, 'signal_process_dialog_form-j_')]").click()
    driver.find_element_by_xpath("//input[contains(@id, '-close_code_select_one_menu_filter')]").send_keys(reason)
    driver.find_element_by_xpath("//input[contains(@id, '-close_code_select_one_menu_filter')]").send_keys(Keys.ENTER)
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//form[contains(@id, 'j_idt')]/div/button[contains(@id, '-save')]").click()
    except:
        continue

    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Наряд закрыт')]"))
        )
    finally:
        continue

driver.quit()
