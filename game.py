import random


class Wordle:

    def __init__(self) -> None:
        self.today_word="house"
        #self.get_word()

    def get_word(self):
        # Get a random word from the file
        with open("words.txt","r") as file:
            words=file.read()
            words=list(map(str,words.split()))
            self.today_word=random.choice(words)

    def check_word(self,word):
        reply=""
        if word.lower()==self.today_word:
            return "🟩🟩🟩🟩🟩","Congratulations 🥳🎉 You won the game.🥳🎉",1
        if len(word)!=5:
            return "It need to have 5 letters.",0
        else:
            for i in range(len(word)):
                if word[i] in self.today_word:
                    if word[i]==self.today_word[i]:
                        reply+="🟩"
                    else:
                        reply+="🟨"
                else:
                    reply+="🟫"
        return word.upper(),reply
            
    

# game=Wordle()
# for i in range(5):
#     word=input("Enter your Guess: ")
#     reply=game.check_word(word=word)
#     if reply==1:break
#     if i==4:
#         print("Ohh you lost🔴😔\n Better Luck Next Time")