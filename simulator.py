import random

def create_player_connections():
    number_players = int(input("How many players are there? "))
    player_names = {}
    conn_dict = {}
    for x in range(number_players):
        player_name = input("What is the name of player " + str(x+1) + "? ").lower()
        player_names[x] = player_name

    for x in range(number_players):
        conn_dict[x] = input("Which player does " + player_names[x] + " defeat? ")
    
    return player_names, conn_dict, number_players

def play_game(player_1_index, player_2_index):
    if player_1_index == player_2_index:
        return -1
    elif conn_dict[player_1_index] == player_names[player_2_index]:
        return player_1_index
    else:
        return player_2_index
    
def main():
    player_names, conn_dict, number_players = create_player_connections()
    iterations = int(input("How many times would you like to simulate the game?")
    plotting_vals = {}
    for x in range(number_players):
        plotting_vals[x] = 0
    for x in range(iterations):
        player_1_index = random.randint(0, number_players-1)
        player_2_index = random.randint(0, number_players-1)
        plotting_vals[play_game(player_1_index, player_2_index)]

    

    
            
        


create_player_connections()