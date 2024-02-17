#File: q3.py
#Author: Leah Philip
#Date: 02/16/2024
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program takes input on five subjects in one line and outputs them as an array.
def get_scores():
    try:
        scores = list(map(int, input("Enter the scores for 5 subjects (separated by space): ").split()))
        if len(scores) != 5 or not all(0 <= score <= 100 for score in scores):
            raise ValueError("Invalid input. Please enter 5 scores between 0 and 100.")
        return scores
    except ValueError as e:
        print(e)
        return get_scores()

def calculate_average(scores):
    return sum(scores) / len(scores)

def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    else:
        return 'D'

def update_scores(scores):
    # Change score 5 such that the average becomes 95
    new_score_5 = (95 * 5 - sum(scores[:4])) / 1
    scores[4] = new_score_5
    return scores

def validate_scores(scores):
    return all(0 <= score <= 100 for score in scores)

def main():
    scores = get_scores()

    average_score = calculate_average(scores)
    print(f"Average Score: {average_score:.2f}")

    grade = calculate_grade(average_score)
    print(f"Grade: {grade}")

    updated_scores = update_scores(scores)
    print(f"Updated Score Array: {updated_scores}")

    valid_scores = validate_scores(updated_scores)
    print(f"Is test score 5 valid?: {valid_scores}")

if __name__ == "__main__":
    main()
