products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]

found = False
for product in products:
    if product == "MacBook Pro 16 inch":
        print("Da tim thay san pham")
        found = True
        break

if found == False:
    print("Khong tim thay san pham")
