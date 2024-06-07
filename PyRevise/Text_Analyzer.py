def analyze_text(text):
    words = text.split()
    word_count = len(words)
    
    char_count = 0
    for char in text:
        if char != " ":
            char_count += 1
    
    word_freq = {}
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    most_frequent_word = ""
    max_frequency = 0
    for word, frequency in word_freq.items():
        if frequency > max_frequency:
            max_frequency = frequency
            most_frequent_word = word
    
    analysis_results = {
        "word_count": word_count,
        "char_count": char_count,
        "most_frequent_word": most_frequent_word
    }
    
    return analysis_results

text = "This is a test text. This text contains some words. Words are repeated in this text."
analysis = analyze_text(text)
print("Analysis results:")
print("Word count:", analysis["word_count"])
print("Character count (excluding whitespaces):", analysis["char_count"])
print("Most frequent word:", analysis["most_frequent_word"])
