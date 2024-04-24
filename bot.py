import random
from textblob import TextBlob

bad_responses = [
    "I'm so sorry to hear that.",
    "That sounds really tough.",
    "Sending you lots of positive thoughts.",
    "If you need to talk about it, I'm here to listen.",
    "Hang in there, things will get better.",
    "Wishing you strength during this difficult time.",
    "I'm here for you, whatever you need.",
    "I can't imagine how hard that must be.",
    "Remember to take care of yourself.",
    "You're not alone, I'm with you."
]

mild_bad_responses = [
    "That's rough, but you'll get through it.",
    "I'm sorry to hear that, but it's not the end of the world.",
    "Keep your head up, better days are ahead.",
    "It's okay to feel down sometimes, just remember brighter days will come.",
    "I'm here to support you through this.",
    "Every setback is a setup for a comeback.",
    "You're stronger than you think, you'll bounce back from this.",
    "Take a deep breath, you've got this.",
    "This too shall pass, just hold on.",
    "I believe in you, you'll overcome this hurdle."
]

mild_good_responses = [
    "That's a small victory worth celebrating!",
    "It's not perfect, but it's definitely a positive.",
    "Well, that's a silver lining!",
    "It's a step in the right direction, and that's something to be happy about.",
    "Progress is progress, no matter how small.",
    "It's not the best outcome, but it's definitely good news.",
    "Any good news is welcome news!",
    "It's not a huge win, but it's still a win nonetheless.",
    "It might not be amazing, but it's definitely encouraging.",
    "It's nice to see things looking up, even if just a little."
]

good_responses = [
    "That's great news!",
    "I'm happy to hear that!",
    "Congratulations!",
    "What a relief!",
    "That's a step in the right direction.",
    "I'm glad things are looking up.",
    "It's always nice to hear some good news.",
    "That must feel really good.",
    "Well done!",
    "I'm proud of you!"
]

print("Hello, I am a random nameless bot by Mohit.\nPlease press enter after every response.\nIf you want to leave, type \"exit\".\nHow is life?")
user_input = input()

while user_input.lower() != "exit":
    randomNum = random.randint(0,9)
    sentiment_text = TextBlob(user_input)
    textPolarity = sentiment_text.sentiment.polarity
    if textPolarity <= -0.5:
        print(bad_responses[randomNum])
    elif textPolarity <= 0:
        print(mild_bad_responses[randomNum])
    elif textPolarity <= 0.5:
        print(mild_good_responses[randomNum])
    elif textPolarity <= 1:
        print(good_responses[randomNum])
    user_input = input()

print("Buh-bye, till next time!")