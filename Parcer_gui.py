import tkinter as tk
import Document_work
import main
from PIL import  ImageTk, Image
from tkinter import filedialog as fd
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_obj()
        self.render_ui()

    def init_obj(self):

        self.handle_label = tk.Label(text='Хэндл')
        self.time_label = tk.Label(text='Время')
        self.path_label = tk.Label(text='Путь')

        self.ok_img = Image.open('./pic/ок.png')
        self.ok_img = self.ok_img.resize((30,30))
        self.ok_img = ImageTk.PhotoImage(self.ok_img)

        self.path_img = Image.open('./pic/pa.png')
        self.path_img = self.path_img.resize((30,30))
        self.path_img = ImageTk.PhotoImage(self.path_img)


        self.ok_button = tk.Button(image=self.ok_img)
        self.ok_button.bind('<Button-1>', lambda event: self.get_files(self.path_entry.get()))

        self.save_button = tk.Button(image=self.path_img)
        self.save_button.bind('<Button-1>', lambda event: self.get_path())

        self.path_entry = ttk.Entry()

        self.handle_entry = ttk.Entry()

        self.enter_time = ttk.Entry()


    def get_time_limit(self):
        return self.enter_time.get()

    def get_path(self):
        path = fd.askdirectory()
        self.path_entry.insert(0, "{path}/".format(path=path))

    def get_files(self, path):
        self.parc = main.Parcer(self.handle_entry.get())
        problems = self.parc.get_sucses(self.get_time_limit())
        URLS = self.parc.get_url_of_sucsess(problems)
        self.FW = Document_work.File_worker(problems, URLS)
        self.FW.create_file(path=path)
        self.FW.fiil_file(path=path)
        self.FW.rename_to(path=path)

    def render_ui(self):
        self.handle_label.place(x=44, y=22)
        self.time_label.place(x=42, y=49)
        self.path_label.place(x=49, y=77)
        self.path_entry.place(x=92, y=77)
        self.handle_entry.place(x=92, y=23)
        self.enter_time.place(x=92, y=50)
        self.ok_button.place(x=250, y=140)
        self.save_button.place(x=92, y = 110)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Household finance")
    root.geometry("300x186+300+200")
    root.resizable(False, False)
    root.mainloop()
