# Do some research on python classes (I'd recommend starting here: https://www.geeksforgeeks.org/python-classes-and-objects/)
# Vector Class
# Create a class Vector that can be initialized with a list of numbers
# Implement a method to print a user-friendly string representation of the vector
# Overload the + operator to add two vectors of the same dimension (hint: Google 'dunder' methods!)
# Implement a method to calculate the dot product of two vectors
# Implement a method to calculate multiplication between a vector and a scalar (single number)

class Vector:
    def __init__(self, lst1, lst2, scalr):
        self.list1 = lst1
        self.list2 = lst2
        self.scalr = scalr

    def __str__(self):
        return f"these are the lists{self.list1}, {self.list2}"

    
    def __add__(self):
        newVector = []
        for i in range(len(self.list1)):
            if len(self.list1) == len(self.list2):
                newVector.append(self.list1[i] + self.list2[i])
            else:
                break
        return newVector
    def dot_product(self):
        result = 0
        for i in range(len(self.list1)):
            if len(self.list1) == len(self.list2):
                result += (self.list1[i] * self.list2[2])
        return result
    
    def vector_scalr(self):
        scalarVector = []
        for i in (self.list1):
            scalarVector.append(i * self.scalr)
        return scalarVector


    

groupOfLists = Vector([1,2,3,4,5,6,7,8,9], [3,6,8,9,12,45,67,56,70,], 4)


# print(groupOfLists)
print("type of the this output is:", groupOfLists.__str__())
print("sum of two vectors:", groupOfLists.__add__())
print("this the dot product:", groupOfLists.dot_product())
print("result of a scalar:", groupOfLists.vector_scalr())