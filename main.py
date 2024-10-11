class Team:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        self.players.append(name)

    def remove_player(self, name):
        if name in self.players:
            self.players.remove(name)

    def show_team(self):
        print("Гравці команди:", self.players)

# Приклад використання
team = Team()
team.add_player("Володимир")
team.add_player("Олександр")
team.show_team()

team.remove_player("Олександр")
team.show_team()

team.add_player("Петро")
team.show_team()