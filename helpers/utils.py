def save_results(word_frequency):
    with open('files/results.txt', 'w') as file:

        for word, count in word_frequency:
            file.write(f"{word}: {count}\n")
