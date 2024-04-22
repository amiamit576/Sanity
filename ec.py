def word_count(paragraph):
    # Replace periods with spaces to ensure they are treated as word separators
    paragraph = paragraph.replace('.', ' ')

    # Split the paragraph into words using spaces as separators
    words = paragraph.split()

    # Count the number of words
    word_count = len(words)

    return word_count


def main():
    paragraph = input("Enter a paragraph: ")
    total_words = word_count(paragraph)
    print("Total word count:", total_words)


if __name__ == "__main__":
    main()
