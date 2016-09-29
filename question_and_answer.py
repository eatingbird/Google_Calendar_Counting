def ask_and_answer():
    name = input("name?")
    quest = input("quest?")
    color = input("color?")
    return ("Ah, so your name is %s, your quest is %s, "\
          "and your favorite color is %s." %(name, quest, color))


print (ask_and_answer())
