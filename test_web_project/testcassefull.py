import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Cấu hình fixture để khởi tạo và đóng trình duyệt
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Base URL của ứng dụng
BASE_URL = "https://nodejs-ck-x8q8.onrender.com"

# Test case 1: Kiểm tra đăng nhập thành công
def test_successful_login(driver):
    driver.get(BASE_URL + "/login")
    
    # Nhập email và mật khẩu
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    
    email_input.send_keys("john.doe@example.com")  # Email từ users.users.json
    password_input.send_keys("123456")  # Mật khẩu từ users.users.json
    
    # Nhấn nút đăng nhập
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    # Chờ và kiểm tra thông báo chào mừng
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "greeting-text"))
    )
    greeting_text = driver.find_element(By.ID, "greeting-text").text
    assert "Hello John Doe!" in greeting_text, "Login failed: Greeting message not found"

# Test case 2: Kiểm tra đăng ký với thông tin hợp lệ
def test_successful_signup(driver):
    driver.get(BASE_URL + "/signup")
    
    # Nhập thông tin đăng ký
    name_input = driver.find_element(By.ID, "name")
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "confirmpasword")
    
    name_input.send_keys("Test User")
    email_input.send_keys("test.user@example.com")
    password_input.send_keys("Test12345@")
    confirm_password_input.send_keys("Test12345@")
    
    # Nhấn nút đăng ký
    signup_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    signup_button.click()
    
    # Chờ và kiểm tra chuyển hướng về trang đăng nhập
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url, "Signup failed: Did not redirect to login page"

# Test case 3: Kiểm tra tìm kiếm sản phẩm
def test_search_product(driver):
    driver.get(BASE_URL + "/product")
    
    # Nhập từ khóa tìm kiếm
    search_input = driver.find_element(By.NAME, "search")
    search_input.send_keys("Cognac Brandy XO")
    
    # Nhấn nút tìm kiếm
    search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()
    
    # Chờ và kiểm tra kết quả tìm kiếm
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product"))
    )
    product_name = driver.find_element(By.XPATH, "//h2[contains(text(), 'Cognac Brandy XO')]")
    assert product_name.is_displayed(), "Search failed: Product not found"

# Test case 4: Kiểm tra thêm sản phẩm vào giỏ hàng
def test_add_to_cart(driver):
    driver.get(BASE_URL + "/product")
    
    # Tìm sản phẩm và nhấn nút thêm vào giỏ hàng
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-cart"))
    )
    add_to_cart_button.click()
    
    # Chờ và kiểm tra thông báo thêm vào giỏ hàng
    cart_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cart-message"))
    )
    assert cart_message.is_displayed(), "Add to cart failed: Cart message not displayed"

# Test case 5: Kiểm tra đăng xuất
def test_logout(driver):
    # Giả định đã đăng nhập từ test_login
    driver.get(BASE_URL)
    
    # Nhấn nút đăng xuất
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/logout']"))
    )
    logout_button.click()
    
    # Chờ và xác nhận modal đăng xuất
    logout_confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log Out')]"))
    )
    logout_confirm_button.click()
    
    # Kiểm tra hiển thị nút đăng nhập/đăng ký
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "auth-buttons"))
    )
    auth_buttons = driver.find_element(By.ID, "auth-buttons")
    assert auth_buttons.is_displayed(), "Logout failed: Auth buttons not displayed"

# Chạy các test với pytest
if __name__ == "__main__":
    pytest.main(["-v", __file__])