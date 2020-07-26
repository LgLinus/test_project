import entities.Player
class Player_repository:
    def get_players():
        players = entities.Player.Player("Sebbe")
        players1 = entities.Player.Player('Linus')
        players2 = entities.Player.Player('Fredrik')
        return [players, players1, players2]
## create PlayerRepository Class

## No need for __init__ function

## Functions:
## getPlayers()
## -- Return a hardcoded list of all players  (Player("Sebbe"), Player("Fredrik"), Player("Linus"))
## 
##


