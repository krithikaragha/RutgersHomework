# Create a path for the file
paragraph1 = "Resources/paragraph2.txt"

# Initializing variables and lists
num_words = 0
num_sentences = 0
sum_letter_counts = 0
avg_letter_count = 0
letter_counts = []
sentence_lengths = []
sum_sentence_length = 0
avg_sentence_length = 0

with open(paragraph1, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)  # approx. word count
        sentences = line.split(".")
        num_sentences += len(sentences) # approx. sentence count
        for word in words:
            letter_counts.append(len(word)) 
        for letter_count in letter_counts:
            sum_letter_counts += letter_count
        avg_letter_count = sum_letter_counts/ len(letter_counts) # avg. letter count
        for sentence in sentences:
            tokens = sentence.split()
            sentence_lengths.append(len(tokens))
        for sentence_length in sentence_lengths:
            sum_sentence_length += sentence_length
        avg_sentence_length = sum_sentence_length / len(sentence_lengths) # avg. sentence length

# Print the results
print("Approx. Word Count: ", num_words)
print("Approx. Sentence Count: ", num_sentences)
print("Average Letter Count: ", round(avg_letter_count, 2))
print("Average Sentence Length: ", round(avg_sentence_length, 2))