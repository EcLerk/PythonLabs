import re
import constants
import task1
import task2

def main():
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

    n = input("Введите n и k:")
    k = input()
    task1.find_ngrams(words, int(n), int(k))

    #############################################
    #TASK2

    username = input("Введите имя пользователя:")
    collection = task2.MyCollection(username)

    print("add <key> [key, …] – add one or more elements to the container \n"
          "remove <key> – delete key from container\n"
          "find <key> [key, …] – check if the element is presented in the container\n"
          "list – print all elements of container\n"
          "grep <regex> – check the value in the container by regular expression\n"
          "save/load – save container to file/load container from file\n"
          "switch – switches to another user\n"
          "------------------------------------\n")


    while True:
        operation = input("Введите команду:").lower()

        match operation:
            case "add":
                collection.add(input("Введите значение:"))
            case "remove":
                collection.remove(input("Введите значение:"))

            case "find":
                collection.find(input("Введите значение:"))

            case "list":
                collection.list()

            case "grep":
                collection.grep(input("Введите регулярное выражение:"))

            case "save":
                collection.save()

            case "load":
                collection.load()

            case "switch":
                ask_for_save(collection)
                collection.switch(input("Введите имя пользователя:"))

            case "q":
                ask_for_save(collection)
                break

def ask_for_save(collection):
    print("Do you want to save the container?\n Enter Y|N:")

    while True:
        answer = input().lower()

        if answer == "y":
            collection.save()
            break
        elif answer == "n":
            break
        else:
            print("Try again")
            continue

if __name__ == '__main__':
    main()