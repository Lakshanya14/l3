from textblob import TextBlob

print("Hello, I am an AI chatbot which can detect your sentiment.")
print("What is your name?")
name = input()
print(f"Wow! {name}, that's a really good name.")
print("How are you feeling today?")
feeling = input().lower()  # Convert input to lowercase for easier comparison

# Check for positive sentiments
if feeling in ["happy", "good", "great", "fine"]:
    print("I am glad to hear that you are feeling good.")
    print("Positive sentiment detected.")
# Check for negative sentiments
elif feeling in ["sad", "bad", "angry", "depressed"]:
    print("I am sorry to hear that you are feeling bad.")
    print("Negative sentiment detected.")
# Neutral or unrecognized sentiments
else:
    print("It's okay, sometimes it happens that you are not able to express your feelings.")
    print("Neutral sentiment detected.")

print("If you want to end our conversation, please type 'exit'.")
exit_input = input().lower()  # Convert input to lowercase for consistency
if exit_input == "exit":
    print("Thank you for chatting with me, have a great day!")
    exit()
else:
    print("That's great, let's talk more!")