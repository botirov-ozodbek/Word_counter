
def count_words(text):
    words = text.split()
    
    total_words = len(words)

    total_chars = len(text)

    # Split the text by whitespace and filter out empty strings
    filtered_words = [word for word in words if word]
    return len(filtered_words)

# Example usage:
input_text = input("Enter your text: ").strip()
print(f"Total words: {count_words(input_text)}")
print(f"Total characters: {len(input_text)}")
print(f"Total characters (excluding spaces): {len(input_text.replace(' ', ''))}")
