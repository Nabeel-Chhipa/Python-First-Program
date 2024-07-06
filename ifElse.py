# num = input('Enter a number: ')
# num = int(num)
# if num % 2 == 0:
#     print('Number is Even')
# else:
#     print('Number is Odd')

pakistaniCuisine = ['Karrahi', 'Biryani', 'Haleem']
italianCuisine = ['Pizza', 'Pasta', 'risotto']
cuisine = input('Enter a cuisine name: ')
if cuisine in pakistaniCuisine:
    print(cuisine + ' is a Pakistani cuisine')
elif cuisine in italianCuisine:
    print(cuisine + ' is a Italian cuisine')
else:
    print("I don't know which cuisine is " + cuisine)