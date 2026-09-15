import pytest
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# -------------------------------
# Task 1: Run two test classes in parallel
# -------------------------------

class TestLogin:
    def test_login(self):
        print(f"LoginTest running on Thread: {threading.get_ident()}")

class TestSearch:
    def test_search(self):
        print(f"SearchTest running on Thread: {threading.get_ident()}")


# -------------------------------
# Task 2: Run three methods in parallel
# -------------------------------

class TestCart:
    def test_add_to_cart(self):
        print(f"AddToCart Thread ID: {threading.get_ident()}")

    def test_remove_from_cart(self):
        print(f"RemoveFromCart Thread ID: {threading.get_ident()}")

    def test_checkout(self):
        print(f"Checkout Thread ID: {threading.get_ident()}")


# -------------------------------
# Task 3: Cross browser execution
# -------------------------------

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_flipkart(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    driver.get("https://www.flipkart.com")
    print(f"Opened Flipkart on {browser} - Thread: {threading.get_ident()}")
    driver.quit()


# -------------------------------
# Task 4: Thread-count > available tests
# -------------------------------
# In pytest, you control parallelism with `pytest -n <threads>` using pytest-xdist.
# If you run with more threads than tests, some threads will stay idle.

def test_thread_count_behavior():
    print(f"Thread-count demo running on Thread: {threading.get_ident()}")


# -------------------------------
# Task 5: Each method on different browser
# -------------------------------

class TestMultiBrowser:
    def test_search_chrome(self):
        driver = webdriver.Chrome(service=ChromeService())
        driver.get("https://www.flipkart.com")
        print("Search on Chrome")
        driver.quit()

    def test_filter_firefox(self):
        driver = webdriver.Firefox(service=FirefoxService())
        driver.get("https://www.flipkart.com")
        print("Filter on Firefox")
        driver.quit()

    def test_sort_edge(self):
        driver = webdriver.Edge(service=EdgeService())
        driver.get("https://www.flipkart.com")
        print("Sort on Edge")
        driver.quit()
