import unicodedata
import re


def to_slug(text):
    # Chuẩn hoá Unicode
    text = unicodedata.normalize("NFD", text)
    # Loại bỏ dấu
    text = text.encode("ascii", "ignore").decode("utf-8")
    # Chuyển về chữ thường
    text = text.lower()
    # Thay mọi ký tự không phải chữ/số thành "-"
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # Xoá dấu "-" thừa đầu/cuối
    return text.strip("-")


orgText = "Top 5 Laptop Gaming Đáng Mua Nhất"
print(to_slug(orgText))
