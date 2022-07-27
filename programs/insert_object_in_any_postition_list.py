# Python program to insert a number to any position in a list

def insert_number_in_any_position(index_position, number_to_be_inserted):
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_numbers)

    new_list = list_numbers.insert(index_position, number_to_be_inserted)

    print(list_numbers)


insert_number_in_any_position(5, 433)
