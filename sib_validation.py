import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_siblings(num_pairs, genetic_effect, shared_environment_effect):
    """
    Generate synthetic data for sibling pairs.
    :param num_pairs: Number of sibling pairs to generate.
    :param genetic_effect: Effect of genetics on the trait/disease (standard deviation).
    :param shared_environment_effect: Shared environmental effect on the trait/disease.
    :return: Two arrays representing the trait values or disease risk scores for each sibling.
    """
    # Genetic component: siblings share some genetic information, but also have unique parts
    shared_genetics = np.random.normal(0, genetic_effect, num_pairs)
    unique_genetics_sib1 = np.random.normal(0, genetic_effect, num_pairs)
    unique_genetics_sib2 = np.random.normal(0, genetic_effect, num_pairs)

    # Environmental component
    shared_environment = np.random.normal(0, shared_environment_effect, num_pairs)

    # Combine effects for each sibling
    sib1_trait = shared_genetics + unique_genetics_sib1 + shared_environment
    sib2_trait = shared_genetics + unique_genetics_sib2 + shared_environment

    return sib1_trait, sib2_trait

def calculate_predictive_accuracy(sib1_trait, sib2_trait):
    """
    Calculate the accuracy of prediction (how often the one with higher genetic score has the higher trait value).
    :param sib1_trait: Trait values or disease risk scores for sibling 1.
    :param sib2_trait: Trait values or disease risk scores for sibling 2.
    :return: Prediction accuracy as a fraction.
    """
    correct_predictions = np.sum(sib1_trait > sib2_trait)
    total_predictions = len(sib1_trait)
    accuracy = correct_predictions / total_predictions
    return accuracy

# Parameters for the simulation
num_pairs = 10000
genetic_effect = 1  # Standard deviation of the genetic effect
shared_environment_effect = 0.5  # Standard deviation of the shared environmental effect

# Generate synthetic sibling data
sib1_trait, sib2_trait = generate_siblings(num_pairs, genetic_effect, shared_environment_effect)

# Calculate predictive accuracy
accuracy = calculate_predictive_accuracy(sib1_trait, sib2_trait)
print(f"Predictive accuracy between siblings: {accuracy:.2f}")

# Plotting the distribution of trait differences
plt.hist(sib1_trait - sib2_trait, bins=50, alpha=0.7, label='Trait Difference Distribution')
plt.xlabel('Difference in Trait Values')
plt.ylabel('Frequency')
plt.title('Distribution of Trait Differences Between Siblings')
plt.legend()
plt.show()