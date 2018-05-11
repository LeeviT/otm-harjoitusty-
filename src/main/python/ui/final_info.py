from tkinter import Tk, Label, mainloop, S


class FinalView:

    def __init__(self, output_file_path):
        self.Master = Tk()
        self.Master.wm_title("nbodysim")
        self.Label = Label(self.Master, text=str("Output file saved to " + output_file_path), font=("Helvetica", 20))\
            .grid(row=0, column=0, sticky=S, padx=20, pady=20)
        mainloop()
