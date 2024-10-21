import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Function to check if a string is a valid email address
def is_valid_email(email):
    try:
        # Check email format using regular expression
        email_pattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email_pattern, email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# Initialize Chrome WebDriver
chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    # Open the webpage
    driver.get("https://prasutigirha.vercel.app/")
    time.sleep(2)

    # Explicitly wait for the email field to be clickable
    email_field = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))
    )

    # Explicitly wait for the password field to be present
    password_field = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )

    # Set values for email and password
    email = "softech@gmail.com"
    password = "Softech@123!"

    # Enter email and password values
    email_field.clear()
    email_field.send_keys(email)
    password_field.clear()
    password_field.send_keys(password)

    # Check if the email address is valid
    if is_valid_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")
    time.sleep(1)

    # Remember email and password (Tick)
    remember = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
    )
    remember.click()

    # Click the SignIn button
    log_in_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
    )
    log_in_button.click()
    time.sleep(20)

    # Scroll down the webpage
    target_y = 6000
    scroll_distance = 500
    current_y = 0

    while current_y < target_y:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance
        time.sleep(1)

    # Scroll up the webpage
    target_y_up = 0  # Target vertical scroll position for scrolling up
    scroll_distance = -1000  # Negative value to scroll up
    current_y = 6000  # Assuming the current vertical scroll position is at the bottom of the page

    while current_y > target_y_up:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance  # Decrementing the current_y position
        time.sleep(2)

    # Locate Office Dropdown and wait for it to be clickable
    Office = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Office']"))
    )
    Office.click()
    time.sleep(2)

    #Locate User and wait for it to br clickable
    User = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='User']"))
    )
    User.click()
    time.sleep(2)

    #Locate Fiscal Year  and wait it to be clickable
    Fiscal_year = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Fiscal Year']"))
    )
    Fiscal_year.click()
    time.sleep(2)



    #Locate Department List and wait it to be clickable
    Department_list = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Department List']"))
    )
    Department_list.click()
    time.sleep(5)



    #Locate Post and wait it to be clickable
    Post = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH , "//h1[normalize-space()='Post']"))
    )
    Post.click()
    time.sleep(5)



    #Locate Employee List and wait it to be clickable
    Employee_list = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Employee List']"))
    )
    Employee_list.click()
    time.sleep(5)


    #Locate Donation and wait it to be clickable
    Donation = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Donation']"))
    )
    Donation.click()
    time.sleep(5)


    #Locate Donor Record and wait it to be clickable
    Donor_record = WebDriverWait(driver,40).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Donor Record']"))
    )
    Donor_record.click()
    time.sleep(10)

    #Locate View Donor Record and wait it to be clickable
    View_donor_record = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='View Donor Record']"))
    )
    View_donor_record.click()
    time.sleep(20)

    try:
    # Scroll down the webpage
        target_y = 6000
        scroll_distance = 500
        current_y = 0

        while current_y < target_y:
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)

    # Scroll up the webpage
        target_y_up = 0  # Target vertical scroll position for scrolling up
        scroll_distance = -1000  # Negative value to scroll up
        current_y = 6000  # Assuming the current vertical scroll position is at the bottom of the page

        while current_y > target_y_up:
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            current_y += scroll_distance  # Decrementing the current_y position
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")


    # Input donor name and search
    Donor_name = driver.find_element(*(By.XPATH, "//input[@placeholder='Donor Name']"))

    #Set donor name
    donorname = "Muna Tamang"


    # Check if the first name is empty
    if not Donor_name:
        print("Name cannot be empty")

    # Clear the field and enter the first name value
    Donor_name.clear()
    Donor_name.send_keys(donorname)

    #Locate Search Button and wait it to be clickable
    Search = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='SEARCH']"))
    )
    Search.click()
    time.sleep(5)

    #Locate Details Button and wait it to be clickable
    Details = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Details']"))
    )
    Details.click()
    time.sleep(10)

    #Navigate back
    driver.back()
    time.sleep(5)

    # # Locate to Reset Button and wait it to be clickable
    # Reset = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='RESET']"))
    # )
    # Reset.click()
    # time.sleep(5)

    #Locate Volume of Milk and wait it to be clickable
    Volume_of_milk = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Volume of Milk']"))
    )
    Volume_of_milk.click()
    time.sleep(5)

    #Locate List of Volume Milk and wait it to be clickable
    List_of_volume_milk = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='List of Volume Milk']"))
    )
    List_of_volume_milk.click()
    time.sleep(20)

    # Scroll down the webpage
    target_y = 6000
    scroll_distance = 1000
    current_y = 0

    try:
        # Scroll down the webpage
        target_y = 6000
        scroll_distance = 500
        current_y = 0

        while current_y < target_y:
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)

        # Scroll up the webpage
        target_y_up = 0  # Target vertical scroll position for scrolling up
        scroll_distance = -1000  # Negative value to scroll up
        current_y = 6000  # Assuming the current vertical scroll position is at the bottom of the page

        while current_y > target_y_up:
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            current_y += scroll_distance  # Decrementing the current_y position
            time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")

    # Input donor name and search
    Dname = driver.find_element(*(By.XPATH, "//input[@placeholder='Donor Name']"))

    # Set donor name
    dname = "Rachana Mahat"

    # Add a sleep to see the form filling action
    time.sleep(2)
    # Adjust the sleep duration as needed

    # Check if the first name is empty
    if not Dname:
        print("Name cannot be empty")

    # Clear the field and enter the first name value
    Dname.clear()
    Dname.send_keys(dname)

    # Locate Search Button and wait it to be clickable
    Search1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/main[1]/div[1]/form[1]/div[1]/div[2]/button[1]"))
    )
    Search1.click()
    time.sleep(10)

    # Navigate back
    driver.back()
    time.sleep(10)

    # # Locate to Reset Button and wait it to be clickable
    # Reset1 = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/main[1]/div[1]/form[1]/div[1]/div[2]/button[2]"))
    # )
    # Reset1.click()
    # time.sleep(10)

    #Locate Pasteurization and wait it to be clickable
    Pasteurization = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[contains(@class,'text-xl')][normalize-space()='Pasteurization']"))
    )
    Pasteurization.click()
    time.sleep(5)

    #Locate pasteurization and wait it to be clickable
    pasteurization = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[4]/div[1]/div[2]/a[1]/div[1]/h1[1]"))
    )
    pasteurization.click()
    time.sleep(10)

    try:
        # Scroll down the webpage
        target_y = 6000
        scroll_distance = 500
        current_y = 0

        while current_y < target_y:
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)

    # Scroll up the webpage
        target_y_up = 0  # Target vertical scroll position for scrolling up
        scroll_distance = -1000  # Negative value to scroll up
        current_y = 6000  # Assuming the current vertical scroll position is at the bottom of the page

        while current_y > target_y_up:
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            current_y += scroll_distance  # Decrementing the current_y position
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")


    #Locate  Culture and wait it to be clickable
    Culture = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[4]/div[1]/div[2]/a[2]/div[1]/h1[1]"))
    )
    Culture.click()
    time.sleep(5)

    #Locate Milk Requistion and wait it to be clickable
    Milk_requistion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Milk Requistion']"))
    )
    Milk_requistion.click()
    time.sleep(5)

    #Locate Baby List and wait it to be clickable
    Baby_list = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Baby List']"))
    )
    Baby_list.click()
    time.sleep(5)

    #Locate Milk Requisition and wait it to be clickable
    Milk_requisition = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Milk Requisition']"))
    )
    Milk_requisition.click()
    time.sleep(10)

    #Locate Report and wait it to be clickable
    Report = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Report']"))
    )
    Report.click()
    time.sleep(5)

    #Locate Donor and wait it to be clickable
    Donor = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Donor']"))
    )
    Donor.click()
    time.sleep(5)

    #Locate Milk Volume and wait it to be clickable
    Milk_volume = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Milk Volume']"))
    )
    Milk_volume.click()
    time.sleep(5)

    #Locate Pasteurization and wait it to be clickable
    Pasteurization1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[6]/div[1]/div[2]/a[3]/div[1]/h1[1]"))
    )
    Pasteurization1.click()
    time.sleep(5)

    #Locate Culture and wait for it to clickable
    Culture1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[6]/div[1]/div[2]/a[4]/div[1]/h1[1]"))
    )
    Culture1.click()
    time.sleep(5)

    #Locate Requistion and wait it to be clickable
    Requistion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Requistion']"))
    )
    Requistion.click()
    time.sleep(5)

    #Locate Recipient and wait it to be clickable
    Recipient = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='Recipient']"))
    )
    Recipient.click()
    time.sleep(5)



except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
    print("Congrats!! Code ran successfully")
