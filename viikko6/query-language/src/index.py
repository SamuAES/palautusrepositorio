from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(20, "assists"),
    #     PlaysIn("PHI")
    # )

    matcher1 = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
    )

    matcher2 = And(
    HasFewerThan(2, "goals"),
    PlaysIn("NYR")
    )

    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all))

    # matcher = Or(
    # HasAtLeast(45, "goals"),
    # HasAtLeast(70, "assists")
    # )

    # matcher = And(
    #     HasAtLeast(70, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("FLA"),
    #         PlaysIn("BOS")
    #     )
    # )

    # for player1, player2 in zip(stats.matches(matcher1), stats.matches(matcher2)):
    #     print(player1 == player2)

    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.plays_in("NYR").build()
    #matcher = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()
    
    m1 = (
    query
        .plays_in("PHI")
        .has_at_least(10, "assists")
        .has_fewer_than(10, "goals")
        .build()
    )

    m2 = (
    query
        .plays_in("EDM")
        .has_at_least(50, "points")
        .build()
    )

    matcher = query.one_of(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()