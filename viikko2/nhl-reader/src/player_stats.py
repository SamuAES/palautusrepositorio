from player_reader import PlayerReader
from rich.table import Table

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        return filter(lambda x: x.nationality == nationality, self.players)

    def top_scorers_table(self, season:str, nationality:str):

        table = Table(title=f"\nTop scorers of {nationality} season {season}")

        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        for player in filter(lambda x: x.nationality == nationality, self.players):
            table.add_row(player.name, player.team, f"{player.goals}", f"{player.assists}", f"{player.get_points()}")

        return table





    
        