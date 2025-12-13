# Bai 1
def ChiaHaiSo():
    try:
        a = input("A = ")
        b = input("B = ")
        a = int(a)
        b = int(b)
        ketQua = a / b

    except (ValueError, ZeroDivisionError) as e:
        return f"Lỗi input: {e}"
    else:
        return f"Kết quả là:{ketQua}"
    finally:
        print("Kết thúc chương trình")


print(ChiaHaiSo())
