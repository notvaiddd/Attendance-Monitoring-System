import tkinter as tk
from tkinter import messagebox
from datetime import datetime


rfid_students = {
    "1": "Vaid",
    "2": "Karan",
    "3": "Sharma",
    "4": "Ratan",
    "5": "Virat",
    "6": "Dhoni",
    "7": "Ambani",
    "8": "Ankur",
    "9": "Singh",
    "10": "Victor"

}


attendance_records = []


def mark_attendance():
    rfid = entry_rfid.get()  
    if rfid in rfid_students:
        name = rfid_students[rfid]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"{name} - {timestamp}"
        attendance_records.append(record)
        listbox.insert(tk.END, record)
        entry_rfid.delete(0, tk.END)  
        messagebox.showinfo("Attendance Marked", f"Attendance marked for {name}")
    else:
        messagebox.showerror("Invalid RFID", "RFID not recognized. Please try again.")
        entry_rfid.delete(0, tk.END)


def clear_attendance():
    global attendance_records
    attendance_records = []  
    listbox.delete(0, tk.END)  

root = tk.Tk()
root.title("RFID Attendance System")
root.geometry("500x400")
root.config(bg="#f0f0f0")


header_frame = tk.Frame(root, bg="#0066cc")
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="RFID Attendance Monitoring System", font=("Arial", 18), fg="white", bg="#0066cc", pady=10)
header_label.pack()


label_rfid = tk.Label(root, text="Scan RFID (Simulate by entering RFID):", font=("Arial", 12), bg="#f0f0f0")
label_rfid.pack(pady=10)

entry_rfid = tk.Entry(root, font=("Arial", 12), width=30)
entry_rfid.pack(pady=5)

button_mark = tk.Button(root, text="Mark Attendance", font=("Arial", 12), command=mark_attendance, bg="#28a745", fg="white")
button_mark.pack(pady=10)


listbox_label = tk.Label(root, text="Attendance Records:", font=("Arial", 12), bg="#f0f0f0")
listbox_label.pack(pady=10)

listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=10)
listbox.pack(pady=5)


button_clear = tk.Button(root, text="Clear Attendance", font=("Arial", 12), command=clear_attendance, bg="#dc3545", fg="white")
button_clear.pack(pady=10)


footer_frame = tk.Frame(root, bg="#0066cc")
footer_frame.pack(side="bottom", fill="x")

footer_label = tk.Label(footer_frame, text="Developed by [Your Name] © 2024", font=("Arial", 10), fg="white", bg="#0066cc", pady=5)
footer_label.pack()


root.mainloop()
