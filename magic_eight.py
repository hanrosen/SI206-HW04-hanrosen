import random
lst = ['It is certain', 'It is decidely so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again']
def question():
    q = input('What is your question? ')
    while q != 'quit':
        if "?" in q:
            print(random.choice(lst))
        else:
            print("I'm sorry, I can only answer questions")
        q = input('What is your question? ')

question()
