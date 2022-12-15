#1
print("Cutie, Cutie, little girl, \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a star in the sky. \nCutie, cutie, little girl,\n\t How I wonder what you are!")


#2
people = ['Jack','Jim']
Conversation = ["How are you today ?" , "I'm well Thank you and you?"]
print(people[0] , ":", Conversation[0] , "\n", people[1] , Conversation[1])

#3
square = 3**0.5
tri = 8**(1/3)
print('The squre root of 3.000 is {:.3f}'.format(square))
print('The triple root of 8.000 is {:.3f}'.format(tri))


#4
Temp = (100/5)*9+32
print("Temperature in 100 Celcius = {:.1f} Fahrenheit".format(Temp))


#5
tuple1 = ["Orange", (10, 20, 30), (5, 15, 25)]
print(tuple1[1][1])
print(tuple1[2][2])

#6
tuple1 = ('ab',78)
tuple2 = (99 , 'cd')
tuple1,tuple2 = tuple2,tuple1
print("From the original Tuple 1 = ('ab', 78 ) \n\t and Tuple2 = (99, 'cd') \nThe newly swapped tuples are:")
print("Tuple 1 =",tuple1)
print("Tuple 2=",tuple2)

#7
sample_dict = {
 'emp1': {'name': 'Jhon', 'salary': 7500},
 'emp2': {'name': 'Emma', 'salary': 8000},
 'emp3': {'name': 'Brad', 'salary': 6500}
}
sample_dict['emp2']['salary'] = 10000
print(sample_dict)
