### Simulation for visulization of linear combinations and Vector Span.

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
