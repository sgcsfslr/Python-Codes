# Air quality Indicator app
# pm25.py
# Reference from China University Module
""" Old version
def main(): # define function call "main"
    PM = eval(input("What is today's PM2.5? ")) # Prompt for an input value
    if PM > 75:
        print("Unhealty. Be careful!")
    if PM >=35:
        print("Moderate. Wear masks")
    if PM < 35:
        print("Good. Go running!")

main()
""""
# Improved version
def main(): # define function call "main"
    PM = eval(input("What is today's PM2.5? ")) # Prompt for an input value
    if PM < 35:
        print("Good. Go running!")
    elif PM <= 75:
        print("Moderate. Wear masks!")
    elif PM > 75:
        print("Unhealty. Be careful!")

main()
