from textblob import TextBlob

with open("text.txt","r") as f:
    text = f.read()
    textblb = TextBlob(text)
    textcorrected = textblb.correct()
    print(textcorrected)