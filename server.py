import socket
import tkinter as tk
import sys




def create_window():
    # Tạo một đối tượng Tk
    root = tk.Tk()

    # Thiết lập kích thước cửa sổ
    root.geometry("300x200")

    # Tạo một nhãn
    label = tk.Label(root, text="Xin chào, đây là một ứng dụng tkinter!")

    # Đặt nhãn vào cửa sổ
    label.pack()

    # Tạo một nút
    button = tk.Button(root, text="Nhấn vào đây để thoát", command=root.quit)

    # Đặt nút vào cửa sổ
    button.pack()

    # Vòng lặp chạy chương trình
    root.mainloop()


create_window()




