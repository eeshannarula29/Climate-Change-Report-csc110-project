"""
This file will act as a library to train a liner model
to our data for future predictions.

Resources:
- https://towardsdatascience.com/linear-regression-using-python-b136c91bf0a2
- https://matplotlib.org/devdocs/contents.html
"""

import matplotlib.pyplot as plt
from random import uniform
from typing import List

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


def predict(x: float, weight: float, bias: float) -> float:
    """Returns the prediction made by the line, by passing
    in the value of x in equation y = theta_1*x + theta_0"""
    return weight * x + bias


# step1: initialize weights and biases randomly
def initialize_parameters(minimum, maximum) -> List[float]:
    """Returns list of two randomly generate numbers
    in range <min> to <max>

    @param minimum: the least value the numbers in the return list can take
    @param maximum: the maximum value the numbers in the return list can take
    """
    return [uniform(minimum, maximum), uniform(minimum, maximum)]


# step2: compute the cost of our weight and bias
def compute_cost(xs: List[float], ys: List[float], weight: float, bias: float) -> float:
    """
    Return the cost of the model by calculating the average squared difference in the
    predicted and actual values

    :param xs: list of values of predictor variable of our model
    :param ys: list of values of dependent variable corresponding to the values in xs
    :param weight: the slope of the model or line
    :param bias: the intercept of the model or line
    :return: the cost of the model
    """

    # compute the average squared difference in the predicted and actual values
    sq_avg = sum(pow(predict(xs[i], weight, bias) - ys[i], 2) for i in range(len(xs))) / len(xs)

    # we return our answer divided by 2 because of computational purposes
    return sq_avg / 2


# step3 and step 4: compute the gradient which would be used to modify theta_1 and theta_0
def compute_gradients(xs: List[float], ys: List[float], weight: float, bias: float) -> \
        List[float]:
    """ Return the delta weight and bias, with which we can change our current
    weight and bias to lower the cost function and increase the accuracy of our
    prediction. These deltas are called gradients and are calculated by computing
    the partial derivative of the cost function with respect to the weight and bias.

    :param xs: list of values of predictor variable of our model
    :param ys: list of values of dependent variable corresponding to the values in xs
    :param weight: weight: the slope of the model or line
    :param bias: bias: the intercept of the model or line
    :return: gradients for weight and bias of the line
    """

    d_bias = sum([(predict(xs[i], weight, bias) - ys[i])
                  for i in range(len(xs))]) / len(xs)

    d_weight = sum([(predict(xs[i], weight, bias) - ys[i]) * xs[i]
                    for i in range(len(xs))]) / len(xs)

    return [d_weight, d_bias]


# step4: Repeat step 2 to 4, and train our model
def train(xs: List[float], ys: List[float], epochs: int, alpha: float, minmax: List[int]) -> list:
    """The function would calculate the gradients of the randomly initialized weight and bias
    and change them according to the gradient and the learning rate. This process is repeated
    <epochs> times, and return the trained weights. The aim is to reduce the cost of these
    parameters.

    :param xs: list of values of predictor variable of our model
    :param ys: list of values of dependent variable corresponding to the values in xs
    :param epochs: The number of times we want to train our model
    :param alpha: the learning rate with which we want to learn
    :param minmax: list containing the range of random initial weight and bias: [min, max]
    :return: The weight and bias of the trained model, and a list of cost after every epoch
    """

    # step 1: initialize weights and biases randomly
    weight, bias = initialize_parameters(minmax[0], minmax[1])

    # step 2 to 4
    history = []  # contain the cost of the function after every epoch

    for _ in range(epochs):
        # computing the gradients to modify parameters
        gradients = compute_gradients(xs, ys, weight, bias)

        # modifying parameters
        weight = weight - alpha * gradients[0]
        bias = bias - alpha * gradients[1]

        # cost of the model
        cost = compute_cost(xs, ys, weight, bias)

        history.append(cost)

    return [weight, bias, history]


def plot_statistics(xs: List[float], ys: List[float], weight: float, bias: float, history: List[float]) -> None:
    """
    Plot the line and the data-points in one plot and cost on another plot

    :param xs: list of values of predictor variable of our model
    :param ys: list of values of dependent variable corresponding to the values in xs
    :param weight: weight of the model
    :param bias: bias of the model
    :param history: list of cost per epoch
    :return: None
    """

    fig, axs = plt.subplots(2)

    # plot the data points and line
    axs[0].scatter(xs, ys)
    axs[0].xlabel('x')
    axs[0].ylabel('y')

    predicted_values = [predict(i, weight, bias) for i in xs]

    axs[0].plot(xs, predicted_values, color='r')

    # plot the cost function with epochs
    axs[1].plot(list(range(len(history))), history)

    plt.show()
