### WRITTEN BY ALI ASHRAFY 2023
### MATHEMATICS AND STATISTICS RESEARCH COMPETITION
# 13 Aug 2023

### This code is the Monte Carlo/simulated approach to random walks. Our paper can be found at the GitHub:
# https://github.com/alislaboratory/MSRC2023



import random



def monte_carlo_simulation(start, gamma, trials=1000000):
    total_steps = 0

    for _ in range(trials):
        x, y = start
        steps = 0
        while (x, y) not in gamma:
            direction = random.choice(["up", "down", "left", "right"])
            if direction == "up":
                y -= 1
            elif direction == "down":
                y += 1
            elif direction == "left":
                x -= 1
            elif direction == "right":
                x += 1
            steps += 1
        total_steps += steps

    return total_steps / trials


# Running the Monte Carlo simulation for the spider problem


start_position = (6, 6)
gamma = [  # The coordinates for boundary curve gamma
    (6, 8),
    (7, 8),
    (8, 8),
    (8, 9),
    (9, 9),
    (10, 9),
    (10, 8),
    (10, 7),
    (10, 6),
    (10, 5),
    (9, 5),
    (8, 5),
    (8, 4),
    (8, 3),
    (8, 2),
    (7, 2),
    (6, 2),
    (5, 2),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (3, 5),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (3, 9),
    (4, 9),
    (4, 8),
    (5, 8),
]
monte_carlo_expected_time = monte_carlo_simulation(start_position, gamma)
print(monte_carlo_expected_time)
