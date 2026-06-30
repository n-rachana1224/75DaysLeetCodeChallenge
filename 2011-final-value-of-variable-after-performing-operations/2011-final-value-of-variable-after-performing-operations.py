class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        for i in range(len(operations)):
            if "++" in operations[i]:
                X=X+1
            else:
                X=X-1

        return X
        