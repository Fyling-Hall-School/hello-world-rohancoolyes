import random


def filenamelogin():
    value = 0
    
    logindetails = []
    file = open("logindetails.txt","r")
    for line in file:
        logindetails.append(line.strip())
        
    #passwordchecker
    rohan = "cool123"
    mrwheeler = "nice123"
    sarah = "girl123"
    ali = "best123"

    print("authorised users are:",logindetails)
    login = str(input("Enter your name to authenticate: "))
    password = str(input("Enter your password to authenticate: "))
    while True:
        if login in logindetails:
            if ((login == "rohan") or (login == "Rohan")):
                if password == rohan:
                    print("you have been authenticated!")
                    value = 0+1
                    print(value)
                    break
                else:
                    print("you are not authenticated, leavveeee")
                    break

            elif ((login == "sarah") or (login == "Sarah")):
                if password == sarah:
                    print("you have been authenticated!")
                    value = 0+1
                    print(value)
                    break
                else:
                    print("you are not authenticated, leavveeee")
                    break

            elif ((login == "ali") or (login == "Ali")):
                if password == ali:
                    print("you have been authenticated!")
                    value = 0+1
                    print(value)
                    break
                else:
                    print("you are not authenticated, leavveeee")
                    break

            elif ((login == "Mr Wheeler") or (login == "Mr.Wheeler") or (login == "mrwheeler") or (login == "mr wheeler")):
                if password == mrwheeler:
                    print("you have been authenticated!")
                    value = 0+1
                    print(value)
                    break
                else:
                    print("you are not authenticated, leavveeee")
                    break
            else:
                print("this name and password is not in the database")
             
def musicgame():
    music = []
    file = open("music.txt","r", encoding='utf-8')
    for line in file:
        music.append(line.strip().split(' - '))
    artist, title = random.choice(music)
    print("Artist:" ,artist, "First Letter of Title:", title[0])
    run = True
    score = 0
    count = 0
    while run:
        answer = input("Guess the song: ")
        if count == 2:
            print("you have been dropped, progam ends")
            run = False
        elif answer == title:
            print("You have gotten it correct!!!!")
            score = score + 1
            print(score)
            break
        else:
            print("You have gotten it wrong retry!!!")
            count = count + 1
            print(count)
    name = str(input("could you please name your gamer username: "))
    file = open("scores.txt","a")
    file.write(name)
    file.write(score)
    



filenamelogin()
musicgame()


