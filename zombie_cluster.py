class model:
    mlist = []
    mlists = []
    def __init__(self, matrix):
        for i in range (0,len(matrix)):
            self.mlists.append([i])
    def get_cluster_of(self,i):
        for list in self.mlists:
            if i in list:
                return list
    def get_cluster_number(self):
        return len(self.mlists)
    def extend_cluster(self,i,j):
        for list in self.mlists:
            if j in list:
                if (model.get_cluster_of(model,i) != list):
                    self.mlists.remove(list)
                    model.get_cluster_of(model, i).extend(list)
                return
        model.get_cluster_of(self,i).extend([j])
    def solve(self,matrix):
        n=len(matrix)
        self.__init__(self,matrix)
        for i in range(0, n):
            for j in range(i + 1, n):
                if matrix[i][j] == 1:
                    self.extend_cluster(self,i,j)
        print(self.mlists)
        print (self.get_cluster_number(self))

matrix=[[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]

model.solve(model,matrix)
