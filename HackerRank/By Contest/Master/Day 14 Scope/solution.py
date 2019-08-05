	# Add your code here
    def computeDifference(self):
        e = sorted([abs(i) for i in self.__elements])
        self.maximumDifference = e[-1] - e[0]