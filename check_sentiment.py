from textblob import TextBlob

# List of SMS messages to analyze
sms_messages = [
       "Hey there! Just wanted to share some exciting news - I got the job!",
        "I'm feeling really down today. Can we talk?",
        "Thank you so much for your help yesterday. You're a lifesaver!",
        "Guess what? We're going to Disneyland next week! 🎉",
        "I can't believe they messed up my order again! 😡",
        "I just found out I won tickets to the concert. Can you believe it?",
        "Finally, the exam is over. I can breathe now!",
        "I heard about the storm heading our way. Are you prepared?",
        "I've been practicing a lot, and I feel ready for the presentation.",
        "Believe in yourself, and you can achieve anything!",
        "I'm so sorry to hear about your loss. My thoughts are with you.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Keep pushing forward. Every small step brings you closer to your goal.",
        "I hope you're taking care of yourself. Don't forget to rest.",
        "Remember the good old times when we used to go on road trips?",
        "Our team just won the championship. We did it!",
        "I thought the movie would be great, but it was a letdown.",
        "I believe better days are ahead. Stay positive!",
        "I don't really have a preference. You choose.",
        "Your support means the world to me. Thanks for being there.",
        "Can you pick up some groceries on your way home?",
        "I'm running late for our meeting. Please start without me.",
        "Congratulations on your graduation! 🎓",
        "Let's plan a weekend getaway soon!",
        "The sunset today was absolutely breathtaking.",
        "I appreciate your feedback on the project. It's helpful.",
        "I can't make it to the party this weekend. Sorry!",
        "The concert last night was epic! You missed out.",
        "I'm craving pizza. Want to order some for dinner?",
        "I need your advice on something important. Can we chat?",
        "I just finished reading an incredible book. You should check it out.",
        "I can't stop laughing at that hilarious video you sent!",
        "The weather forecast says it's going to rain all day. Bring an umbrella!",
        "I'm really proud of you for taking that big step. You've got this!",
        "Happy anniversary! It's been an amazing journey together.",
        "The new restaurant in town has amazing reviews. Let's try it soon.",
        "I'm feeling under the weather. Can you bring me some soup?",
        "Don't stress about the small stuff. It'll all work out.",
        "I'm impressed by your dedication to your fitness goals.",
        "I had a dream about our childhood adventures. Good times!",
        "I just found a great playlist for our road trip next week.",
        "I'll be there in 10 minutes. See you soon!",
        "Can you believe how fast time flies? It's already September!",
        "I love the smell of fresh flowers in the morning.",
        "I can't wait to see your new art exhibition. You're so talented!",
        "I'm considering a career change. Any advice for me?",
        "Let's plan a picnic in the park this weekend. It'll be fun!",
        "I made your favorite dessert. When can you come over?",
        "The view from the mountaintop was breathtaking. You should visit.",
        "Life is full of surprises. Embrace the journey!",
        "I'm feeling nostalgic about our college days. Those were the best!",
        "I just adopted a cute puppy. You have to meet him!",
        "I found a great deal on flights. Let's book that vacation!",
        "I'm so proud of your recent achievements. Keep shining!"
]

# Perform sentiment analysis and categorize the sentiment
sentiment_analysis_results = []
for message in sms_messages:
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    sentiment_analysis_results.append((message, sentiment, polarity))

sentiment_analysis_results
