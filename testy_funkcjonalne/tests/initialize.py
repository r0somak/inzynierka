import pytest
from selenium.webdriver import Firefox, Chrome
import json
from selenium import webdriver

@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else 10

@pytest.fixture(scope='session')
def config_browser(config):
  if 'browser' not in config:
    raise Exception('The config file does not contain "browser"')
  elif config['browser'] not in ['chrome', 'firefox']:
    raise Exception(f'"{config["browser"]}" is not a supported browser')
  return config['browser']

@pytest.fixture(scope='session')
def config():
    with open('tests/config.json') as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()
