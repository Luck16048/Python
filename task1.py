def create_array(size):
    array = []
    for i in range(size):
        num = int(input(f'Wprowadź liczbę całkowitą {i + 1}: '))
        array.append(num)
    return array

def find_max_min(array):
    return max(array), min(array)

def reverse_array(array):
    return array[::-1]

def main():
    size = int(input("Podaj rozmiar tablicy: "))
    array = create_array(size)
    max_num, min_num = find_max_min(array)
    reversed_array = reverse_array(array)
    
    print(f'Największa liczba: {max_num}')
    print(f'Najmniejsza liczba: {min_num}')
    print(f'Odwrócona tablica: {reversed_array}')

if __name__ == "__main__":
    main()
