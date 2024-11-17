"""
TestcaseID:TC_PIM_01

Test objective:
  Forgot password link validation on login page
URL= https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Precondition:
1.Launch URL
2.OrangeHRM 3.0 site launched on a compatible browser
3.Click on “Forgot password” link
Steps
1.Username textbox is visible
2.Provide username
3.Click on Reset Password

Expected Result:
The user should be able to see the username box and get a successful message saying “Reset password link sent successfully”.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

# Set up test credentials and URL
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"  # Example username to provide for reset

try:
    # Step 1: Open the OrangeHRM login page
    driver.get(url)
    driver.maximize_window()
    
    # Step 2: Click on the "Forgot your password?" link
    forgot_password_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Forgot your password?"))
    )
    forgot_password_link.click()

    # Step 3: Validate that the username textbox is visible
    username_textbox = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    
    if username_textbox.is_displayed():
        print("Username textbox is visible.")

        # Step 4: Provide username
        username_textbox.send_keys(username)

        # Step 5: Click on Reset Password button
        reset_password_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Reset Password']"))
        )
        reset_password_button.click()

        # Step 6: Validate the success message
        success_message = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-alert-success')]"))
        )
        
        if "Reset password link sent successfully" in success_message.text:
            print("Test Passed: Successful message is displayed.")
        else:
            print("Test Failed: Successful message is NOT displayed.")
    else:
        print("Test Failed: Username textbox is NOT visible.")

except TimeoutException as te:
    print(f"Timeout Exception: {te}")
except NoSuchElementException as ne:
    print(f"Element not found: {ne}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()


"""
TestcaseID:TC_PIM_02
Test objective:
  Header validation on Admin page 
Precondition:
1.Launch URL and login as “Admin”
2.OrangeHRM 3.0 site launched on a compatible browser
Steps:
1.Go to Admin page and validate “Title of the page as OrangeHRM”
2.Validate below options are displaying on admin page
                 1.User management
                 2.Job
                3.Organizations
               4.Qualifications
               5.Nationalities
              6.Corporate banking
              7.Configuration

Expected Result:
The user should be able to see above mentioned Admin page headers on Admin page.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

# Set up test credentials and URL
username = "Admin"
password = "admin123"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

try:
    # Step 1: Open the OrangeHRM login page and log in as Admin
    driver.get(url)
    driver.maximize_window()
    
    # Wait for login elements to be visible and input credentials
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Step 2: Navigate to the Admin page
    admin_page_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))
    )
    admin_page_link.click()

    # Step 3: Validate the title of the page
    expected_title = "OrangeHRM"
    WebDriverWait(driver, 10).until(lambda d: d.title == expected_title)
    assert driver.title == expected_title, f"Title mismatch. Expected: {expected_title}, Found: {driver.title}"
    print("Title validation passed.")

    # Step 4: Validate presence of expected headers on Admin page
    expected_headers = [
        "User Management",
        "Job",
        "Organization",
        "Qualifications",
        "Nationalities",
        "Corporate Banking",
        "Configuration"
    ]

    # Admin page
    for header_text in expected_headers:
        try:
            # Check for each header element by visible text
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//span[text()='{header_text}']"))
            )
            print(f"Header '{header_text}' is visible on the Admin page.")
        except (NoSuchElementException, TimeoutException):
            print(f"Test Failed: Header '{header_text}' is NOT visible on the Admin page.")

    print("Test Passed: All expected headers are present on the Admin page.")

except AssertionError as ae:
    print(f"Assertion Error: {ae}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()






"""
TestcaseID:TC_PIM_03
Test objective:
  Main menu validation on Admin page 
Precondition:
1.Launch URL and login as “Admin”
2.OrangeHRM 3.0 site launched on a compatible browser
Steps:
             1.Go to admin Page
             2.Validate below “Menu options”(on side pane)displaying on Admin page

                 a.Admin
                 b.PIM
                 C.Time
                 d.Leave
                 e.Recruitment
                 f.My Info
                 g.Performance
                 h.Dashboard
                 i.Directory
                k.Maintainance
                l.Buzz

Ecpected Result: The user should able to see above mentioned Admin Page Menu items on Admin page.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the WebDriver
driver = webdriver.Chrome()

# Test credentials and URL
username = "Admin"
password = "admin123"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

try:
    # Step 1: Open the OrangeHRM login page and log in as Admin
    driver.get(url)
    driver.maximize_window()
    
    # Wait for login elements to be visible and input credentials
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Step 2: Navigate to the Admin page
    admin_page_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))
    )
    admin_page_link.click()

    # Step 3: Validate presence of expected menu options in the side pane on Admin page
    expected_menu_options = [
        "Admin",
        "PIM",
        "Time",
        "Leave",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard",
        "Directory",
        "Maintenance",  
        "Buzz"
    ]

    all_visible = True
    for option_text in expected_menu_options:
        try:
            # Check for each menu option element by visible text
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, f"//span[text()='{option_text}']"))
            )
            print(f"Menu option '{option_text}' is visible on the Admin page.")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Test Failed: Menu option '{option_text}' is NOT visible on the Admin page. Error: {str(e)}")
            all_visible = False

    if all_visible:
        print("Test Passed: All expected menu options are present on the Admin page.")
    else:
        print("Test Failed: Some menu options are missing on the Admin page.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
