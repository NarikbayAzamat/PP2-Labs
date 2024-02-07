def solve(numheads, numlegs):
    chickens = (numlegs - (numheads * 2)) / 2
    rabbits = numheads - chickens

    return f"{chickens} chickens, {rabbits} rabbits."

x = solve(35, 94)
print(x)