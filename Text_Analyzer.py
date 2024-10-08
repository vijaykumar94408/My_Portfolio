# defining a function which take input as text variable and finds total character, unique words and word frequencies 
def analyze_text(text):
    try:
        words = text.split()
        total_characters = len(text)
        unique_words = set(words)
        word_frequencies = {}
        for word in words:
            word = word.lower()
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1
# printing output from here
        print("\n--- Text Analysis ---")
        print(f"Total words: {len(words)}")
        print(f"Total characters (including spaces): {total_characters}")
        print(f"Unique words: {len(unique_words)}")

        print("\nWord Frequencies:")
        for word, count in word_frequencies.items():
            print(f"{word}: {count} times")
    
    except Exception as e:
        print(f"An error occurred: {e}")
# defining a function to input text from user to validate it 
def get_text():
    try:
        text = input("Enter a paragraph of text: ")
        if not text.strip():
            raise ValueError("Error: Text cannot be empty.")
        return text
    except ValueError as e:
        print(e)
        return None


# this main function loops until user gives valid text and exit when analyzing the text operation is performemd 
def run_text_analyzer():
    while True:
        text = get_text()
        if text:
            analyze_text(text)
            break

run_text_analyzer()
# calling main function 