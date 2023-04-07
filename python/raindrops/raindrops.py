def convert(number):
    d = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    return ''.join(value for key, value in d.items()
                   if number % key == 0) or str(number)
