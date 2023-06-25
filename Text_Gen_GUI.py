import openai
import re
import sys
import pyttsx3
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

key = "your_Open_Ai_API_KEY"  # <----- paste your OpenAI key

class Text_gen(QMainWindow):
    def __init__(self):
        super(Text_gen, self).__init__()
        loadUi("Text_Generator_Using Open Ai\Text_Gen.ui", self)
        self.pushButton_3.clicked.connect(self.Text_Genr)
        self.fazeel = pyttsx3.init('sapi5')
        self.voice = self.fazeel.getProperty("voices")
        self.fazeel.setProperty("voice", self.voice[0].id)

    def Text_Genr(self):
        openai.api_key = key
        prompt = self.plainTextEdit.toPlainText()
        model = "text-davinci-003"

        def Stuff():
            s = "AI BOT is trying to generate a new text for you...."

            completion = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5
            )
            generated_text = completion.choices[0].text
            self.textBrowser.setPlainText(str(generated_text))

            def _save():
                with open("Text.txt", "w") as f:
                    f.write(str(generated_text.strip()))

            self.pushButton_2.clicked.connect(_save)

            def speak(audio):
                self.fazeel.say(audio)
                self.fazeel.runAndWait()

            def _spk():
                speak(generated_text)

            self.pushButton.clicked.connect(_spk)

        Stuff()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Text_gen()
    win.setWindowIcon(QIcon("Prog.ico"))
    win.show()
    sys.exit(app.exec_())
