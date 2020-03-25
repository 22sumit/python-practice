import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("D:\pythonPractise\drivers\chromedriver.exe") #if not added in PATH
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()