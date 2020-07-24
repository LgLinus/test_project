import entities.Player
class Player_repository:
    def get_players():
        players = entities.Player.Player("Sebbe", 'Fredrik', 'Linus')
        return players.name, players.name1, players.name2

## create PlayerRepository Class

## No need for __init__ function

## Functions:
## getPlayers()
## -- Return a hardcoded list of all players  (Player("Sebbe"), Player("Fredrik"), Player("Linus"))
## 
##


