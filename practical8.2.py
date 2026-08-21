# Text Moderation Filter

feedback = input("Enter your feedback: ")

target_words = ["bad", "stupid", "hate"]

for word in target_words:
    feedback = feedback.replace(word, "***")
    feedback = feedback.replace(word.capitalize(), "***")

print("Moderated Feedback:", feedback)