"""
Module Name: Player Score Analyzer Template
Description: Analyzes video game tournament scores, classifies players by skill level, and calculates the average and highest score.
Author: Kollier
"""

players = int(input("Enter the number of participating players: "))

scores = []
print("--- PLAYER SCORES ---")

for i in range(players):
    score = int(input(f"Enter the score for player {i + 1}: "))
    scores.append(score)

experts = 0
beginners = 0

for score in scores:
    if score >= 1500:
       experts += 1
    else:
       beginners += 1

average_score = sum(scores) / len(scores) if scores else 0
highest_score = max(scores) if scores else 0

print(f"Number of Expert-level players: {experts}")
print(f"Number of Beginner-level players: {beginners}")
print(f"Overall average score: {average_score}")
print(f"Highest score recorded: {highest_score}")