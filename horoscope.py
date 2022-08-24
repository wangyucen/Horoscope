import  random
horoscope_dic = {"ARIES":["Get-togethers with friends or meetings with a small group.",
                          "Your imagination should be flying high today.",
                          "Keeping things in balance today might be tricky."],
                 "TAURUS":["Today things could be rather hectic at work.",
                           "Your financial goals are probably on the verge of becoming reality.",
                           "Things may be tough and aggressive today."],
                 "GEMINI":["Some new information could have you browsing the web and looking through books to learn.",
                           "Conversations with a friend whose good sense you trust could open your eyes to new career possibilities.",
                           "Make sure that the battle you fight today is yours."]}
print("\033[1:33m <<<<<welcome to satan's fortune teller corner>>>>>>")
print("\033[1:32m !!!safe to leave by speaking go to hell!!!")
def fortune_reader():
    noob = 0
    found = False
    while True:
        zodiac=input("\033[1:36m poor lost soul, speak to me your Zodiac, Santa will light your further path :-)")
        if zodiac == "go to hell":
            print("\033[1:31m oh hell no no no no n....")
            break
        for key in horoscope_dic.keys():
            if key == zodiac.upper():
                print("\033[1:31m Thinking.........")
                print(" ".join(random.choice(horoscope_dic[zodiac])))
                found = True
        if not found:
            if noob == 0:
                print("\033[1:31m what a poor guy, you can't even spell")
                noob += 1
            elif noob == 1:
                print("\033[1:31m so sad, you pathetic creature")
                noob += 1
            elif noob == 2:
                print("\033[1:31m now you getting me a bit angry, better take care")
                noob += 1
            elif noob == 3:
                print("\033[1:31m you have wasted all my patience, Hell satan!!!")
                print()
                print("\033[1:32m oh no no no,don't come to me")
                break


fortune_reader()