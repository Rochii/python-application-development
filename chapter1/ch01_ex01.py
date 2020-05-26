import random
import textwrap

def play():

    keep_playing = "y"

    # Print the game mission
    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("\033[1m" + "Attack of The Orcs v0.0.1:" + "\033[0m")
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")
    print(textwrap.fill(msg, width=width))
    print("\033[1m" + "Mission:" + "\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m" + "TIP:" + "\033[0m")
    print("Be careful as there are enemies lurking around!")
    print(dotted_line)

    while keep_playing == "y":
        # Create huts lists and place randomly 'enemy', 'friend' or 'unoccupied' in 5 huts    
        hut_states = ["enemy", "friend", "unoccupied"]
        huts = [random.choice(hut_states) for i in range(5)]

        # Prompt player to select a hut number
        num = int(input("\n\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"))

        # Print the occupant info
        print("Revealing the occupants...")
        msg = ""
        for i in range(len(huts)):
            occupant_info = "<%d:%s>"%(i+1, huts[i])
            if i+1 == num:
                occupant_info = "\033[1m" + occupant_info + "\033[0m"
            msg += occupant_info + " "
        print("\t" + msg)
        print(dotted_line)
        print("\033[1m" + "Entering hut %d... " % num + "\033[0m", end=' ')
        
        if huts[num-1] == "enemy":
            print("\033[1m" + "YOU LOSE! Better luck next time!" + "\033[0m")
        else:
            print("\033[1m" + "YOU WIN! Congratulations!" + "\033[0m")
        
        print(dotted_line)
        keep_playing = input("Play again? Yes(y)/No(n):")
    
if __name__ == "__main__":
    play()