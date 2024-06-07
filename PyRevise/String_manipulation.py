def reverse_String(text):
    String_list = text.split()
    
    reverse_String = String_list[::-1]
    reversed_String = ' '.join(reverse_String)
    return reversed_String

example_text = "Hello world this is a test"
reversed_text = reverse_String(example_text)
print(f"Reversed words: {reversed_text}")
