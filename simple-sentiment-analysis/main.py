from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    name : str
    score : float

def get_mood(text, *, sensitivity : float):
    score : float = TextBlob(text).sentiment.polarity
    if score > sensitivity:
        return Mood("happy", score)
    elif score < -sensitivity:
        return Mood("sad", score)
    else:
        return Mood("neutral", score)
    
def run_bot():

    print("Enter some text and I will perform a setiment analysis on it.\n")
    while True:
        text = input("You: ")
        mood : Mood = get_mood(text, sensitivity=0.3)
        print(f"Bot: {mood.name}, {mood.score}")

if __name__ == "__main__":
    run_bot()
