import pytest
from selenium.webdriver.common.by import By
import app


g = app.Zen()
url = "https://www.zenclass.in"
querytitle = "Guvi Python AT – 1 &2 Automation Project"
querydes = "This is a Project Test Code Running for the Python Automation – 1&2 Project Given by mentor Mr. " \
                   "Suman Gangopadhyay."

# test for zen login
@pytest.mark.first
def test_signin():
    g.sign_in(url)
    assert g.driver.current_url == "https://www.zenclass.in/class"

# test to check query creation
@pytest.mark.repeat(1)
def test_createquery():
    g.query_creation(querytitle, querydes)
    assert g.driver.find_element(by=By.XPATH, value="//*[@id='root']/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/span").text.__contains__(querytitle)

# test for extracting data from lhs of zen class page
@pytest.mark.second
def test_lhsData():
    print(g.getLhsData())
