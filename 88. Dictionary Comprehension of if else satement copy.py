print('-----1.Print Square Even Number -----')

square_even_numbers = {x**2:(x**3 if x % 2 == 0 else 'Odd') for x in range(1, 10)}
print(square_even_numbers)

print()

#============================================================================================================

div = {f'{x} is D By 3':x if x % 3 == 0 else f'{x} is D By 5' if x % 5 == 0 else x for x in range(1, 16)}
print(div)

print()