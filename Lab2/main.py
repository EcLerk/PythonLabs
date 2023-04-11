import re
import constants
import task1

if __name__ == '__main__':
    #принимаем текст и находим кол-во предложений
    text = input("Enter the text:")
    sentences = re.findall(constants.REGEX_SENTENCES, text)
    print(sentences)

    number_of_sentences = task1.delete_abbreviations(text, sentences)
    print("Количество предложений:", number_of_sentences)
    print("Количество недекларативных предложений:", task1.non_declarative(sentences))

    #поиск слов
    words = re.findall(constants.REGEX_WORDS, text)
    print("Количество слов:", len(words))
    print("Средняя длина слов в тексте:", task1.average_len(words))
