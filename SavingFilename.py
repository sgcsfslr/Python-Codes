# Saving filename setting.txt 
# Test needs to be executed on a folder with full write access rights.
setting_file = open("setting.txt", "r")
name = setting_file.readline()
setting_file.close()
if name =="":
    name_input = input("Hellow, nice to meet you. What's your name?")
    setting_file = open("setting.txt", "w")
    setting_file.write(name_input)
    setting_file.close() # somehow error appears in Ms Studio but works fine in Python IDE
    print("Thank you, " + name_input)
else:
    print("Nice to have you back, " + name)
emotion = input("How are you?")
if "good" in emotion:
    print("Great, have a nice day then")
elif emotion.find("not") != -1:
    print("Oh, tomorrow will be better")
else:
    print("Sorry, I didn't understand you")