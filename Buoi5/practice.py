import datetime

# Bai 1
"""
def nhap_so():
    try:
        a = int(input("Nhap a:"))
        return a
    except ValueError as e:
        return f"Giá trị không hợp lệ {e}"
    finally:
        print("Kết thúc chương trình")

print(nhap_so())


# Bai 2
def chia_hai_so():
    try:
        a = int(input("Nhap a: "))
        b = int(input("Nhap b: "))
        if b == 0:
            raise ZeroDivisionError("Không thể chia cho 0")
    except (ValueError, ZeroDivisionError) as e:
        return f"Lỗi {e}"
    else:
        return a / b
    finally:
        print("Done")

print(chia_hai_so())


# Bai3
def tinh_BMI():
    try:
        height = float(input("Nhap chieu cao (m): "))
        weight = float(input("Nhap can nang (kg): "))
        # Kiểm tra chiều cao, cân nặng nhập vào
        if height <= 0 or weight <= 0:
            raise ValueError("Giá trị phải lớn hơn 0")
        elif height > 3:
            raise ValueError("Chiều cao không hợp lý")
    except ValueError as e:
        return f"Lỗi: {e}"
    else:
        bmi_value = weight / (height**2)
        return round(bmi_value, 2)
    finally:
        print("Hoàn thành tính toán")

print(tinh_BMI())

# Bai 4
def doc_file(path):
    try:
        with open(path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Không thể tìm thấy file {e}"
    finally:
        print("Đã đóng file")


print(doc_file("/Users/phupham/Phu_python/Buoi5/example.txt"))



# Bai 5
def nhap_email():
    try:
        email = input("Nhap email: ")
        if email == "":
            raise ValueError("Không được để trống email")
        elif "@" not in email:
            raise ValueError("Email này không hợp lệ")
    except ValueError as e:
        return f"Lỗi {e}"
    else:
        return f"Email {email} hợp lệ"


print(nhap_email())



# Bai 6
def validate_password():
    try:
        has_upper = False
        has_lower = False
        has_number = False

        password = input("Nhập vào mật khẩu: ")

        # Kiểm tra các yêu cầu của mật khẩu
        if len(password) < 8:
            raise ValueError("Mật khẩu phải có ít nhất 8 kí tự")
        if not any(c.isupper() for c in password):
            raise ValueError("Mật khẩu phải có ít nhất 1 chữ hoa")
        if not any(c.islower() for c in password):
            raise ValueError("Mật khẩu phải có ít nhất 1 chữ thường")
        if not any(c.isdigit() for c in password):
            raise ValueError("Mật khẩu phải có ít nhất 1 chữ số")
    except ValueError as e:
        return f"Lỗi {e}"
    else:
        return "Mật khẩu hợp lệ"
    finally:
        print("Kết thúc chương trình")


print(validate_password())



# Bai 7
# Biểu giá điện
# Bậc 1: 0 - 50 kWh đầu tiên: 1.984 VNĐ/kWh.
# Bậc 2: 51 - 100 kWh tiếp theo: 2.050 VNĐ/kWh.
# Bậc 3: 101 - 200 kWh tiếp theo: 2.380 VNĐ/kWh.
# Bậc 4: 201 - 300 kWh tiếp theo: 2.998 VNĐ/kWh.
# Bậc 5: 301 - 400 kWh tiếp theo: 3.350 VNĐ/kWh.
# Bậc 6: Từ 401 kWh trở lên: 3.460 VNĐ/kWh.

# Tổng tiền điện = (Số kWh Bậc 1 x Giá Bậc 1) + (Số kWh Bậc 2 x Giá Bậc 2) + ... + (Số kWh Bậc 6 x Giá Bậc 6) + (Tổng tiền các bậc x 10% VAT).


def tinh_tien_dien():
    try:
        kwh = int(input("Nhập số kWh: "))

        # Tiền/kWh tương ứng với bậc
        gia_tien_bac1 = 1678
        gia_tien_bac2 = 1734
        gia_tien_bac3 = 2014
        gia_tien_bac4 = 2536
        gia_tien_bac5 = 2834
        gia_tien_bac6 = 2927
        # Kiểm tra tiền điện
        if kwh < 0:
            raise ValueError("Số kWh không thể là số âm")

    except ValueError as e:
        return f"Lỗi input: {e}"
    else:
        # Kiểm tra xem thuộc bậc nào
        if kwh <= 50:
            tien = kwh * gia_tien_bac1
        elif kwh <= 100:
            tien = 50 * gia_tien_bac1 + (kwh - 50) * gia_tien_bac2
        elif kwh <= 200:
            tien = 50 * gia_tien_bac1 + 50 * gia_tien_bac2 + (kwh - 100) * gia_tien_bac3
        elif kwh <= 300:
            tien = (
                50 * gia_tien_bac1
                + 50 * gia_tien_bac2
                + 50 * gia_tien_bac3
                + (kwh - 200) * gia_tien_bac4
            )
        elif kwh <= 400:
            tien = (
                50 * gia_tien_bac1
                + 50 * gia_tien_bac2
                + 50 * gia_tien_bac3
                + 50 * gia_tien_bac4
                + (kwh - 300) * gia_tien_bac5
            )
        elif kwh > 400:
            tien = (
                50 * gia_tien_bac1
                + 50 * gia_tien_bac2
                + 50 * gia_tien_bac3
                + 50 * gia_tien_bac4
                + 50 * gia_tien_bac5
                + (kwh - 400) * gia_tien_bac6
            )

        return f"Tổng tiền điện trước thuế: {tien}"

    finally:
        print("Hoàn tất xử lý")


print(tinh_tien_dien())
"""


# Bai8
def check_date():
    input_date = input("Nhập ngày sinh theo định dạng (dd/mm/yyyy): ")
    # Cắt chuỗi
    input_date_splited = input_date.split("/")
    # Năm hiện tại
    current_year = datetime.datetime.now().year

    try:
        day1 = int(input_date_splited[0])
        month1 = int(input_date_splited[1])
        year1 = int(input_date_splited[2])
    except ValueError as e:
        return f"Lỗi input: {e}"

    try:
        datetime.date(year1, month1, day1)
        if year1 > current_year:
            raise ValueError("Năm không được lớn hơn năm hiện tại")

    except ValueError as e:
        return f"Lỗi input: {e}"

    else:
        age = current_year - year1
        return f"Tuổi của bạn: {age}"

    finally:
        print("Xong")


print(check_date())
