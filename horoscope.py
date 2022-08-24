import  random
horoscope_dic = {"ARIES":["Get-togethers with friends or meetings with a small group.",
                          "Your imagination should be flying high today.",
                          "Keeping things in balance today might be tricky."],
                 "TAURUS":["Today things could be rather hectic at work.",
                           "Your financial goals are probably on the verge of becoming reality.",
                           "Things may be tough and aggressive today."],
                 "GEMINI":["Some new information could have you browsing the web and looking through books to learn.",
                           "Conversations with a friend whose good sense you trust could open your eyes to new career possibilities.",
                           "Make sure that the battle you fight today is yours."],
                 "CANCER":["Today you might learn about new and creative ways to increase your income. ",
                           "Strange dreams, insights, or visions could upend your spiritual orientation. ",
                           "Wake up on the right side of bed"],
                 "LEO":["Social events could put you in touch with interesting people in intriguing professions. ",
                        "A friend you may not have seen for a while could awaken strange new feelings for which you're unprepared. ",
                        "You may feel a strong connection with your fanciful, romantic side today. "],
                 "VIRGO":["A friend or colleague could recommend some books that you want to read right away. ",
                          "The formation of a new business partnership might transform your working life. ",
                          "Give people the benefit of the doubt today. "],
                 "LIBRA":["Today your mind will be quick, insightful, and inspired. ",
                          "Unfinished job tasks might have you wanting to pitch in and get them done no matter what it takes. ",
                          "Some action you took yesterday may be opposed today. "],
                 "SCORPIO":["If visitors are able to pop in and out during the day. ",
                            "Today you're apt to feel very sensual and passionate. ",
                            "If you find yourself in a slump today. "],
                 "SAGITTARIUS":[" Don't be surprised if your inbox fills with email or your phone rings off the hook. ",
                                "A powerful desire for a current or potential romantic partner might come over you today. ",
                                "Use the day's boisterous energy to take charge and make things happen. "],
                 "CAPRICORN":["Inspiration is the word for today. ",
                              "A powerful need to reach someone either for business or personal reasons could have you spending a lot of time on the phone. ",
                              "There's apt to be powerful aggression today that may leave you feeling like you want to declare war on everyone. "],
                 "AQUARIUS":["Today your physical and mental energy should be operating at a very high level. ",
                             "Money matters could prove obsessive today. ",
                             "You may run into some tension today as fantasy gets in the way of your plan of attack. "],
                 "PISCES":["Your intuition is likely to be very keen today, Pisces. Accurate psychic insights could come to you thick and fast. ",
                           "Today you should be looking especially good and feeling particularly passionate and sensual. ",
                           " You may run into a great deal of frustration if you try to fight the current circumstances. "]}

print("\033[1:33m <<<<<welcome to satan's fortune teller corner>>>>>>")
print("             .,:cccccccccc:,. \n" +
"       ,lolc:,'.cccccccc.',:clll,.\n" +
"      .cll:.                .:llc'\n" +
"    .ld:.,dl'              'ld,.:do.\n"+
"   ;xl.  .oOlc;.        .;clko.  .cx;\n" +
"  :k:     'o;.,cc;.  .;cc,.,o'     ;kc\n" +
" ;k:       :o.  .colloc.  .o:       ;k:\n"+
".xo.       .lc..:c,',;c:'.:l.        lx.\n"+
";k;         ;dl:'      ':ld;         ,k:\n"+
"ck'      .,ccll.        .ol;c;.      .kl\n"+
":k'   .':c;. .lc        :o. .;cc,.   'kc\n"+
"'kc 'lxdc'....:d;......,oc....':dxo'.:k,\n"+
" co;:lc:;;;;;;,ld:;;;;cdl;;;;;;;;cc:;oc.\n"+
" .do.          .l:    ;l.          .ox. \n"+
"  .dd.          ,o'  .o;          .od'\n" +
"  .lx:.         cl'.ll         .:xl.\n" +
"     'odc.       .oOOd.       .:do'\n" +
"       .cooc,.    ,xk;    .,:ooc.\n"+
"          .:llllccccccccllll:.\n"+
"              .;cc;;:c;cd.")
print("\033[1:32m !!!safe to leave by speaking go to hell!!!")
def fortune_reader():
    noob = 0
    while True:
        found = False
        zodiac=input("\033[1:36m poor lost soul, speak to me your Zodiac, Santa will light your further path :-)\n")
        if zodiac == "go to hell":
            print("\033[1:31m oh hell no no no no n....")
            break
        for key in horoscope_dic.keys():
            if key == zodiac.upper():
                print("\033[1:31m Thinking.........")
                print(" ".join(random.choice(horoscope_dic[zodiac.upper()])))
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
                print("\033[1:32m oh no no no,leave me alone")
                break


fortune_reader()