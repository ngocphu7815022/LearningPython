scores = [95, 83, 67, 45, 88, 90, 50]
for score in scores:
    if score > 90:
        print(f"So diem {score} hoc luc xuat sac")
    elif score >= 70:
        print(f"So diem {score} hoc luc kha")
    elif score >= 50:
        print(f"So diem {score} hoc luc trung binh")
    else:
        print(f"So diem {score} hoc luc yeu")
