from tkinter import *


class CalculationView:

    def __init__(self, n_timesteps):
        self.Master = Tk()
        self.Master.wm_title("nbodysim")
        self.accuracy = 1
        self.timestep = StringVar()
        self.timestep.set("0")
        self.Label = Label(self.Master, text="Current calculation step: ").grid(row=0, column=0, sticky=S, pady=14)
        self.Label = Label(self.Master,
                           text="of " + str(n_timesteps) + " timesteps total").grid(row=1, column=1, sticky=S, pady=10)
        self.Label2 = Label(self.Master, textvariable=self.timestep, font=("Helvetica", 20))
        self.Label2.grid(row=0, column=1)

    def update_current_timestep(self, current_timestep):
        self.timestep.set(str(current_timestep))
        self.Master.update()

