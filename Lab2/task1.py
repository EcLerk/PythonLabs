import constants


def non_declarative(sentences):
    sum = 0

    for char in sentences:
        if char != '.':
            sum += 1

    return sum

#find all words that match regex_words
def average_len(words):
    sum = 0

    for word in words:
        sum += len(word)

    average = sum / len(words)
    return average

def delete_abbreviations(text, sentences):
    text = text.lower()
    sentences_len = len(sentences)

    for i in constants.ABBREVIATIONS:
        sentences_len -= text.count(i)

    for i in constants.ANOTHER_ABBREVIATIONS:
        sentences_len -= 2 * text.count(i)

    return sentences_len