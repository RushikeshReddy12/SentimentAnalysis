from textblob import TextBlob
import pandas as pd

def analyze(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

data = {
    'text': [
        "I love this product! It's amazing.",
        "Worst service ever. I'm really disappointed.",
        "It’s okay, not too bad but could be better.",
        "Absolutely fantastic! Highly recommended.",
        "I didn't like the experience at all."
    ]
}
df = pd.DataFrame(data)
df['sentiment'] = df['text'].apply(analyze)
print(df)