if __name__ == '__main__':

    # imports
    from AreYouTheOne1 import start_sim as sim1
    from AreYouTheOne2 import start_sim as sim2
    from AreYouTheOne3 import start_sim as sim3
    from AreYouTheOne4 import start_sim as sim4
    import matplotlib.pyplot as plt
    from statistics import mean,median
    # initialize list to store data
    data = list()
    # run simulation 500 times and add game length to data set
    for i in range(500):
        data.append(sim1())

    # initiialize data2
    data2 = list()
    # run simulation 500 times and add game length to data set
    for i in range(500):
        data2.append(sim2())

    # initialize data3
    data3 = list()
    # run simulation 500 times and add game length to data set
    for i in range(500):
        data3.append(sim3())

    # initialize data4
    data4 = list()
    # run simulation 500 times and add game length to data set
    for i in range(500):
        data4.append(sim4())

    # Create and display histogram
    plt.hist(data, range=(0,150), bins=150,label='Algorithm 1',alpha=.5,color="red")            # 1- Additional attributes for matching algorithm
    plt.hist(data2, range=(0,150), bins=150,label='Algorithm 2',alpha=.5,color="royalblue")     # 2- No added attributes, but full use of filtering bad matches (truth booth and special circumstances)
    plt.hist(data3, range=(0,150), bins=150,label='Algorithm 3',alpha=.5,color="orange")        # 3- Correct guesses are saved AND bad matches from truth booth are saved
    plt.hist(data4, range=(0,150), bins=150,label='Algorithm 4',alpha=.5,color="limegreen")     # 4- Correct guesses are saved for future guesses

    ### Mean indicators ###

    # Get y axis bounds
    min_ylim,max_ylim = plt.ylim()

    # Algorithm 1
    plt.axvline(mean(data),color='r',linestyle='dashed',linewidth=1)
    plt.text(mean(data)+1,max_ylim*.9,f'Mean\n {mean(data):.2f} ',size=10)
    plt.axvline(median(data),color='r',linestyle='dashed',linewidth=1)
    plt.text(median(data)-7,max_ylim*.9,f'Median\n  {median(data):.2f}  ',size=10)

    # Algorithm 2
    plt.axvline(mean(data2),color='b',linestyle='dashed',linewidth=1)
    plt.text(mean(data2)+1,max_ylim*.95,f'Mean\n{mean(data2):.2f}',size=10)
    plt.axvline(median(data2),color='b',linestyle='dashed',linewidth=1)
    plt.text(median(data2)-7,max_ylim*.95,f'Median\n {median(data2):.2f} ',size=10)

    # Algorithm 3
    plt.text(mean(data3)+1,max_ylim*.9,f'Mean\n{mean(data3):.2f}',size=10)
    plt.axvline(mean(data3),color='#FFA500',linestyle='dashed',linewidth=1)
    plt.axvline(median(data3),color='#FFA500',linestyle='dashed',linewidth=1)
    plt.text(median(data3)-7,max_ylim*.9,f'Median\n  {median(data3):.2f}  ',size=10)

    # Algorithm 4
    plt.axvline(mean(data4),color='g',linestyle='dashed',linewidth=1)
    plt.text(mean(data4)+1,max_ylim*.7,f'Mean\n{mean(data4):.2f}',size=10)
    plt.axvline(median(data4),color='g',linestyle='dashed',linewidth=1)
    plt.text(median(data4)-7,max_ylim*.7,f'Median\n  {median(data4):.2f}  ',size=10)


    # Title, axes, legend
    plt.title('Algorithm Comparison\nFrequency of Game Length (500 trials)')
    plt.xlabel('Weeks')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')

    # Display
    plt.show()
