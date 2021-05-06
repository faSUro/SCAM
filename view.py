from tkinter import *
from threading import Thread
import lib


class ViewThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.crypto_labels = {}

    def run(self):
        window = Tk()
        window.title("SCAM")

        for i in range(len(lib.interesting_crypto)):
            name_frame = Frame(master=window)
            name_frame.grid(row=i, column=0)
            name_label = Label(master=name_frame, text=lib.interesting_crypto[i], font=('Helvetica bold', 25))
            name_label.pack(padx=10, pady=10)

            price_frame = Frame(master=window)
            price_frame.grid(row=i, column=1)
            price_label = Label(master=price_frame, text="0000", font=('Helvetica bold', 25))
            price_label.pack(padx=10, pady=10)

            trend_frame = Frame(master=window)
            trend_frame.grid(row=i, column=2)
            trend_label = Label(master=trend_frame, text="0,00%", font=('Helvetica bold', 25))
            trend_label.pack(padx=10, pady=10)

            self.crypto_labels[lib.interesting_crypto[i]] = {'name': name_label, 'price': price_label, 'trend': trend_label}

        window.mainloop()

    def refresh_data(self, new_data):
        # if (new_data[0]+new_data[1]) in self.crypto_labels:
        self.crypto_labels[new_data[0]+new_data[1]]['name'].config(text=new_data[0])
        self.crypto_labels[new_data[0]+new_data[1]]['price'].config(text=new_data[2])
        self.crypto_labels[new_data[0]+new_data[1]]['trend'].config(text=new_data[3])
