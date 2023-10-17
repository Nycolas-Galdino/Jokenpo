import random
from time import sleep

try: # Add the colors in windows <= 7
    from colorama import init
    init()
except:
    try:
        import os
        os.system('pip install colorama')
        from colorama import init
        init()
    except:
        pass

items = ['rock', 'paper', 'scissors']
h_points = 0 #Human points
c_points = 0 #Computer points
d_points = 0 #Draw points

def print_log(text:str, color:str = 'normal', bold:bool = False, underline:bool = False, sleep_t:float = 0.5, end:str = '\n'):
    """Print the text with formatation.
    
    Colors:
    - normal (default)
    - red
    - green
    - yellow
    - blue
    - purple
    - pink

    Args:
        text (str): Insert the text for formatations
        color (str, optional): Color of the text. Defaults to 'normal'.
        bold (bool, optional): Format text in bolder. Defaults to False.
        underline (bool, optional): Format style of text with underline. Defaults to False.
        sleep_t (float, optional): Time that will be waited before return. Defaults to 0.5.
        end (str, optional): How to terminate the text. Defaults is breakline. 
    """
    color = color.lower()
    colors = ['normal', 'red', 'green', 'yellow', 'blue', 'purple', 'pink']

    if color not in colors: raise Exception("The selected color is not in the list, please select one of the colors from the list.")

    b = "1;" if bold == True else ""
    u = "4;" if underline == True else ""

    if (color == "green"): print(f"""\033[{b}{u}32m{text}\033[0m""", end=end)
    elif (color == "blue"): print(f"""\033[{b}{u}36m{text}\033[0m""", end=end)
    elif (color == "red"): print(f"""\033[{b}{u}31m{text}\033[0m""", end=end)
    elif (color == "yellow"): print(f"""\033[{b}{u}33m{text}\033[0m""", end=end)
    elif (color == "purple"): print(f"""\033[{b}{u}35m{text}\033[0m""", end=end)
    elif (color == "pink"): print(f"""\033[{b}{u}34m{text}\033[0m""", end=end)
    else: print(f"""{text}""", end=end)

    sleep(sleep_t)

print_log("Welcome to the Rock Paper Scissors!", "blue", bold=True, underline=True)

while True:
    print_log("""Please, use the numbers for your choise.
            Choose your weapon:

            1 - Rock!
            2 - Paper!
            3 - Scissors!

            0 - Exit""")
    try:
        i = int(input('Your weapon: '))
    except ValueError:
        print_log("Unfortunately, this character is not acceptable to the game, please enter a \033[1;4mnumber\033[0m")
        continue

    if i == 0:
        print_log("Thank you for playing! Bye Bye! =D", "green", bold=True)
        quit()

    if i >= 4 or i<=-1:
        print_log("Please select rock, paper or scissors using numbers 1 to 3")
        continue

    choose = items[i-1]
    pc_choose = random.choice(items)
    print_log("Wait a moment! The computer is choosing a weapon...", "yellow")

    print_log("Ready?", color='blue', bold=True, sleep_t=1 )
    print_log("Jo...", color='blue', sleep_t=1 )
    print_log("ken..", color='blue', sleep_t=1 )
    print_log("po!", color='blue', sleep_t=1 )

    print_log(f"You chose {choose} and I chose {pc_choose}", sleep_t=1, end="... ")
    

    if choose == pc_choose:
        print_log(f"""\033[1mOmg!\033[0m We Draw! hahaha...""")
        d_points += 1

    if choose == 'rock':
        if pc_choose == 'paper':
            print_log(f"You loss!", color='red')
            c_points += 1
        if pc_choose == 'scissors':
            print_log(f"You won!", color = 'green')
            h_points += 1

    elif choose == 'paper':
        if pc_choose == 'scissors':
            print_log(f"You loss!", color='red')
            c_points += 1
        if pc_choose == 'rock':
            print_log(f"You won!", color = 'green')
            h_points += 1

    elif choose == 'scissors':
        if pc_choose == 'rock':
            print_log(f"You loss!", color='red')
            c_points += 1
        if pc_choose == 'paper':
            print_log(f"You won!", color = 'green')
            h_points += 1

    print_log(f'Human: {h_points} | Computer: {c_points} | Draw: {d_points}', underline=True, bold=True)
