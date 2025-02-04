# Jadyn Brabham
# Chapter 2, Assignment 2
# This program will create a list of 30 words and phrases commonly found
# in spam messages, ask the user to input an email message, and it will
# scan the message for each of those 30 words or phrases. It then creates
# a "spam score" for each occurrence of the words and phrases. The program
# rates the likelihood that the message is spam, and then displays the
# user's "spam score", likelihood that the message is spam, and the words
# and phrases that caused it to be spam.

# The calculate_spam_score function takes the user's email message and
# the keywords. It uses a for loop to check if any of the keywords are
# present in the message. If a keyword is found, it adds 1 to the spam
# score and adds the keyword to a list of found keywords.
def calculate_spam_score(email_message, spam_keywords):
    spam_score = 0
    found_keywords = []

    # Check each keyword or phrase in the message
    for keyword in spam_keywords:
        if keyword.lower() in email_message.lower():
            spam_score += 1
            found_keywords.append(keyword)

    return spam_score, found_keywords

# The determine_spam_likelihood function takes the spam score and returns
# a string indicating the likelihood of the message being spam based on
# the score.
def determine_spam_likelihood(spam_score):
    if spam_score >= 10:
        return "High likelihood the message is spam."
    elif spam_score >= 5:
        return "Medium likelihood the message is spam."
    else:
        return "Low likelihood the message is spam."

# The main function defines the spam keywords/phrases, asks the user for
# an email message, and then uses the previous 2 functions to calculate the
# spam score and likelihood of the message being spam. Then it displays
# the spam score, likelihood, and keywords that were found.
def main():
    # Define the common keywords and phrases
    spam_keywords = ["act now", "double your cash", "free",
                     "immediate action is required", "congratulations",
                     "100% guaranteed", "full refund", "earn extra cash",
                     "double your income", "final offer", "Instant savings",
                     "last chance", "risk-free", "credit card",
                     "limited offer", "investment opportunity", "urgent",
                     "claim here", "receive", "click here", "exclusive offer",
                     "loan approval", "winner", "hurry", "deadline",
                     "time-sensitive", "clear debt", "eliminate bad credit",
                     "free trial", "discreet shipping"]

    # Get email message input from the user
    email_message = input('Enter the email message to analyze: ')

    # Calculate the spam score and get keywords found
    spam_score, found_keywords = calculate_spam_score(email_message, spam_keywords)

    # Determine the likelihood of being spam
    spam_likelihood = determine_spam_likelihood(spam_score)

    # Display the results
    print(f'\nSpam Score: {spam_score}')
    print(spam_likelihood)
    if found_keywords:
        print('Keywords/Phrases found that indicate spam:')
        for keyword in found_keywords:
            print(f'- {keyword}')
    else:
        print('No spam indicators found.')

# Call the main function
if __name__ == "__main__":
    main()
