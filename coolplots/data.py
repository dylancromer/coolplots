import matplotlib.pyplot as plt
import numpy as np

def plot1d(xdata, ydata, outfile=None, xdata_label=None, ydata_label=None, caption=None):
    plt.gcf().clear()
    with plt.xkcd():
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))

        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        plt.plot(xdata, ydata)

        plt.xlabel(xdata_label)
        plt.ylabel(ydata_label)
        fig.text(
            0.5, 0.05,
            caption,
            ha='center')

        fig.tight_layout()

        if outfile is not None:
            fig.savefig(outfile)

def dryrun_plot1d():
    xdata = np.linspace(0, 3, 100)
    ydata = np.exp(-xdata**2)
    plot1d(xdata, ydata, outfile='test.svg', xdata_label='time', ydata_label='power spectrum', caption='A cool plot')

def plotpoints1d(xdata, ydata, outfile=None, xdata_label=None, ydata_label=None, caption=None):
    plt.gcf().clear()
    with plt.xkcd():
        fig = plt.figure()
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))

        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        plt.scatter(xdata, ydata)

        plt.xlabel(xdata_label)
        plt.ylabel(ydata_label)
        fig.text(
            0.5, 0.05,
            caption,
            ha='center')
        fig.tight_layout()

        if outfile is not None:
            fig.savefig(outfile)

def dryrun_plotpoints1d():
    xdata = np.linspace(0, 3, 100)
    ydata = np.exp(-xdata**2) + np.random.rand(xdata.size)
    plotpoints(xdata, ydata, outfile='test.pdf', xdata_label='time', ydata_label='power spectrum', caption='A cool plot')

if __name__ == '__main__':
    print("This module is not meant to be run as a script")
