def bowling_averages(game1, game2, game3, handicap):
    average = (game1 + game2 + game3) / 3
    average_with_handicap = average + handicap
    return average, average_with_handicap

last_name = input("Enter bowler last name: ")
game1 = float(input("Enter game 1 score: "))
game2 = float(input("Enter game 2 score: "))
game3 = float(input("Enter game 3 score: "))
handicap = float(input("Enter handicap: "))

average, adjusted_average = bowling_averages(game1, game2, game3, handicap)
print("Bowler:", last_name)
print("Average score:", format(average, ".2f"))
print("Average with handicap:", format(adjusted_average, ".2f"))
