import requests
import json


def speak(to_read):
    from win32com.client import Dispatch
    speakit = Dispatch("SAPI.SpVoice")
    speakit.Speak(to_read)


if __name__ == '__main__':
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1133ab4e587242c88ed66e58f09a2a62"

    news = requests.get(url)
    news = news.text
    news = json.loads(news)

    i=1
    for article in news['articles']:
        speak(str(i))
        speak(article['title'])
        i += 1
        if i == 5:
            break
