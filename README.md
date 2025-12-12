# ==============================================
# 📜 To-Do List (قائمة المهام)
# By: [Your Name]
# Description: This project allows you to add, view, and delete tasks.
# It includes user-friendly prompts and visual separators.
# ==============================================

# قائمة لتخزين المهام
tasks = []

# =========================================================
# دوال المشروع
# =========================================================
def display_menu():
    """عرض القائمة الرئيسية للمستخدم"""
    print("\n" + "="*50)
    print("      📋 Welcome to To-Do List (قائمة المهام) 📋")
    print("="*50)
    print("1️⃣  Add Task (إضافة مهمة)")
    print("2️⃣  Show Tasks (عرض المهام)")
    print("3️⃣  Delete Task (حذف مهمة)")
    print("4️⃣  Exit (خروج)")
    print("="*50)

def add_task():
    """إضافة مهمة جديدة"""
    task_name = input("✏️ Enter new task (أدخل المهمة الجديدة): ")
    if task_name:
        tasks.append(task_name)
        print(f"✅ Task added successfully! (تم إضافة المهمة: '{task_name}')")
    else:
        print("❌ Task name cannot be empty. (لا يمكن أن يكون اسم المهمة فارغاً)")

def show_tasks():
    """عرض جميع المهام الحالية"""
    if not tasks:
        print("📭 No tasks to show. (لا توجد مهام حالياً)")
        return

    print("\n--- 📝 Your Tasks (مهامك الحالية) ---")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("------------------------------")

def delete_task():
    """حذف مهمة حسب رقمها"""
    show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("🗑️ Enter task number to delete (أدخل رقم المهمة للحذف): "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"✅ Task '{deleted_task}' deleted successfully! (تم حذف المهمة)")
        else:
            print("❌ Invalid task number. (رقم مهمة غير صالح)")
    except ValueError:
        print("❌ Invalid input. Please enter a number. (إدخال غير صالح)")

# =========================================================
# الحلقة الرئيسية لتشغيل البرنامج
# =========================================================
def main():
    while True:
        display_menu()
        choice = input("🔹 Choose an option (اختر خياراً): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("👋 Exiting the To-Do List. Goodbye! (مع السلامة!)")
            break
        else:
            print("⚠️ Invalid option. (خيار غير صالح)")

        # فاصل بصري وإيقاف مؤقت لتجربة أفضل في Termux/Pydroid
        print("\n" + "-"*50)
        input("Press ENTER to return to menu... (اضغط ENTER للعودة إلى القائمة)")
        print("-"*50 + "\n")

# =========================================================
if __name__ == "__main__":
    main()
