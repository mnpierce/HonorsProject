if __name__ == '__main__':

    from AreYouTheOne import *
    import matplotlib.pyplot as plt
    import numpy as np
    from statistics import mean,median

    # initialize list to store data
    data = list()

    # run simulation 100 times and add game length to data set
    for i in range(100):
        data.append(start_sim())

    # Create and display histogram
    plt.hist(data, range=(0,150), bins=150,label='Algorithm 3')
    plt.title('Algorithm Comparison\nFrequency of Game Length (100 trials)')
    plt.xlabel('Weeks')
    plt.ylabel('Frequency')
    plt.axvline(mean(data),color='k',linestyle='dashed',linewidth=1)
    min_ylim,max_ylim = plt.ylim()
    plt.text(mean(data)*1.2,max_ylim*.95,f'Mean: {mean(data)}')
    plt.legend(loc='upper right')
    plt.show()