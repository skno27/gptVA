# Speech to text program
import speech_recognition as speech
import pyttsx3


# speech recognizer
recognizer = speech.Recognizer()


def record_text():
    while 1:
        try:
            # use the microphone as an input source
            with speech.Microphone() as source:

                # prepare the recognizer for input
                recognizer.adjust_for_ambient_noise(source, duration=0.2)

                print("I'm listening")

                # listen for the input
                audio = recognizer.listen(source)

                # use google for recognizing
                Text = recognizer.recognize_whisper(audio)

                return Text

        except speech.RequestError as e:
            print("Could not request results; {0}".format(e))
        except speech.UnknownValueError:
            print("Unknown error occurred")

        return


def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")

    f.close()
    return


while True:
    text = record_text()
    output_text(text)
    print("Wrote text")
