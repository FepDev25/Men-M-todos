import tkinter as tk

class Table(tk.Frame):
    def __init__(self, parent, filas, columnas):
        tk.Frame.__init__(self, parent)

        self.labels = []

        for i in range(filas):
            row = []
            for j in range(columnas):
                label = tk.Label(self, text="", relief=tk.RIDGE)
                label.grid(row=i, column=j, sticky="nsew")
                row.append(label)
            self.labels.append(row)

        for i in range(filas):
            self.grid_rowconfigure(i, weight=1)
        for j in range(columnas):
            self.grid_columnconfigure(j, weight=1)

    def set_cell_value(self, row, column, value):
        self.labels[row][column].config(text=value)