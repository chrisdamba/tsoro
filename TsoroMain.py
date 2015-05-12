from TsoroGameEngine import TsoroGameEngine


def start():
    start = False
    while start == False:
        start_option = raw_input("New game (N) or load a game (L)?: ").upper()
        
        if start_option == "NEW GAME" or start_option == "N":
            os.system('cls')        #clears screen
            os.system('color c')    #Light red
            
            player1 = player(raw_input("What is your name Player 1?: ").upper(), 'a')   #Light green
            player2 = AI("Alpha", 0)
            
            first, second = player1, player2
            Won = False
            start = True
            turn = 0
            
        elif start_option == "LOAD" or start_option == "L":

            raw_filenames = os.listdir(".\Saves")

            save_files = []
            for name in raw_filenames:

                if name.endswith('.pkl'):
                    save_files.append(os.path.join(".\Saves", name))

            if len(save_files) <1:
                print "No save files!"

            else:
                os.system('cls')
                save_files.reverse()
                print "Save Games:\n"
                for name in save_files:
                    print name[8:][:-4]+"\n"

                save_option =raw_input("What game would you like to load? (or BACK (B)): ").upper()
                if save_option == "B" or save_option == "BACK":
                    os.system('cls')
                else:
                    try:
                        opened_file = open('.\Saves\\'+save_option+'.pkl', 'rb')
                        data = pickle.load(opened_file)
                        
                        second, first, Won, turn = data
                        start = True
                    except Exception:
                        os.system('cls')
                        print "Not a valid name\n"

        else:
            print "try again\n"
            
    while Won==False:
    	tsoro = TsoroGameEngine(3)
		tsoro.print_board()
        first, second, Won, turn = play_turn(player1, player2, Won, turn)
        player2.turn(player1)
        
        
    raw_input("Hit enter to close. ")



if __name__ == '__main__':
    start()
