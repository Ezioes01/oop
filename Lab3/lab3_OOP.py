# ฟังก์ชั่นย่อยในการคำนวณต่างๆ
def left_half_tree(max_rows):
    """ lab 2.1 รูปที่ 1 left_half_tree """
    data_tree1 = []
    for i in range(1,max_rows+1):
        data_tree1.append('* ' * i)
    return data_tree1

def invert_left_half_tree(max_rows):
    """ lab 2.1 รูปที่ 2 invert_left_half_tree """
    data_tree2 = []
    for i in range(max_rows,0,-1):
        data_tree2.append('* '*i)
    return data_tree2

def full_tree(max_rows):
    """ lab 2.1 รูปที่ 3 full_tree """
    data_tree3 = []
    for i in range(1, max_rows + 1):
        data_tree3.append(' ' * (max_rows - i) + '* ' * i)
    return data_tree3

def inverst_full_tree(max_rows):
    """ lab 2.1 รูปที่ 4 inverst_full_tree """
    data_tree4 = []
    for i in range(max_rows, 0, -1):
        data_tree4.append(' ' * (max_rows - i) + '* ' * i)
    return data_tree4

def right_half_tree(max_rows):
    """ lab 2.1 รูปที่ 5 right_half_tree """
    data_tree5 = []
    for i in range(1,max_rows + 1):
        data_tree5.append('  '*(max_rows-i) + '* '*i)
    return data_tree5

    
# ฟังก์ชั่นหลัก เรียกใช้ฟังก์ชั่นย่อยในการคำนวณ
def generate_tree(max_rows):
    tree_1 = left_half_tree(max_rows)
    
    tree_2 = invert_left_half_tree(max_rows)
    
    tree_3 = full_tree(max_rows)
    
    tree_4 = inverst_full_tree(max_rows)
    
    tree_5 = right_half_tree(max_rows)
    
    return tree_1, tree_2, tree_3, tree_4, tree_5
    

max_rows = int(input("Enter max_rows: "))   # กำหนดแถวทั้งหมด
tree_1, tree_2, tree_3, tree_4, tree_5 = generate_tree(max_rows)  # กำหนดตัวแปรใช้รับค่าและส่งจำนวนแถวทั้งหมดเข้าฟังก์ชั่น

print("left_half_tree")
print("\n".join(tree_1))

print("\n Invert_left_half_tree")
print("\n".join(tree_2))

print("\n Full_Tree")
print("\n".join(tree_3))

print("\n Inverst_Full_Tree")
print("\n".join(tree_4))

print("\n right_half_tree")
print("\n".join(tree_5))



