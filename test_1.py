import pytest
import yaml
import time

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(site, select_input_login, select_input_password, select_input_button, select_error):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_input_button)
    btn.click()
    err_label = site.find_element('xpath', select_error)
    assert err_label.text == '401'


def test_step_2(site, select_input_login, select_input_password, select_input_button, select_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    answer = site.find_element('xpath', select_hello_user)
    print(answer.text)
    assert answer.text == f'Hello, {testdata["login"]}'


def test_step_3(site, select_input_login, select_input_password, select_input_button, select_input_create_new_post, select_input_name_new_post, select_input_button_new_post, select_title_post):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login_dummy'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password_dummy'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    input3 = site.find_element('xpath', select_input_create_new_post)
    input3.click()
    input4 = site.find_element('xpath', select_input_name_new_post)
    input4.send_keys(testdata['title_new_post'])
    btn_new_post = site.find_element('xpath', select_input_button_new_post)
    btn_new_post.click()
    time.sleep(testdata['sleep_time'])
    answer = site.find_element('xpath', select_title_post)
    assert answer.text == testdata["title_new_post"]
