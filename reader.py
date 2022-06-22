def speak(to_read):
    from win32com.client import Dispatch
    speakit = Dispatch("SAPI.SpVoice")
    speakit.Speak(to_read)


fi = open("read_thiss.txt", "r")

if __name__ == '__main__':
    # while True:
    #     speak_this=input("enter to speak(enter x to exit): ")
    #     if speak_this == "x":
    #         break
    #     else:
    #         speak(speak_this)
    speak(fi.read())
    fi.close()