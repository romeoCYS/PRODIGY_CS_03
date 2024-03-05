import tkinter as tk

def check_password_complexity(password):
    complexity = {
        'length': len(password) >= 8,
        'uppercase': any(char.isupper() for char in password),
        'lowercase': any(char.islower() for char in password),
        'digit': any(char.isdigit() for char in password),
        'special_char': any(not char.isalnum() for char in password)
    }
    return complexity

def check_password():
    password = entry.get()
    complexity = check_password_complexity(password)
    result_label.config(text="Password Complexity:\n")
    for key, value in complexity.items():
        result_label.config(text=result_label.cget("text") + f"{key}: {'✓' if value else '✗'}\n")

root = tk.Tk()
root.title("Password Complexity Checker")

window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

label = tk.Label(root, text="Enter Password:")
label.pack()

entry = tk.Entry(root, show="*")
entry.pack()

check_button = tk.Button(root, text="Check Complexity", command=check_password)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
