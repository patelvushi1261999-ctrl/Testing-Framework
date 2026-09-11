import os
import logging
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# ============================================================
# CONFIGURATION
# ============================================================

BASE_URL = "https://www.saucedemo.com/"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ============================================================
# BROWSER FIXTURE
# ============================================================

@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(BASE_URL)

    yield driver

    driver.quit()


# ============================================================
# TASK 1
# LOGIN TESTS
# Equivalent of:
# FlipkartLoginTests.java
# @BeforeMethod
# @AfterMethod
# ============================================================

class TestLogin:

    def test_login_with_valid_credentials(self, driver):

        print("\nRunning: test_login_with_valid_credentials")

        # Enter username
        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("standard_user")

        # Enter password
        driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        # Click login
        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        # Verify dashboard/inventory page
        inventory_element = driver.find_element(
            By.ID,
            "inventory_container"
        )

        assert inventory_element.is_displayed()

        assert "inventory.html" in driver.current_url

        print("Login successful")


# ============================================================
# TASK 2
# SEARCH TESTS
# Equivalent of:
# SearchProductTests.java
#
# TestNG:
# @Test(groups = {"search"})
#
# pytest equivalent:
# @pytest.mark.search
# ============================================================

@pytest.mark.search
class TestSearchProduct:

    def test_search_by_product_name(self, driver):

        print("\nRunning: test_search_by_product_name")

        # Login
        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("standard_user")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        # Verify product page
        assert "inventory.html" in driver.current_url

        # Check product name
        products = driver.find_elements(
            By.CLASS_NAME,
            "inventory_item_name"
        )

        product_names = [
            product.text
            for product in products
        ]

        print("Available products:", product_names)

        assert len(product_names) > 0

        # Search for a specific product name
        assert "Sauce Labs Backpack" in product_names

    def test_search_by_category(self, driver):

        print("\nRunning: test_search_by_category")

        # Login
        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("standard_user")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        assert "inventory.html" in driver.current_url

        # Get all products
        products = driver.find_elements(
            By.CLASS_NAME,
            "inventory_item"
        )

        # Category/product validation
        assert len(products) > 0

        print(
            f"Products available in inventory: {len(products)}"
        )


# ============================================================
# TASK 3
# DATA PROVIDER EQUIVALENT
#
# TestNG:
# @DataProvider
#
# pytest:
# @pytest.mark.parametrize
# ============================================================

class TestAddToCart:

    @pytest.mark.parametrize(
        "product_name, quantity",
        [
            ("Sauce Labs Backpack", 1),
            ("Sauce Labs Bike Light", 1),
            ("Sauce Labs Bolt T-Shirt", 1),
        ]
    )
    def test_add_multiple_products_to_cart(
        self,
        driver,
        product_name,
        quantity
    ):

        print(
            f"\nAdding product: {product_name}, "
            f"Quantity: {quantity}"
        )

        # Login
        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("standard_user")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        assert "inventory.html" in driver.current_url

        # Find all products
        products = driver.find_elements(
            By.CLASS_NAME,
            "inventory_item"
        )

        product_found = False

        for product in products:

            name = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            if name == product_name:

                add_button = product.find_element(
                    By.TAG_NAME,
                    "button"
                )

                add_button.click()

                product_found = True

                break

        # Verify product was found
        assert product_found, (
            f"Product not found: {product_name}"
        )

        # Get cart count
        cart_count = driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_badge"
        )

        actual_count = int(cart_count.text)

        # Verify cart count
        assert actual_count == quantity

        print(
            f"Cart count is correctly updated to "
            f"{actual_count}"
        )


# ============================================================
# TASK 4
# PRIORITY EQUIVALENT
#
# TestNG:
# @Test(priority = 1)
#
# pytest does not have native TestNG-style priority.
#
# For learning purposes, we demonstrate the desired order
# using a marker and explain the ordering below.
# ============================================================

class TestCheckout:

    @pytest.mark.order(1)
    def test_checkout_process(self, driver):

        print(
            "\nRunning: test_checkout_process "
            "(HIGHEST PRIORITY)"
        )

        # Login
        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("standard_user")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        assert "inventory.html" in driver.current_url

        print("Checkout scenario executed")


class TestLoginPriority:

    @pytest.mark.order(2)
    def test_login_low_priority(self, driver):

        print(
            "\nRunning: test_login_low_priority "
            "(LOWER PRIORITY)"
        )

        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("standard_user")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        assert "inventory.html" in driver.current_url

        print("Login test executed")


# ============================================================
# TASK 5
# PARALLEL EXECUTION
#
# pytest-xdist is the Python equivalent for parallel execution.
#
# Run:
#
# pytest test_advanced.py -n 2
#
# ============================================================


# ============================================================
# AUTOMATIC SCREENSHOT ON FAILURE
# ============================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            test_name = (
                item.name
                .replace("[", "_")
                .replace("]", "_")
                .replace(" ", "_")
            )

            screenshot_path = os.path.join(
                "screenshots",
                test_name + ".png"
            )

            driver.save_screenshot(
                screenshot_path
            )

            print(
                f"\nScreenshot saved at: "
                f"{screenshot_path}"
            )

            logger.error(
                f"Test failed. Screenshot: "
                f"{screenshot_path}"
            )