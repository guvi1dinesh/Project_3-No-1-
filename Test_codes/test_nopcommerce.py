from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data import data2
import pytest
from webdriver_manager.firefox import GeckoDriverManager
import time


class TestNopCommerce:
    url = 'https://demo.nopcommerce.com/login'

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    # # Testcase ID:- TC_Login_01
    def test_login_01(self, booting_function):
        self.driver.get(self.url)

        # Click registration button on left side of the webpage.

        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.register_xpath))
        )
        register_button.click()

        #  Fill your personal details:

        # Firstname:
        first_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.first_name_input))
        )
        first_name.send_keys(data2.TestData.firstname)

        # Lastname:
        last_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.last_name_input))
        )
        last_name.send_keys(data2.TestData.lastname)

        # Email:
        Email = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input))
        )
        Email.send_keys(data2.TestData.email)

        # Password:
        Password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input))
        )
        Password.send_keys(data2.TestData.password)

        # Confirm Password:
        ConfirmPassword = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_2))
        )
        ConfirmPassword.send_keys(data2.TestData.password_2)

        # Click register button(to save customer details):
        register_button_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.register_xpath_2))
        )
        register_button_2.click()

        # Expected result:
        print('Registration of customer account successfully.')

    # Testcase ID:- TC_Login_02
    def test_login_02(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()

        # Expected Result:
        print('The customer is logged in successfully.')

    # Testcase ID:- TC_Login_02_1
    def test_login_02_01(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Testing@gmail.com).

        Email2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_3))
        )
        Email2.send_keys(data2.TestData.email3)

        # Enter the Incorrect (password: Admin198).

        password4 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_4))
        )
        password4.send_keys(data2.TestData.password_4)

        # Click the “Login” button.

        login_button_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath_2))
        )
        login_button_2.click()

        # Expected Result:
        print('A valid error message for invalid credentials is displayed.')

    # Testcase ID:- TC_Search_01
    def test_search_01(self, booting_function):
        self.driver.get(self.url)

        # In the login panel enter the (Email: Tester@yahoo.com).

        Email1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.email_input_2))
        )
        Email1.send_keys(data2.TestData.email2)
        time.sleep(5)

        # Enter the (password: admin123).

        password3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.password_input_3))
        )
        password3.send_keys(data2.TestData.password_3)
        time.sleep(5)

        # Click the “Login” button.

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_button_xpath))
        )
        login_button.click()
        time.sleep(5)

        # In top right corner panel of the webpage in search box type the product (Name:
        #  Apple MacBook Pro 13-inch) and click the search button

        # Type the product in searchstore:

        Search_store = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.search_store_input))
        )
        Search_store.send_keys(data2.TestData.search_store)
        time.sleep(5)

        # Click search button:

        Search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.search_button_xpath))
        )
        Search_button.click()
        time.sleep(5)
        self.driver.execute_script('window.scrollBy(0, 500)')

        # Click the button → Add to cart:

        Add_to_cart_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.add_to_cart))
        )
        Add_to_cart_button.click()
        time.sleep(10)

        # Click the button → Add to cart2:

        Add_to_cart_button2 = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.add_to_cart_2))
        )
        Add_to_cart_button2.click()
        time.sleep(10)

        # Click the icon → shopping cart:

        Shopping_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.shopping_cart_xpath))
        )
        Shopping_cart_button.click()

        # Click and agree the terms of service

        Terms_of_service = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.terms_of_service_xpath))
        )
        Terms_of_service.click()

        # Click -> checkout button:

        Checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.checkout_xpath))
        )
        Checkout_button.click()

        # Fill the details:

        # Select dropdown country:

        Select_dropdown_country = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.dropdown_country_xpath))
        )
        Select_dropdown_country.click()

        # Select options in country:

        Select_country = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.option_country_xpath))
        )
        Select_country.click()

        # Fill city:

        City = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.city_xpath))
        )
        City.send_keys(data2.TestData.city)

        # Fill address 1:

        Address1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.address_xpath))
        )
        Address1.send_keys(data2.TestData.address)

        # Fill Zipcode:

        Zipcode = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.zipcode_xpath))
        )
        Zipcode.send_keys(data2.TestData.zipcode)

        # Fill phone number:

        Phone_number = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.phone_no_xpath))
        )
        Phone_number.send_keys(data2.TestData.phone_no)

        # Click -> continue button:

        Continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.continue_xpath))
        )
        Continue_button.click()

        # Shipping method page -> continue button:
        Continue_button2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.continue_xpath_2))
        )
        Continue_button2.click()

        # Payment method page -> continue button:
        Continue_button3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.continue_xpath_3))
        )
        Continue_button3.click()

        # Payment information -> continue button:
        Continue_button4 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.continue_xpath_4))
        )
        Continue_button4.click()

        # Confirm Order -> confirm button:
        Confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.confirm_xpath))
        )
        Confirm_button.click()

        text1 = Confirm_button.text
        print(text1)

        # Order placed successfully-> click continue button:
        Continue_button5 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.continue_xpath_5))
        )
        Continue_button5.click()

        # Click My account on top of the webpage:
        My_account = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.my_account_xpath))
        )
        My_account.click()

        #  On the left side of the webpage of -> My account → Click orders ->we can see order status
        Orders = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.orders_xpath))
        )
        Orders.click()

        # Expected result:
        print('Order placed successfully.')

        
















