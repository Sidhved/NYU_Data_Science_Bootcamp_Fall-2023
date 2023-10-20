# Numpy Practice Questions

1. Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.
2. Find common elements between A and B. [Hint : Intersection of two sets]
3. Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]
4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
	'''
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
	    iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
    '''
