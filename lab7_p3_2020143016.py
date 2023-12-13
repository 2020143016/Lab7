

from unittest import result


class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        for i in range(len(arr)):
            if type(arr[i]) != list:
                raise  not2DError()
            else:
                if len(arr[0]) != len(arr[i]):
                    raise unevenListError()
        self.extend(arr)

    def __str__(self):

        return "list_2D: "+ str(len(self)) +"*"+ str(len(self[0]))

        

    def transpose(self):
        lstToreturn = []
        for k in range(len(self[0])):
            lst = []
            for i in range(len(self)):
                lst.append(self[i][k])
            lstToreturn.append(lst)
        self = list_D2(lstToreturn)
        return self


    def __matmul__(self, others):
        
        if len(self[0]) != len(others):
            raise improperMatrixError()
        result = []
        for selfRow in self:
        # B의 각 열에 대해 반복하여 내적 계산
            result_row = []
            for selfCol in zip(*others):
                dot_product = sum(a * b for a, b in zip(selfRow, selfCol))
                result_row.append(dot_product)

            result.append(result_row)

        
        self = list_D2(result)
        return self
        ######

    def avg(self):
        avg = 0
        for i in range(len(self)):
            for k in range(len(self[0])):
                avg = avg + self[i][k]
        avg = avg/(len(self)*len(self[0]))
        return avg
