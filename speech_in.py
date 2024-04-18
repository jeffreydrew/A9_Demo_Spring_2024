import speech_recognition as sr


class SpeechIn:
    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    def listen(self):
        with self.m as source:
            self.r.adjust_for_ambient_noise(source, duration=0.4)
            audio = self.r.listen(source)

        try:
            return self.r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sphinx could not understand audio"
        except sr.RequestError as e:
            return "Sphinx error; {0}".format(e)
        
if __name__ == "__main__":
    s = SpeechIn()
    print(s.listen())
