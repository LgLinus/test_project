import entities.Player
class Player_repository:
    def get_players():
        players = entities.Player.Player("Sebbe")
        Players1 = entities.Player.Player('Linus')
        Players2 = entities.Player.Player('Fredrik')
        return players.name, Players1.name, Players2.name

## create PlayerRepository Class

## No need for __init__ function

## Functions:
## getPlayers()
## -- Return a hardcoded list of all players  (Player("Sebbe"), Player("Fredrik"), Player("Linus"))
## 
##


