class GameStore:
    def __init__(self):
        self.games = []

    def search_games(self, game_name):
        if game_name in self.games:
            print(f"Game {game_name} found")
        else:
            print("Game not found")

# Instantiate and demonstrate the Game Store
game_store = GameStore()
game_store.search_games("Example Game")
