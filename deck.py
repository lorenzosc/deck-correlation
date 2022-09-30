import numpy as np

class Deck:
    def __init__(self, name: str, mu_table: dict):
        self.mu_table = mu_table
        self.name = name
        self.statistic_values()

    def statistic_values(self, field: dict = None):
        if type(self.mu_table) is not type({"a": 1}):
            raise Exception("The provided mu_table isn't in a dict data type")

        if field == None:
            average = np.mean(list(self.mu_table.values()))
            std = np.std(list(self.mu_table.values()))

        else:
            average = 0
            for key in field:
                average += self.mu_table.get(key, self.mu_table["Other"]) * field[key]

            std = 0
            for key in field:
                std += ( self.mu_table.get(key, self.mu_table["Other"]) - average ) ** 2 * field[key]
            std = std ** 0.5


        self.average_wr = average
        self.standard_deviation = std

    def __repr__ (self):
        return (f"Deck name: {self.name}\nDeck Average WR: {self.average_wr}\n" +
                f"Deck matchup table:\n{self.mu_table}")

    def update_wr (self, villain: str, new_wr: float) -> None:
        self.mu_table[villain] = new_wr
        self.statistic_values()

def compatibility (deck1: Deck, deck2: Deck, field: dict = None):
    if field == None:
        if deck1.mu_table.keys() != deck2.mu_table.keys():
            raise Exception("Couldn't define field and no field was provided")

        size = len(deck1.mu_table)
        playrate = 1 / size

        field = {}
        for key in deck1.mu_table:
            field[key] = playrate

    deck1.statistic_values(field=field)
    deck2.statistic_values(field=field)

    x = 0
    y = 0
    xy = 0
    x2 = 0
    y2 = 0
    for key in field:
        aux1 = deck1.mu_table.get( key, deck1.mu_table["Other"] )
        aux2 = deck2.mu_table.get( key, deck2.mu_table["Other"] )

        y += aux2 * field[key]
        y2 += aux2 ** 2 * field[key]
        x += aux1 * field[key]
        x2 += aux1 ** 2 * field[key]
        xy += aux1 * aux2 * field[key]

    coefficient = (xy - x*y) / ( (x2 - x**2) * (y2 - y**2) ) ** 0.5

    return coefficient