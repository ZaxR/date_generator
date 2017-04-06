import csv
import tkinter as tk
from tkinter import ttk


class DateGenerator(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.wm_title("Date Generator")

        tk.Frame.__init__(self, self.root)
        self.create_widgets()

    def create_widgets(self):
        year_choices = [i for i in range(1896, 2051)]

        tk.Label(self.root, text="Start Year: ").grid(row=0)
        start = tk.StringVar(self.root)
        start.set(1997)
        start_year = ttk.Combobox(self.root, textvariable=start, values=year_choices, state='readonly')
        start_year.grid(column=1, row=0)

        tk.Label(self.root, text="End Year: ").grid(row=1)
        end = tk.StringVar(self.root)
        end.set(2017)
        end_year = ttk.Combobox(self.root, textvariable=end, values=year_choices, state='readonly')
        end_year.grid(column=1, row=1)

        #Allow pushing enter to run, but causes all previous selections to be saved
        #self.root.bind('<Button-1>', lambda x=0, y=0: self.get_date_list(start.get(), end.get()))
        #self.grid()

        self.submit = tk.Button(self.root, text="Generate")
        self.submit.bind('<Button-1>', lambda x=0, y=0: self.get_date_list(start.get(), end.get()))
        self.submit.grid(column=1, row=4)

    def get_date_list(self, start_year, end_year):
        start_year = int(start_year)
        end_year = int(end_year)
        if start_year > end_year:
            date_list = self.count_back(start_year, end_year)
        else:
            date_list = self.create_date_range(start_year, end_year)

        self.write_to_csv(start_year, end_year, date_list)

    def count_back(self, start_year, end_year):
        start_year, end_year = end_year, start_year
        date_list = self.create_date_range(start_year, end_year)
        return date_list[::-1]

    def create_date_range(self, start_year, end_year):
        date_list = []
        for i in range(start_year, end_year + 1):
            date_list.append(i)
            for j in range(2, 5):
                date = "{0}Q{1}".format(j, str(i)[2:4])
                date_list.append(date)

        return date_list

    def write_to_csv(self, start_year, end_year, date_list):  # todo handle PermissionError when file locked
        file_name = "Dates {0} to {1} quarterly.csv".format(start_year, end_year)
        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            for date in date_list:
                writer.writerow([date])

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    DateGenerator().start()