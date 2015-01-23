def main():
    
    array_list = []
    transformed_array = []
    count = int(input("Enter the number of elements you want to insert in an array:"))
    i = 0
    for i in range(count):
        num = (input("Enter a sorted array of numbers :"))
        array_list += int(num)
    print(array_list)
    
main()
