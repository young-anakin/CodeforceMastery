# Read the input string
s = input().strip()

# Split the string by "WUB" and filter out empty strings
words = [word for word in s.split("WUB") if word]

# Join the words with spaces
original_song = " ".join(words)

# Print the original song
print(original_song)
