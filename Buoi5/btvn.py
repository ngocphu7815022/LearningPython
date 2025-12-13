"""
# Bai 1
def Square():
    try:
        a = int(input("A = "))
        squareResult = a * a
        return squareResult
    except ValueError:
        return "Wrong input, only number allow"


# print(Square())

# Bai 2
def read_file():
    try:
        # Mở file ở chế độ đọc
        with open("example.txt", "r") as file:
            # In ra nội dung trong file
            content = file.read()
        return f"Nội dung file: {content}"
    except FileNotFoundError:
        return "Không thể tìm thấy file"
    finally:
        print("Kết thúc chương trình")


print(read_file())
"""


# Bai 3
def tinh_tuoi():
    try:
        # Nhập vào năm sinh từ bán phím
        year_of_birth = int(input("Nhập năm sinh của bạn: "))

        # Kiểm tra năm sinh có hợp lệ hay không. Năm sinh không được lớn hơn năm hiện tại
        if year_of_birth < 1900 or year_of_birth > 2025:
            raise ValueError("Năm sinh không hợp lệ")
        else:
            your_age = 2025 - year_of_birth
        return your_age

    except ValueError as e:
        return f"Lỗi input {e}"

    finally:
        print("Kết thúc chương trình")


print(tinh_tuoi())
