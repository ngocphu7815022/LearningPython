"""
# Bai 1

s = "Hello Python Developer"
if "Python" in s:
    print("yes")

# Bai 2

message = "python is fun and python is easy"
message_list = message.split()
count = 0
for i in message_list:
    if i == "python":
        count += 1

print(f"So tu 'python' trong cau la {count}")


# Bai 3
name = "ngoc phu"
print(name.title())

# Bai 4
text = "HeLLo WoRLd"
print(text.lower())

# Bai 5
data = "   hello   "
print(data.strip())

# Bai 6
line = "apple,banana,orange,grape"

line_list = line.split(",")
for i in line_list:
    print(i)

# Bai 7
words = ["Python", "is", "powerful"]
newString = " ".join(words)
print(newString)


# Bai 8
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
count = 0

s = "He11o Pyth0n 2025"
s_list = s.split()

for i in s_list:
    for j in i:
        if j in numbers:
            count += 1

print(count)

# Bai 9
txt = "abcdef"
print(txt[::-1])

# Bai 10
word = "level"
if word == word[::-1]:
    print("yes")
else:
    print("no")

# Bai 11
email = "user123@gmail.com"
start = email.find("@") + 1
print(email[start:])


# Bai 12
vowels = ["a", "e", "i", "o", "u"]
countVowel = 0
countConsonant = 0

s = "Python Developer"
s_list = s.split()

for i in s_list:
    for j in i:
        if j in vowels:
            countVowel += 1
        else:
            countConsonant += 1

print(f"So nguyen am {countVowel}")
print(f"So phu am {countConsonant}")


# Bai 13
text = "Hello!!! Python@@@2025***"
count = 0
text_list = text.split()

for i in text_list:
    for j in i:
        if not j.isalnum():
            count += 1

print(f"So ki tu dac biet la {count}")


# Bai 14
def CheckPassword(password):
    lowerChar = False
    upperChar = False
    digitChar = False
    specialChar = False

    if len(password) < 8:
        print("Password cần tối thiểu 8 kí tự")
        return False
    else:
        for chacracter in password:
            if chacracter.isupper() == True:
                upperChar = True
            elif chacracter.islower() == True:
                lowerChar = True
            elif chacracter.isdigit() == True:
                digitChar = True
            elif chacracter.isalnum() == False:
                specialChar = True
            if upperChar and lowerChar and digitChar and specialChar:
                break

    # Sau khi duyệt xong
    if lowerChar and upperChar and digitChar and specialChar:
        print("Password mạnh")
        return True
    else:
        print("Password yếu")
        return False


CheckPassword("Abc12aaaaa3!")
"""

# Bai 15


def ChuanHoa(name):
    # Xóa khoảng trắng trước sau
    newName = name.strip()
    # Chuẩn hóa về các chữ cách nhau 1 khoảng trắng
    newName1 = newName.split()
    newName2 = " ".join(newName1)

    # Chuyển hết thành chữ thường
    newName3 = newName2.lower()

    # Chuẩn hóa cuối cùngz
    newName4 = newName3.title()

    return newName4


print(ChuanHoa("  nGuYeN    vAn    phU   "))
