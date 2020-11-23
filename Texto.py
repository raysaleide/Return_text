def first_word(text: str) -> str:
    # Insira seu código aqui
    if '.' in text:
        text = text.replace('.', ' ')
    elif ',' in text:
        text = text.replace(',',' ')
    get_word = text.split()
    return get_word[0]


# Não escreva nada abaixo dessa linha
if __name__ == '__main__':
    print("Examplo:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print('Terminou')