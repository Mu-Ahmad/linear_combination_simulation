import numpy as np
from time import sleep
import matplotlib.pyplot as plt

# 'bmh' 'seaborn-poster' 'seaborn-dark' '_classic_test' 'Solarize_Light2' 'seaborn-dark' 'dark_background' 'classic'
plt.style.use('bmh')
Gcolor = 'black'  # colour of the linear combination plotted


class plotLinearCombinations:

    '''
    This Class takes list of vectors and weights(optional), calculate and plot 'count' number of linear combinations
        ----------
        Parameters
        ----------
        **Kwags

        vectors   : list
            list of vectors

        weights   : list |default==random|
            list of weights

        count     : int  |default==10|
            No. of linear combinations to plot
            |~count<=1 to plot only linear combination with given weights only|

        origin    : list |default==(0,0)|
            coordinates of origin point for the plot

        pointOnly : Bool |default == False|
            weather to plot points or vectors

        dynamic   : Bool |default==False|
            to enable dynamic plotting

        printInfo : Bool |default==True|
            to print details of each linear combination

        -------
        Attributes
        -------
        purpose:
            To store the parameters

        meaning:
            Self Explanatory

        -------
        Behaviours
        -------
        _findLinearComb:
            return:
                calculated linear combination

        _randomWeights:
            populates the 'weights' attribute with random weights in accordance with no. of vectors

        _plotLine:
            plot the vector(s)

        findPlotlinearcomb:
            Loops through list of vector and calculates 'count' no of linear combinations
            with random weights and plot them. This function incorporates all of the above described
            private functions

        ------
        Raises
        ------
        ValueError
            unequal number of vectors and weights supplied!

        ------
        Signature
        ------
        plotLinearCombinations(vectors, weights=False, count=10, origin=(
            0, 0), pointOnly=False, dynamic=False, printInfo=False)
        '''

    def __init__(self, vectors, weights=False, count=10, origin=(0, 0), pointOnly=False, dynamic=False, printInfo=False):
        self.vectors = np.array(vectors, dtype='float64')
        if not weights:
            self.weights = np.array([1 for vector in vectors])
        else:
            self.weights = np.array(weights)
        self.count = count
        self.printInfo = printInfo
        self.resultant = []
        self.pointOnly = pointOnly
        self.origin = origin
        self.dynamic = dynamic

        if len(vectors) != len(self.weights):
            raise ValueError

    def _findLinearComb(self):
        resultant = self.vectors[0]*0
        for vector, weight in zip(self.vectors, self.weights):
            resultant += vector*weight
        return resultant

    def _randomWeights(self):
        self.weights = np.random.randint(-6, 6,
                                         size=len(self.weights))*np.random.rand()

    def _plot(self):
        plt.grid()
        plt.title(
            f'Linear Combinations Visualization\nCount : "{max(self.count, 1)}"')
        origin = self.origin
        xCords = np.array([vectors[0] for vectors in self.resultant])
        yCords = np.array([vectors[1] for vectors in self.resultant])
        xCord = np.array([vectors[0] for vectors in self.vectors])
        yCord = np.array([vectors[1] for vectors in self.vectors])
        colorArray = ['r', 'b', 'g', 'y', 'grey',
                      'orange', 'silver', 'purple', 'pink']
        if not self.pointOnly:
            plt.quiver(*origin, xCords, yCords, angles='xy',
                       scale_units='xy', color=Gcolor, scale=1)
            plt.xlim(min(min(xCords)+self.origin[0], min(xCord)+self.origin[0], self.origin[0])-1,
                     max(max(xCords)+self.origin[0], max(xCord)+self.origin[0], self.origin[0])+1)
            # plt.xlim(-40, 40) #for semi dynamic mode
            plt.ylim(min(min(yCords)+self.origin[1], min(yCord)+self.origin[1], self.origin[1])-1,
                     max(max(yCords)+self.origin[1], max(yCord)+self.origin[1], self.origin[1])+1)
            #plt.ylim(-40, 40)
        else:
            plt.plot(xCords, yCords, 'D', color='white', markerfacecolor='white',
                     markeredgecolor='black', markeredgewidth=1)  # temp
        plt.quiver(*origin, xCord, yCord, color=colorArray,
                   angles='xy', scale_units='xy', scale=1)
        if self.dynamic:
            plt.pause(0.1)
        else:
            plt.show()

    def findPlotlinearcomb(self):
        self.resultant *= 0
        result = self._findLinearComb()
        self.resultant.append(result)
        if self.printInfo:
            print('Linear combination: {} of \n{} \nwith weights {}\n'.format(
                self.resultant[-1], self.vectors, self.weights))
        count = self.count
        if self.dynamic:
            self._plot()
        while count > 1:
            self._randomWeights()
            result = self._findLinearComb()
            self.resultant.append(result)
            if self.printInfo:
                print('Linear combination: {} of \n{} \nwith weights {}\n'.format(
                    self.resultant[-1], self.vectors, self.weights))
            count -= 1
            if self.dynamic:
                self._plot()
            self._randomWeights()
        if self.dynamic:
            plt.grid()
            plt.show()
        else:
            plt.grid()
            self._plot()


try:
    p = plotLinearCombinations(vectors=[
        [6, 3], [-3, 5]], weights=[2, 3], count=90000000, origin=[-5, 10], pointOnly=False, printInfo=False, dynamic=False)
    p.findPlotlinearcomb()
    # p._plot()
except Exception as e:
    print(e)
    print('unequal number of vectors and weights supplied!')


# p = plotLinearCombinations(vectors=[
#     [12, 6], [13, -5]], weights=[2, -1], count=15, origin=[0, 0], pointOnly=False, dynamic=True, printInfo=False)
# p.findPlotlinearcomb()
