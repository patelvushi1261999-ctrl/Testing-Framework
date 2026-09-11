import os
import logging
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


# ============================================================
# CONFIGURATION
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

BASE_URL = "https://www.saucedemo.com/"

SCREENSHOT_FOLDER = "screenshots"


# ============================================================
# DRIVER FIXTURE
# ============================================================

@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(BASE_URL)

    yield driver

    driver.quit()


# ============================================================
# AUTOMATIC SCREENSHOT WHEN TEST FAILS
# ============================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Let pytest finish the test first
    outcome = yield

    # Get test result
    report = outcome.get_result()

    # We only want screenshots for actual test failures
    if report.when == "call" and report.failed:

        # Get Selenium driver from fixture
        driver = item.funcargs.get("driver")

        if driver:

            # Create screenshot folder if it doesn't exist
            os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

            # Get test name
            test_name = item.name

            # Remove characters that can cause filename problems
            test_name = (
                test_name
                .replace("[", "_")
                .replace("]", "_")
                .replace(" ", "_")
            )

            # Screenshot path
            screenshot_path = os.path.join(
                SCREENSHOT_FOLDER,
                test_name + ".png"
            )

            # Take screenshot
            driver.save_screenshot(screenshot_path)

            # Log screenshot path
            logger.error(
                f"Screenshot saved at: {screenshot_path}"
            )

            print(
                f"\nScreenshot saved at: {screenshot_path}"
            )


# ============================================================
# TEST CLASS 1 - LOGIN TESTS
# ============================================================

class TestLogin:

    def test_valid_login(self, driver):

        logger.info("Checking login button visibility")

        # Find username field
        username = driver.find_element(
            By.ID,
            "user-name"
        )

        # Enter username
        username.send_keys("standard_user")

        # Find password field
        password = driver.find_element(
            By.ID,
            "password"
        )

        # Enter password
        password.send_keys("secret_sauce")

        # Find login button
        login_button = driver.find_element(
            By.ID,
            "login-button"
        )

        # Check login button visibility
        assert login_button.is_displayed()

        logger.info("Checking login button visibility")

        # Click login
        login_button.click()

        # Verify successful login
        assert "inventory.html" in driver.current_url

    def test_invalid_login(self, driver):

        logger.info("Testing invalid login")

        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("wrong_user")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("wrong_password")

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        # Invalid login should NOT go to inventory
        assert "inventory.html" not in driver.current_url


# ============================================================
# TEST CLASS 2 - CHECKOUT TESTS
# ============================================================

class TestCheckout:

    def test_website_title(self, driver):

        logger.info("Checking website title")

        assert driver.title == "Swag Labs"

    def test_saucedemo_url(self, driver):

        logger.info("Checking SauceDemo URL")

        assert "saucedemo.com" in driver.current_url


# ============================================================
# INTENTIONALLY FAILING TEST
# ============================================================

class TestFailureExample:

    def test_intentional_failure(self, driver):

        logger.info(
            "Running intentional failure test"
        )

        # This is intentionally wrong.
        # It is used to test automatic screenshots.

        assert False, "This test is intentionally failing"


# ============================================================
# TEST SUMMARY
# ============================================================

"""
TASK 1
------

This file contains two main test classes:

    TestLogin
    TestCheckout

There is also:

    TestFailureExample

Run the file with:

    python -m pytest test_all_tasks.py -v


TASK 2
------

Generate an HTML report:

    python -m pytest test_all_tasks.py -v --html=reports/report.html --self-contained-html

The report will be created here:

    reports/report.html

Open that file in your browser.

The report shows:

    PASS
    FAIL
    SKIP

for each test method.

Example:

    TestLogin::test_valid_login
        PASSED

    TestLogin::test_invalid_login
        PASSED

    TestCheckout::test_website_title
        PASSED

    TestCheckout::test_saucedemo_url
        PASSED

    TestFailureExample::test_intentional_failure
        FAILED


TASK 3
------

Custom messages are created using Python logging:

    logger.info("Checking login button visibility")

You can see these messages in the terminal.

Example:

    INFO - Checking login button visibility


TASK 4
------

When a test fails, pytest calls:

    pytest_runtest_makereport()

The hook checks:

    report.failed

If the test failed, Selenium takes a screenshot:

    driver.save_screenshot(screenshot_path)

The screenshot is saved inside:

    screenshots/


TASK 5
------

After running the intentionally failing test, open:

    reports/report.html

Find:

    TestFailureExample::test_intentional_failure

The report will show:

    FAILED

The terminal will also show:

    Screenshot saved at:
    screenshots/test_intentional_failure.png

Open that PNG file to see the browser state when the test failed.

This helps you identify:

    1. Which test failed
    2. Why it failed
    3. What the browser looked like
    4. Where the screenshot was saved
"""


# ============================================================
# COMMAND TO RUN EVERYTHING
# ============================================================

"""
Use this command from PowerShell:

python -m pytest test_all_tasks.py -v --html=reports/report.html --self-contained-html
"""