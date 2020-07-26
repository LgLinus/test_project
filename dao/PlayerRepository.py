from entities.Player import Player
class PlayerRepository:
    def get_players():
        players = Player("Sebbe")
        players1 = Player('Linus')
        players2 = Player('Fredrik')
        return [players, players1, players2]
