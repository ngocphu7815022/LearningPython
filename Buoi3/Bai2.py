expected_messages = ["Login successfull", "Welcome"]
actual_message = "Welcome"

for message in expected_messages:
    if message == actual_message:
        print("Cau lenh" + " " + message + " " + "hop le")
    else:
        print("Cau lenh" + " " + message + " " + "khong hop le")
