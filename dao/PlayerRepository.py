import entities.Player
class Player_repository:
    def get_players():
        players = entities.Player.Player("Sebbe")
        players1 = entities.Player.Player('Linus')
        players2 = entities.Player.Player('Fredrik')
        return [players, players1, players2]


