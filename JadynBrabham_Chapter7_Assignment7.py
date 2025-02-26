# Jadyn Brabham
# Chapter 7, Assignment 7
# This program prompts the user to input a paragraph, including
# sentences which begin with numbers. Then the program displays each sentence
# along with the total count of sentences in the paragraph.

import re

# Function to split the paragraph into individual sentences
def split_into_sentences(paragraph):
    # Regular expression to split paragraph at sentence-ending punctuation
    sentences = re.split(r'(?<=[.!?]) +', paragraph)
    return sentences

# Function to count the number of sentences
def count_sentences(sentences):
    return len(sentences)

# Function to prompt the user to input the paragraph; then it calls
# the split_into_sentences function and count_sentences function.
# Then it displays each sentence and the total count of sentences.
def main():
    # Get paragraph input from the user
    paragraph = input("Enter a paragraph: ")

    # Split the paragraph into sentences
    sentences = split_into_sentences(paragraph)

    # Count the number of sentences
    sentence_count = count_sentences(sentences)

    # Display each sentence and the total count of sentences
    print("\nSentences in the paragraph: ")
    for idx, sentence, in enumerate(sentences, 1):
        print(f"Sentence {idx}: {sentence}")

    # Display the total number of sentences
    print(f"\nTotal number of sentences: {sentence_count}")

if __name__ == "__main__":
    main()