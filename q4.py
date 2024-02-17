#File: q4.py
#Author: Leah Philip
#Date: 02/07/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program prints the average and variance of weights on user input.
def calculate_mean(data):
    return sum(data) / len(data)
def calculate_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)
def calculate_std_dev(variance):
    return variance ** 0.5
def main():
    weights_str = input("Enter the weights: ")
    weights = [float(x) for x in weights_str.split()]
    if len(weights) != 5:
        print("Error: Please provide exactly 5 weights.")
        return
    mean = calculate_mean(weights)
    variance = calculate_variance(weights, mean)
    std_dev = calculate_std_dev(variance)
    print(f"Mean: {mean}")
    print(f"Variance: {variance} Lbs^2")
    print(f"Standard Deviation: {std_dev} Lbs")


if __name__ == "__main__":
    main()
