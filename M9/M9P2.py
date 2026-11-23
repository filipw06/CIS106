def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats


playerCount = 0
again = "Y"
while again == "Y":
    lastName = input("Enter player last name: ")
    hits = int(input("Enter hits: "))
    atBats = int(input("Enter at bats: "))
    average = batting_average(hits, atBats)
    print("Player:", lastName)
    print("Batting average:", format(average, ".3f"))
    playerCount = playerCount + 1
    again = input("Enter Y to continue or N to stop: ").upper()
print("Number of players:", playerCount)
