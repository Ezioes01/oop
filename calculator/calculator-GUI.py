import tkinter as tk
from tkinter import messagebox  # สำหรับแสดงหน้าต่างป๊อปอัพ

# ฟังก์ชันสำหรับการกดปุ่มเลขหรือเครื่องหมาย
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# ฟังก์ชันสำหรับการคำนวณผลลัพธ์
def btn_equal():
    global expression, history
    try:
        result = str(eval(expression))  # คำนวณสมการ
        input_text.set(result)          # แสดงผลลัพธ์
        history.append(f"{expression} = {result}")  # เพิ่มลงในประวัติ
        expression = result             # อัปเดต expression ด้วยผลลัพธ์
    except:
        input_text.set("Error")
        expression = ""

# ฟังก์ชันสำหรับการล้างหน้าจอ
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# ฟังก์ชันแสดงประวัติการคำนวณ
def show_history():
    if history:
        messagebox.showinfo("History", "\n".join(history))  # แสดงประวัติในหน้าต่างป๊อปอัพ
    else:
        messagebox.showinfo("History", "No history available")  # ถ้าไม่มีประวัติให้แสดงข้อความนี้


# เริ่มต้นแอปพลิเคชัน
calculator = tk.Tk()
calculator.title("Calculator")
calculator.geometry("450x480")
# เปลี่ยนสี window
calculator.configure(bg="#ADD8E6")

expression = ""
history = []
input_text = tk.StringVar()

# ช่องแสดงผลลัพธ์
input_frame = tk.Frame(calculator, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('Arial', 22, 'bold'), textvariable=input_text, width=27, bg="#33CC99", bd=1, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # ช่องให้ใหญ่ขึ้น

# ปุ่มเครื่องคิดเลข
btns_frame = tk.Frame(calculator, width=400, height=450, bg="grey")
btns_frame.pack()

# ขนาดตัวหนังสือที่ใช้ในปุ่ม
btn_font = ('Arial', 12, 'bold')

# สร้างปุ่มแต่ละแถว พร้อมตั้งขนาดตัวหนังสือด้วย `font=btn_font`
tk.Button(btns_frame, text="C", fg="black", width=21, height=3, bd=1, bg="#CC6699", cursor="hand2", font=btn_font, command=btn_clear).grid(row=0, column=0, columnspan=2)
tk.Button(btns_frame, text="%", fg="black", width=10, height=3, bd=1, bg="#CCCC99", cursor="hand2", font=btn_font, command=lambda: btn_click("%")).grid(row=0, column=2)
tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=1, bg="#CCCC99", cursor="hand2", font=btn_font, command=lambda: btn_click("/")).grid(row=0, column=3)

tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(7)).grid(row=1, column=0)
tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(8)).grid(row=1, column=1)
tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(9)).grid(row=1, column=2)
tk.Button(btns_frame, text="x", fg="black", width=10, height=3, bd=1, bg="#CCCC99", cursor="hand2", font=btn_font, command=lambda: btn_click("*")).grid(row=1, column=3)

tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(4)).grid(row=2, column=0)
tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(5)).grid(row=2, column=1)
tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(6)).grid(row=2, column=2)
tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=1, bg="#CCCC99", cursor="hand2", font=btn_font, command=lambda: btn_click("-")).grid(row=2, column=3)

tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(1)).grid(row=3, column=0)
tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(2)).grid(row=3, column=1)
tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(3)).grid(row=3, column=2)
tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=1, bg="#CCCC99", cursor="hand2", font=btn_font, command=lambda: btn_click("+")).grid(row=3, column=3)

tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=1, bg="#CCFF99", cursor="hand2", font=btn_font, command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=1, bg="#CCCC99", cursor="hand2", font=btn_font, command=lambda: btn_click(".")).grid(row=4, column=2)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=1, bg="#33FF99", cursor="hand2", font=btn_font, command=lambda: btn_equal()).grid(row=4, column=3)

tk.Button(calculator, text="History", fg="black", width=35, height=2, bd=1, bg="#FFCC66", cursor="hand2", font=('Arial', 12, 'bold'), command=show_history).pack(pady=10)

calculator.mainloop()
