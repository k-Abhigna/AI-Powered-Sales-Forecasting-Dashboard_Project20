import matplotlib.pyplot as plt

def plot_forecast(actual, predicted):

    plt.figure(figsize=(12,6))

    plt.plot(actual, label="Actual")

    plt.plot(predicted, label="Forecast")

    plt.legend()

    plt.show()
