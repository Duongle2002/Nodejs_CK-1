import openpyxl
from openpyxl.styles import Alignment

# Tạo workbook và worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Add to Cart Test Scripts"

# Định dạng tiêu đề
headers = ["Test Case ID", "Test Case", "Description", "Preconditions", "Test Steps", "Expected Outcome", "Postconditions"]
ws.append(headers)

# Dữ liệu kịch bản test
test_scripts = [
    {
        "Test Case ID": "TC_AD_01",
        "Test Case": "Add Cognac Brandy XO to Cart",
        "Description": "Kiểm tra chức năng thêm sản phẩm \"Cognac Brandy XO\" vào giỏ hàng với số lượng 2.",
        "Preconditions": "- Trình duyệt Chrome đã được mở.\n- Người dùng đã đăng nhập với tài khoản hợp lệ (email: admin@gmail.com, password: 123456).\n- Trang sản phẩm (https://nodejs-ck-x8q8.onrender.com/product) đã được tải.\n- Sản phẩm \"Cognac Brandy XO\" (ID: 67659eac432938258cd5f120) có sẵn trên trang.",
        "Test Steps": "1. Điều hướng đến trang sản phẩm bằng cách nhấn liên kết \"Products\" trên menu.\n2. Chờ danh sách sản phẩm hiển thị (tối đa 15 giây).\n3. Tìm sản phẩm \"Cognac Brandy XO\" bằng ID \"67659eac432938258cd5f120\".\n4. Cuộn trang đến vị trí sản phẩm để đảm bảo sản phẩm hiển thị rõ ràng.\n5. Di chuột đến sản phẩm để hiển thị nút \"Add to Cart\".\n6. Nhấn nút \"Add to Cart\" 2 lần để thêm sản phẩm với số lượng 2.\n7. Chờ hệ thống xử lý mỗi lần nhấn (khoảng 1 giây giữa các lần nhấn).\n8. Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công.",
        "Expected Outcome": "- Sản phẩm \"Cognac Brandy XO\" được thêm vào giỏ hàng với số lượng 2.\n- Kết quả: \"Add 2 to cart success\".",
        "Postconditions": "Giỏ hàng chứa sản phẩm vừa thêm.\nTrang sản phẩm vẫn được hiển thị để sẵn sàng cho test case tiếp theo."
    },
    {
        "Test Case ID": "TC_AD_02",
        "Test Case": "Add London Dry Gin to Cart",
        "Description": "Kiểm tra chức năng thêm sản phẩm \"London Dry Gin\" vào giỏ hàng với số lượng 1.",
        "Preconditions": "- Trình duyệt Chrome đã được mở.\n- Người dùng đã đăng nhập với tài khoản hợp lệ (email: admin@gmail.com, password: 123456).\n- Trang sản phẩm (https://nodejs-ck-x8q8.onrender.com/product) đã được tải.\n- Sản phẩm \"London Dry Gin\" (ID: 67659eac432938258cd5f121) có sẵn trên trang.",
        "Test Steps": "1. Điều hướng đến trang sản phẩm bằng cách nhấn liên kết \"Products\" trên menu.\n2. Chờ danh sách sản phẩm hiển thị (tối đa 15 giây).\n3. Tìm sản phẩm \"London Dry Gin\" bằng ID \"67659eac432938258cd5f121\".\n4. Cuộn trang đến vị trí sản phẩm để đảm bảo sản phẩm hiển thị rõ ràng.\n5. Di chuột đến sản phẩm để hiển thị nút \"Add to Cart\".\n6. Nhấn nút \"Add to Cart\" 1 lần để thêm sản phẩm với số lượng 1.\n7. Chờ hệ thống xử lý (khoảng 1 giây).\n8. Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công.",
        "Expected Outcome": "- Sản phẩm \"London Dry Gin\" được thêm vào giỏ hàng với số lượng 1.\n- Kết quả: \"Add 1 to cart success\".",
        "Postconditions": "Giỏ hàng chứa sản phẩm vừa thêm.\nTrang sản phẩm vẫn được hiển thị để sẵn sàng cho test case tiếp theo."
    },
    {
        "Test Case ID": "TC_AD_03",
        "Test Case": "Add Aged Dark Rum to Cart",
        "Description": "Kiểm tra chức năng thêm sản phẩm \"Aged Dark Rum\" vào giỏ hàng với số lượng 1.",
        "Preconditions": "- Trình duyệt Chrome đã được mở.\n- Người dùng đã đăng nhập với tài khoản hợp lệ (email: admin@gmail.com, password: 123456).\n- Trang sản phẩm (https://nodejs-ck-x8q8.onrender.com/product) đã được tải.\n- Sản phẩm \"Aged Dark Rum\" (ID: 67659eac432938258cd5f122) có sẵn trên trang.",
        "Test Steps": "1. Điều hướng đến trang sản phẩm bằng cách nhấn liên kết \"Products\" trên menu.\n2. Chờ danh sách sản phẩm hiển thị (tối đa 15 giây).\n3. Tìm sản phẩm \"Aged Dark Rum\" bằng ID \"67659eac432938258cd5f122\".\n4. Cuộn trang đến vị trí sản phẩm để đảm bảo sản phẩm hiển thị rõ ràng.\n5. Di chuột đến sản phẩm để hiển thị nút \"Add to Cart\".\n6. Nhấn nút \"Add to Cart\" 1 lần để thêm sản phẩm với số lượng 1.\n7. Chờ hệ thống xử lý (khoảng 1 giây).\n8. Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công.",
        "Expected Outcome": "- Sản phẩm \"Aged Dark Rum\" được thêm vào giỏ hàng với số lượng 1.\n- Kết quả: \"Add 1 to cart success\".",
        "Postconditions": "Giỏ hàng chứa sản phẩm vừa thêm.\nTrang sản phẩm vẫn được hiển thị để sẵn sàng cho test case tiếp theo."
    },
    {
        "Test Case ID": "TC_AD_04",
        "Test Case": "Add Silver Tequila to Cart",
        "Description": "Kiểm tra chức năng thêm sản phẩm \"Silver Tequila\" vào giỏ hàng với số lượng 3.",
        "Preconditions": "- Trình duyệt Chrome đã được mở.\n- Người dùng đã đăng nhập với tài khoản hợp lệ (email: admin@gmail.com, password: 123456).\n- Trang sản phẩm (https://nodejs-ck-x8q8.onrender.com/product) đã được tải.\n- Sản phẩm \"Silver Tequila\" (ID: 67659eac432938258cd5f123) có sẵn trên trang.",
        "Test Steps": "1. Điều hướng đến trang sản phẩm bằng cách nhấn liên kết \"Products\" trên menu.\n2. Chờ danh sách sản phẩm hiển thị (tối đa 15 giây).\n3. Tìm sản phẩm \"Silver Tequila\" bằng ID \"67659eac432938258cd5f123\".\n4. Cuộn trang đến vị trí sản phẩm để đảm bảo sản phẩm hiển thị rõ ràng.\n5. Di chuột đến sản phẩm để hiển thị nút \"Add to Cart\".\n6. Nhấn nút \"Add to Cart\" 3 lần để thêm sản phẩm với số lượng 3.\n7. Chờ hệ thống xử lý mỗi lần nhấn (khoảng 1 giây giữa các lần nhấn).\n8. Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công.",
        "Expected Outcome": "- Sản phẩm \"Silver Tequila\" được thêm vào giỏ hàng với số lượng 3.\n- Kết quả: \"Add 3 to cart success\".",
        "Postconditions": "Giỏ hàng chứa sản phẩm vừa thêm.\nTrang sản phẩm vẫn được hiển thị để sẵn sàng cho test case tiếp theo."
    },
    {
        "Test Case ID": "TC_AD_05",
        "Test Case": "Add Premium Russian Vodka to Cart",
        "Description": "Kiểm tra chức năng thêm sản phẩm \"Premium Russian Vodka\" vào giỏ hàng với số lượng 2.",
        "Preconditions": "- Trình duyệt Chrome đã được mở.\n- Người dùng đã đăng nhập với tài khoản hợp lệ (email: admin@gmail.com, password: 123456).\n- Trang sản phẩm (https://nodejs-ck-x8q8.onrender.com/product) đã được tải.\n- Sản phẩm \"Premium Russian Vodka\" (ID: 67659eac432938258cd5f124) có sẵn trên trang.",
        "Test Steps": "1. Điều hướng đến trang sản phẩm bằng cách nhấn liên kết \"Products\" trên menu.\n2. Chờ danh sách sản phẩm hiển thị (tối đa 15 giây).\n3. Tìm sản phẩm \"Premium Russian Vodka\" bằng ID \"67659eac432938258cd5f124\".\n4. Cuộn trang đến vị trí sản phẩm để đảm bảo sản phẩm hiển thị rõ ràng.\n5. Di chuột đến sản phẩm để hiển thị nút \"Add to Cart\".\n6. Nhấn nút \"Add to Cart\" 2 lần để thêm sản phẩm với số lượng 2.\n7. Chờ hệ thống xử lý mỗi lần nhấn (khoảng 1 giây giữa các lần nhấn).\n8. Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công.",
        "Expected Outcome": "- Sản phẩm \"Premium Russian Vodka\" được thêm vào giỏ hàng với số lượng 2.\n- Kết quả: \"Add 2 to cart success\".",
        "Postconditions": "Giỏ hàng chứa sản phẩm vừa thêm.\nTrang sản phẩm vẫn được hiển thị để sẵn sàng cho test case tiếp theo."
    },
    {
        "Test Case ID": "TC_AD_06",
        "Test Case": "Add Single Malt Scotch Whisky to Cart",
        "Description": "Kiểm tra chức năng thêm sản phẩm \"Single Malt Scotch Whisky\" vào giỏ hàng với số lượng 1.",
        "Preconditions": "- Trình duyệt Chrome đã được mở.\n- Người dùng đã đăng nhập với tài khoản hợp lệ (email: admin@gmail.com, password: 123456).\n- Trang sản phẩm (https://nodejs-ck-x8q8.onrender.com/product) đã được tải.\n- Sản phẩm \"Single Malt Scotch Whisky\" (ID: 67659eac432938258cd5f125) có sẵn trên trang.",
        "Test Steps": "1. Điều hướng đến trang sản phẩm bằng cách nhấn liên kết \"Products\" trên menu.\n2. Chờ danh sách sản phẩm hiển thị (tối đa 15 giây).\n3. Tìm sản phẩm \"Single Malt Scotch Whisky\" bằng ID \"67659eac432938258cd5f125\".\n4. Cuộn trang đến vị trí sản phẩm để đảm bảo sản phẩm hiển thị rõ ràng.\n5. Di chuột đến sản phẩm để hiển thị nút \"Add to Cart\".\n6. Nhấn nút \"Add to Cart\" 1 lần để thêm sản phẩm với số lượng 1.\n7. Chờ hệ thống xử lý (khoảng 1 giây).\n8. Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công.",
        "Expected Outcome": "- Sản phẩm \"Single Malt Scotch Whisky\" được thêm vào giỏ hàng với số lượng 1.\n- Kết quả: \"Add 1 to cart success\".",
        "Postconditions": "Giỏ hàng chứa sản phẩm vừa thêm.\nTrang sản phẩm vẫn được hiển thị để sẵn sàng cho test case tiếp theo."
    },
    {
        "Test Case ID": "TC_AD_07",
        "Test Case": "Add duong test to Cart",
        "Description": "Kiểm tra chức năng thêm sản phẩm \"duong test\" vào giỏ hàng với số lượng 1.",
        "Preconditions": "- Trình duyệt Chrome đã được mở.\n- Người dùng đã đăng nhập với tài khoản hợp lệ (email: admin@gmail.com, password: 123456).\n- Trang sản phẩm (https://nodejs-ck-x8q8.onrender.com/product) đã được tải.\n- Sản phẩm \"duong test\" (ID: 67eb4f1172621629a3a2df6d) có sẵn trên trang.",
        "Test Steps": "1. Điều hướng đến trang sản phẩm bằng cách nhấn liên kết \"Products\" trên menu.\n2. Chờ danh sách sản phẩm hiển thị (tối đa 15 giây).\n3. Tìm sản phẩm \"duong test\" bằng ID \"67eb4f1172621629a3a2df6d\".\n4. Cuộn trang đến vị trí sản phẩm để đảm bảo sản phẩm hiển thị rõ ràng.\n5. Di chuột đến sản phẩm để hiển thị nút \"Add to Cart\".\n6. Nhấn nút \"Add to Cart\" 1 lần để thêm sản phẩm với số lượng 1.\n7. Chờ hệ thống xử lý (khoảng 1 giây).\n8. Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công.",
        "Expected Outcome": "- Sản phẩm \"duong test\" được thêm vào giỏ hàng với số lượng 1.\n- Kết quả: \"Add 1 to cart success\".",
        "Postconditions": "Giỏ hàng chứa sản phẩm vừa thêm.\nTrang sản phẩm vẫn được hiển thị để sẵn sàng cho test case tiếp theo."
    }
]

# Thêm dữ liệu vào worksheet
for script in test_scripts:
    ws.append([
        script["Test Case ID"],
        script["Test Case"],
        script["Description"],
        script["Preconditions"],
        script["Test Steps"],
        script["Expected Outcome"],
        script["Postconditions"]
    ])

# Điều chỉnh căn chỉnh và độ rộng cột
for row in ws.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")

ws.column_dimensions["A"].width = 15
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 60
ws.column_dimensions["D"].width = 60
ws.column_dimensions["E"].width = 80
ws.column_dimensions["F"].width = 80
ws.column_dimensions["G"].width = 40

# Lưu file
output_path = "D:/Tester2/test_web_project/data_report/add_to_cart/test_scripts_add_to_cart.xlsx"
wb.save(output_path)
print(f"File Excel đã được tạo tại: {output_path}")