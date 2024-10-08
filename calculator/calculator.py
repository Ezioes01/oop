# ฟังก์ชันสำหรับการบวก
def add(x, y):
    return x + y

# ฟังก์ชันสำหรับการลบ
def subtract(x, y):
    return x - y

# ฟังก์ชันสำหรับการคูณ
def multiply(x, y):
    return x * y

# ฟังก์ชันสำหรับการหาร
def divide(x, y):
    if y == 0:
        return "ไม่สามารถหารด้วยศูนย์ได้"
    return x / y

# เริ่มต้นโปรแกรมเครื่องคิดเลข
def calculator():
    print("เลือกการดำเนินการ:")
    print("1. บวก")
    print("2. ลบ")
    print("3. คูณ")
    print("4. หาร")

    choice = input("กรุณาเลือก (1/2/3/4): ")

    num1 = float(input("ใส่เลขตัวแรก: "))
    num2 = float(input("ใส่เลขตัวที่สอง: "))

    if choice == '1':
        print(f"ผลลัพธ์: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"ผลลัพธ์: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"ผลลัพธ์: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"ผลลัพธ์: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("เลือกไม่ถูกต้อง")

# เรียกใช้โปรแกรมเครื่องคิดเลข
calculator()
