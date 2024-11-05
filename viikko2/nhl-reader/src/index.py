import requests
from player_reader import PlayerReader
from player_stats import PlayerStats
from player import Player
from rich import print
from rich.prompt import Prompt
from rich.console import Console

def main():
    
    print("\n[italic]NHL Statistics by nationality[/italic]")

    # Select season
    seasons = ["2018-19", "2019-20", "2020-21", "2022-23", "2023-24", "2024-25"]
    season = Prompt.ask(f"\nSelect season:", choices=seasons)

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    
    # Print scores
    while True:

        # Select nationality
        nationalities = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR",
                        "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"]
        nationality = Prompt.ask(f"\nSelect nationality:", choices=nationalities)

        #players = stats.top_scorers_by_nationality(nationality)

        # print(f"\n[italic]Top scorers for [magenta]{nationality}[/magenta][/italic]")
        # for player in players:
        #     print(player)
        table = stats.top_scorers_table(season=season, nationality=nationality)
        console = Console()
        console.print(table)


if __name__ == "__main__":
    main()