import numpy

a = numpy.array([2,3])
b = numpy.array([4, 2])

c = numpy.zeros(2)
c[0] = a[0] + b[0]
c[1] = a[1] + b[1]

c_1 = a + b
c_2 = a - b
c_3 = a * b
c_4 = a / b

print(c_1, c_2, c_3, c_4)

height = numpy.array([1.5, 1.7, 1.9])
weight = numpy.array([57, 93, 85])
bmi = weight / height**2

print(bmi)
print(numpy.trunc(bmi))



height = numpy.random.random(10)
height = height * 0.3
height = height + 1.5

weight = numpy.random.random(10)
weight = weight * 20
weight = weight + 45
print(height, weight)
