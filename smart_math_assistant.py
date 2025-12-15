# =========================================
# Smart Math Assistant
# Author: Abood
# Description:
# This program performs smart math operations
# using Python's math library.
# =========================================

import math  # Import math library | استيراد مكتبة الرياضيات

# Get number from user | إدخال رقم من المستخدم
number = float(input("Enter a number: "))

print("\n--- Math Results ---")  # Display result header | عرض عنوان النتائج

# Square root calculation | حساب الجذر التربيعي
if number >= 0:  # Check if number is non-negative | التأكد أن الرقم غير سالب
    print("Square root:", math.sqrt(number))  # √number
else:
    print("Square root: Not possible for negative numbers")  # لا يمكن حساب الجذر للسالب

# Rounding down | التقريب للأسفل
print("Rounded down:", math.floor(number))

# Rounding up | التقريب للأعلى
print("Rounded up:", math.ceil(number))

# Power calculation | حساب الأس
print("Number power 2:", math.pow(number, 2))  # number²

# Circle area calculation | حساب مساحة الدائرة
radius = abs(number)  # Ensure radius is positive | ضمان أن نصف القطر موجب
circle_area = math.pi * math.pow(radius, 2)  # π × r²
print("Circle area:", circle_area)
