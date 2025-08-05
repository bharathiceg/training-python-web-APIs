from game.get_input import get_input
from game.generator import generate_number,test_guess
def play_game():
    gen_num= generate_number()
    chance=0

    while True:
        guess=get_input()
        chance+=1
        result= test_guess(gen_num,guess)
        print(result)

        if(result=="correct"):
            print(f"ypu guessed in {chance} attempts")
            break

def main():
    while True:
        play_game()
        again= input("IF YOU want AGAIN GIVE y/n").strip().lower()
        if(again!='y'):
            print("Good bye")
            break
if __name__ == "__main__":
    main()

        
