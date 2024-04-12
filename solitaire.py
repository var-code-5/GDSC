import game_V

def main():
    game = game_V.game()
    game.initialize()
    game.display_legal_moves()
    game.display()
    while True:
        current_score = game.game_score()
        if current_score == 364:
            print("Congratulations You have successfully completed the game!!!")
            break
        inp = input("Your move : ")
        try:
            if inp == '0':
                print(f'your score : {current_score}')
                break
            elif inp == '1':
                game.display_legal_moves()
            elif inp == '2':
                game.move_turn_stock()
                game.display()
            elif inp == '3':
                if(game.move_stack_to_foundation()):
                    game.display()
                else:
                    print("Invalid move")
            else:
                inp_list = eval(inp)
                if(inp_list[0] == 1):
                    if game.move_pile_to_pile(inp_list[1],inp_list[2],inp_list[3]):
                        game.display()
                    else:
                        game.display()
                        print("Invalid move")
                        continue
                elif(inp_list[0] ==2):
                    if game.move_stack_to_pile(inp_list[1]):
                        game.display()
                    else:
                        game.display()
                        print("Invalid move")
                        continue
                elif(inp_list[0] ==3):
                    if game.move_pile_to_foundation(inp_list[1]):
                        game.display()
                    else:
                        game.display()
                        print("Invalid move")
                        continue
        except:
            print("Move Not Recognized")

if __name__ == '__main__':
    main()