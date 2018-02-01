def question():
    q = input('What is your question? ')
    while q != 'quit':
        if "?" in q:
            print('response')
        else:
            print("I'm sorry, I can only answer questions")
        q = input('What is your question? ')

question()
