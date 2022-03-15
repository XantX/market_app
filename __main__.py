import tkinter as tk
import config.restaurante_datos as rest_data
# import dataccess.config_db as con_db


def main():
    root = tk.Tk()
    root.title(rest_data.nombre)
    root.iconbitmap(rest_data.ico)
    root.resizable(0, 0)
    frame = tk.Frame(root)
    frame.pack()
    frame.config(width=480, height=400, bg='green')
    root.mainloop()


if __name__ == "__main__":
    main()
