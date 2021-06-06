import numpy as np
class Vector2D:
    def __init__(self,x,y):
        self.data=np.array([x,y],dtype='int32')
    def set(self,x,y):
        self.data[0]=x
        self.data[1]=x
    def __and__(self, other):
        sum=self.data+other.data
        return Vector2D(sum[0],sum[1])
    def __sub__(self, other):
        sum = self.data - other.data
        return Vector2D(sum[0], sum[1])
    def __mul__(self, other):
        sum = self.data * other.data
        return Vector2D(sum[0], sum[1])
    def __divmod__(self, other):
        sum = self.data / other.data
        return Vector2D(sum[0], sum[1])
class Scalar:
    def __init__(self,value):
        self.value=value
    def set(self,value):
        self.value=value
    def __add__(self, other):
        return Scalar(self.value+other.value)
    def __sub__(self, other):
        return Scalar(self.value-other.value)
    def __divmod__(self, other):
        return Scalar(self.value/other.value)
    def __mul__(self, other):
        return Scalar(self.value*other.value)

class Transform:
    def __init__(self,translate:Vector2D,scale:Vector2D,rotate:Scalar):
        self.translate=translate
        self.scale=scale
        self.rotate=rotate