from tkinter import *
from tkinter import filedialog
from main.python.ui.calculation_phase import CalculationView


class StartGUI:

    def __init__(self):
        self.Master = Tk()
        self.Master.wm_title("nbodysim")
        self.input_file_name = None
        self.timesteps = 0
        self.accuracy = 1
        self.Label = Label(self.Master, text="Number of timesteps").grid(row=2, column=0, sticky=S, pady=10)
        self.Button = Button(self.Master, text="Choose a input file",
                             command=self.file_browser).grid(row=0, column=0, sticky=S, padx=15, pady=10)
        self.InputFileEntry = Entry(self.Master).grid(row=0, column=1, sticky=S, pady=10)
        self.Entry = Entry(self.Master, textvariable="")
        self.Entry.grid(row=2, column=1)
        self.AccuracyLabel = Label(self.Master, text="Accuracy of simulation").grid(row=3, column=0, sticky=S, pady=10)
        self.AccuracySlider = Scale(self.Master, from_=1, to=10, orient=HORIZONTAL,
                                    command=self.on_slider).grid(row=3, column=1)
        self.ParamsButton = Button(self.Master, text="Pass values to simulation",
                                   command=self.return_params).grid(row=4, column=0)
        self.NextButton = Button(self.Master, text="Calculate!",
                                 command=self.Master.destroy).grid(row=4, column=1)

    def on_button(self):
        self.timesteps = self.Entry.get()
        return self.timesteps

    def on_slider(self, accuracy):
        self.accuracy = accuracy
        return self.accuracy

    def file_browser(self):
        file = filedialog.askopenfile(parent=self.Master, mode='rb', title='Choose a  input file')
        if not file is None:
            self.input_file_name = file.name
            return self.input_file_name

    def return_params(self):
        self.timesteps = self.on_button()
        self.Master.mainloop()
        return self.input_file_name, int(self.timesteps), int(self.accuracy)
