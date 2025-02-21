import os

SCORE_FILE = "scores.txt"

def add_score(player_name, score):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{player_name}, {score}")

def get_top_scores():
    if not os.path.exists("scores.txt"):
        print("No scores available.")
        return

    with open("scores.txt", "r") as file:
        scores = [line.strip().split(",") for line in file.readlines()]

    # Convert scores to integers and sort in descending order
    scores = [(name, int(score)) for name, score in scores]
    scores.sort(key=lambda x: x[1], reverse=True)

    # Display the top 5 scores
    print("Top 5 Scores:")
    for i, (name, score) in enumerate(scores[:5], start=1):
        print(f"{i}. {name} - {score}")

# Example Usage
add_score("Alice", 50)
add_score("Bob", 80)
add_score("Charlie", 70)
add_score("David", 90)
add_score("Eve", 60)

get_top_scores()