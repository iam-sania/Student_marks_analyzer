import tkinter as tk
from tkinter import messagebox
import numpy as np


def analyze_marks():
    try:
        # Get input and convert to NumPy array
        marks = list(map(float, entry.get().split(',')))
        arr = np.array(marks)

        # Calculations
        total = np.sum(arr)
        avg = np.mean(arr)
        max_mark = np.max(arr)
        min_mark = np.min(arr)
        std_dev = np.std(arr)

        # Show result
        result_text.set(
            f"Total Marks: {total}\n"
            f"Average: {avg:.2f}\n"
            f"Highest: {max_mark}\n"
            f"Lowest: {min_mark}\n"
            f"Std Deviation: {std_dev:.2f}"
        )
    except:
        messagebox.showerror("Invalid Input", "Please enter marks separated by commas. Example: 45,89,72")


root = tk.Tk()
root.title("🎓 Student Marks Analyzer")
root.geometry("400x400")
root.configure(bg="#d0f0c0")  # Soft green background

title = tk.Label(root, text="Student Marks Analyzer", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50")
title.pack(pady=15)

entry_label = tk.Label(root, text="Enter marks (comma separated):", bg="#d0f0c0", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)

analyze_btn = tk.Button(root, text="Analyze", font=("Arial", 12, "bold"), bg="#3498db", fg="white", command=analyze_marks)
analyze_btn.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="#ecf0f1", width=40, height=8, relief="groove", justify="left")
result_label.pack(pady=20)

root.mainloop()
