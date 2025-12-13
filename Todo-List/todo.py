# ==============================================
# Contacts Manager Project
# By: Abood
# Description:
# This project allows the user to manage contacts:
# add, view, search, and delete contacts.
#
# مشروع لإدارة جهات الاتصال:
# إضافة – عرض – بحث – حذف
# ==============================================

# Dictionary to store contacts
# المفتاح: الاسم | القيمة: رقم الهاتف
contacts = {}

def show_menu():
    """Display main menu | عرض القائمة الرئيسية"""
    print("\n" + "=" * 40)
    print("📞 Contacts Manager (إدارة جهات الاتصال)")
    print("=" * 40)
    print("1. Add Contact (إضافة جهة اتصال)")
    print("2. View Contacts (عرض جميع الجهات)")
    print("3. Search Contact (البحث عن جهة)")
    print("4. Delete Contact (حذف جهة)")
    print("5. Exit (خروج)")
    print("=" * 40)

def add_contact():
    """Add a new contact | إضافة جهة اتصال"""
    name = input("Enter contact name (اسم الجهة): ").strip()
    phone = input("Enter phone number (رقم الهاتف): ").strip()

    if name and phone:
        contacts[name] = phone
        print("✅ Contact added successfully!")
    else:
        print("❌ Name or phone cannot be empty.")

def view_contacts():
    """View all contacts | عرض جميع الجهات"""
    if not
