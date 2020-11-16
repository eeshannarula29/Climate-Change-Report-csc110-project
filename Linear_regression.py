"""
This file will act as a library to train a liner model
to our data for future predictions.

Resources:
- https://towardsdatascience.com/linear-regression-using-python-b136c91bf0a2
- https://matplotlib.org/devdocs/contents.html
"""

import matplotlib.pyplot as plt
import numpy as np

"""
A liner regression mode is a straight line which best describes relation between 
variables. The model can be trained in two ways, with maths or machine learning 
technique called gradient decent. We would use gradient decent and matrices to 
find the line of best fit.

The equation of line can be denoted by y = mx + b, where y is the variable we want to 
predict and x predictor variable used to predict variable y. m is the slope and b is the
bias or intercept of that line. 

In machine learning terminology this slope m is denoted by theta 1 and is called the weight, 
and the intercept b is called the bias and denote by theta 0. we want to compute these 
parameters of the line. 

So how do we do this?

1) first we initialize our weights and biases randomly. 

2) then we compute the cost of those weights and biases, which is the 
   average squared difference in the predicted and actual values of our
   dataset. 

3) our aim is to reduce this cost, by changing the values of the weights 
   and biases
   
4) This is done by the use of gradient decent formula, where we compute 
   the partial derivative of the cost function which respect to theta 1
   to modify theta 1 and with respect to theta 0 to modify theta 0. The 
   value we just calculate multiplied by alpha, is the number we would 
   change our weights and bias by. 
   
   here alpha is the learning rate which prevents everything from being 
   to large, and keeps everything in bound. 
   
5) we repeat step 2 to 5 multiple times, to get a line of best fit. the 
   number of times we repeat step 2 to step 5 is called the number of 
   epochs.    
   
*  A very low learning rate can take the model too many epochs to learn, 
   and too high value of learning rate wont let the learn, and instead can
   make it worse with time. 
"""


def predict(x: np.array, weights: np.array) -> np.array:
    """Returns the prediction made by the line, by passing
    in the value of x in equation y = theta_1*x + theta_0"""
    return np.dot(x, weights)


def cost(x: np.array, y: np.array, weights: np.array) -> np.array:
    """Return the cost of the model by calculating the average squared difference in the
    predicted and actual values

    @param x: array of values of predictor variable of our model
    @param y: array of values of dependent variable corresponding to the values in x
    @param weights: array of slope and intercept of the line
    @return: the cost of the model
    """
    m = x.shape[0]  # total samples in the array

    y_hat = predict(x, weights)  # predicted values

    residual = y_hat - y  # difference in the actual and predicted values

    return np.sum(np.square(residual)) / (2 * m)


def train(x: np.array, y: np.array, iterations: int, learning_rate: float) -> list:
    """The function would calculate the gradients of the randomly initialized weight and bias
    and change them according to the gradient and the learning rate. This process is repeated
    <iterations> times, and return the trained weights. The aim is to reduce the cost of these
    parameters.

    :param x: array of values of predictor variable of our model
    :param y: array of values of dependent variable corresponding to the values in x
    :param iterations: number of times we want to train the model on our dataset
    :param learning_rate: the learning  rate of the model
    :return: list containing weights and cost_history
    """

    x = np.insert(x, 0, np.array([1]), axis=1)

    m = x.shape[0]  # total samples in the array

    weights = np.zeros((x.shape[1], 1))  # initialize weights

    cost_history = []  # will store cost after every epoch

    for _ in range(iterations):
        y_hat = predict(x, weights)  # predicted values

        residual = y_hat - y  # difference in the actual and predicted values

        gradient = np.dot(x.T, residual)

        weights -= (learning_rate / m) * gradient

        cost_history.append(cost(x, y, weights))

    return [weights, np.array(cost_history)]


def plot_statistics(x: np.array, y: np.array, weights: np.array, cost_history: np.array) -> None:
    """
    Plot the line and the data-points in one plot and cost on another plot

    @param x: array of values of predictor variable of our model
    @param y: array of values of dependent variable corresponding to the values in x
    @param weights: array of slope and intercept of line
    @param cost_history: array of costs of the model after each iteration of training the model
    """

    plt.figure(1)
    plt.scatter(x, y)

    xs = np.insert(x, 0, np.array([1]), axis=1)

    y_hat = np.dot(xs, weights)  # predicted values

    plt.plot(x, y_hat, color='r')

    plt.figure(2)
    plt.plot(range(cost_history.shape[0]), cost_history)

    plt.show()


def run_demo() -> None:
    """
    The function would run a demo training session on sample data
    :return: None
    """
    # generating data
    np.random.seed(0)
    x = np.random.rand(100, 1)
    y = 2 + 3 * x + np.random.rand(100, 1)

    # defining attributes to the train function
    iterations = 1000
    learning_rate = 0.05

    # train model
    weights, history = train(x, y, iterations, learning_rate)

    # plot graphs
    plot_statistics(x, y, weights, history)


if __name__ == "__main__":
    run_demo()
