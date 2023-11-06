import random

# This is a basic linear regression model with training
# Change this value to predict a test score for the number ofhours studied
hours_studied = 10



previous_study_hours = [10, 8, 11, 13, 5, 7, 9, 16, 6, 12]
previous_exam_scores = [90, 86, 85, 97, 77, 88, 90, 95, 81, 93]

# Function to predict test score using gradient descent
def predict_test_score(train_hours, train_scores, test_hours):
    m = random.random()
    b = random.random()

    # Hyperparameters
    # Parameters that aren't learned from data but that can significantly impact the model's performance
    learning_rate = 0.001
    num_iterations = 10000

    # Gradient Descent
    for _ in range(num_iterations):
        m_gradient = 0
        b_gradient = 0
        for i in range(len(train_hours)):
            x = train_hours[i]
            y = train_scores[i]
            y_pred = (m * x + b)
            # Calculate gradients
            m_gradient += (2 / len(train_hours)) * x * (y_pred - y)
            b_gradient += (2 / len(train_hours)) * (y_pred - y)
        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient

    # Predict test scores
    test_scores = [(m * x + b) for x in test_hours]

    # Make sure test scores are less than 100
    test_scores = [min(score, 100) for score in test_scores]
    return test_scores

# Predict test scores for test_hours_studied
test_hours_studied = [hours_studied]
predicted_scores = predict_test_score(previous_study_hours, previous_exam_scores, test_hours_studied)
print("Predicted test score for this week:", predicted_scores[0])
