import pyttsx3
import time
import tkinter as tk


class SpeechOut:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", "english_rp+f4")
        self.engine.setProperty("rate", 200)  # Set the speed to 200

        self.root = tk.Tk()
        self.root.title("A9 Demo")
        self.root.geometry("1500x1350")
        self.root.configure(background="white")

        # Create a Scrollbar and a Text widget
        self.scrollbar = tk.Scrollbar(self.root)
        self.text = tk.Text(
            self.root,
            wrap="word",
            yscrollcommand=self.scrollbar.set,
            font=("Helvetica", 40),
        )

        # Pack the Scrollbar and Text widgets
        self.scrollbar.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        # Configure the Scrollbar to scroll the Text widget
        self.scrollbar.config(command=self.text.yview)

    # literally find a better voice, don't use espeak
    def speak(self, text):
        # Queue the text to be spoken
        t3 = time.time()
        self.engine.say(text)
        t4 = time.time()

        # Process the speech commands
        t5 = time.time()
        self.engine.runAndWait()
        t6 = time.time()

    def write(self, text):
        time.sleep(0.2)
        # open a tkinter window
        self.text.insert("end", text + "\n")

        # Scroll to the end of the Text widget
        self.text.see("end")

        # run the window loop
        self.root.mainloop()


if __name__ == "__main__":
    out = SpeechOut()
    out.write("Hello World")
