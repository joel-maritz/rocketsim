import tkinter as tk
class ControlPanel:
    def __init__(self,simulation):
        self.sim = simulation
        self.root = tk.Tk()
        self.root.title("Control Panel")

        self.throttle = tk.Scale(
            self.root,
            from_=0,
            to_=100,
            orient='horizontal')
        self.engine_button = tk.Button(
            self.root,
            text='ENGINE: OFF',
            command=self.toggle_engine)
        self.throttle.pack()
        self.engine_button.pack()
    def toggle_engine(self):
        self.sim.engine_on = not self.sim.engine_on
        if self.engine_button['text'] == 'ENGINE: ON':
            self.engine_button['text'] = 'ENGINE: OFF'
        elif self.engine_button['text'] == 'ENGINE: OFF':
            self.engine_button['text'] = 'ENGINE: ON'
    def update(self):
        self.sim.throttle = self.throttle.get() /100
        self.root.update()

