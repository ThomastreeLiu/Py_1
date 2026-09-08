import numpy

a1 = numpy.arange(10)
print(a1)
print(a1.shape)

a2 = numpy.arange(0, 10, 2)
print(a2)
print(a2.shape)

a3 = numpy.zeros(5)
print(a3)
print(a3.shape)

a4 = numpy.zeros((2,3))
print(a4.shape)

a5 = numpy.full((2, 3), 8)
print(a5)

r1 = numpy.array([9, 0, 2, 1, 0])
print(r1)

r2 = numpy.array([[9, 0, 1, 2, 0], [6, 7, 8, 9, 0]])
print(r2)

print(r1[0])
print(r2[0])
print(r2.shape)
print(r2[0, 2])
index1 = numpy.array([2, 4])
print(r1[index1])
