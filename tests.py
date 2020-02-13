import axelrod as axl
import Rochambeau

#Create matches between two players:
players = (Rochambeau(), axl.TitForTat())
match = axl.Match(players, 5)
interactions = match.play()
print(interactions)