import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o")

# Example text
text = "Hey There! How are you doing today?"

# Tokenize the text
tokens = enc.encode(text)
print(tokens)

# Decode the tokens back to text
decoded_text = enc.decode(tokens)
print(decoded_text)