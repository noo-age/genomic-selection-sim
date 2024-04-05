library(ggplot2)
library(rgl)

r = 0.7 # r-correlation of PGS to true genetic score
prob_viable = 1 # probability that a given embryo is viable (can be used for next stage of IES or implanted)
num_trials = 100 # num trials for tests


plot_SD_over_multiple_rounds_over_n <- function(n_values, r, prob_viable, num_trials, num_rounds) {
  # Create a vector to store the average score for each value of n
  avg_scores <- numeric(length(n_values))
  
  # For each value of n
  for (i in seq_along(n_values)) {
    n <- n_values[i]
    
    # Initialize the mean score
    mean_score <- 0
    
    # Repeat for a number of rounds
    for (j in 1:num_rounds) {
      # Generate the score for a number of trials and take the average
      scores <- replicate(num_trials, {
        true_values <- rnorm(n, mean = mean_score)
        polygenic_scores <- r * true_values + sqrt(1 - r^2) * rnorm(n)
        sorted_indices <- order(polygenic_scores, decreasing = TRUE)
        for (k in sorted_indices) {
          rand_num <- runif(1)
          if (rand_num <= prob_viable) {
            return(true_values[k])
          }
        }
        return(NA)
      })
      # Update the mean score
      mean_score <- mean(scores, na.rm = TRUE)
    }
    
    # Save the final mean score
    avg_scores[i] <- mean_score /2
  }
  
  # Create a data frame with the results
  results <- data.frame(
    n = n_values,
    avg_score = avg_scores
  )
  
  # Plot the results
  ggplot(results, aes(x = n, y = avg_score)) +
    geom_line() +
    labs(x = "Number of eggs", y = "Expected z-score") +
    theme_minimal()
}


plot_expected_score_3d <- function(n_values, r, prob_viable, num_trials, num_rounds_values) {
  # Create a matrix to store the average score for each combination of n and num_rounds
  avg_scores <- matrix(nrow = length(n_values), ncol = length(num_rounds_values))
  
  # For each value of n and num_rounds
  for (i in seq_along(n_values)) {
    for (j in seq_along(num_rounds_values)) {
      n <- n_values[i]
      num_rounds <- num_rounds_values[j]
      
      # Initialize the mean score
      mean_score <- 0
      
      # Repeat for a number of rounds
      for (k in 1:num_rounds) {
        # Generate the score for a number of trials and take the average
        scores <- replicate(num_trials, {
          true_values <- rnorm(n, mean = mean_score)
          polygenic_scores <- r * true_values + sqrt(1 - r^2) * rnorm(n)
          sorted_indices <- order(polygenic_scores, decreasing = TRUE)
          for (l in sorted_indices) {
            rand_num <- runif(1)
            if (rand_num <= prob_viable) {
              return(true_values[l])
            }
          }
          return(NA)
        })
        # Update the mean score
        mean_score <- mean(scores, na.rm = TRUE)
      }
      
      # Save the final mean score, dividing by 2 to account for SD of embryos being half of population SD
      avg_scores[i, j] <- mean_score / 2
    }
  }
  
  # Plot the results
  colors <- colorRampPalette(c("blue", "green", "yellow", "red"))(20)
  persp(x = n_values, y = num_rounds_values, z = avg_scores, xlab = "# of eggs", ylab = "# of rounds", zlab = "SDs", theta = 30,col = colors[cut(avg_scores, breaks = 20)])
}

# Test the function
n_values <- seq(100, 300, by = 10)
num_rounds_values <- 1:100
plot_expected_score_3d(n_values, r = r, prob_viable = prob_viable, num_trials = num_trials, num_rounds_values = num_rounds_values)



