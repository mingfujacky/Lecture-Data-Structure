def count_down_and_up(number):
    print(number, 'going down')
    if number == 0:
        # base case
        print('reached the base case')
        return
    else:
        # recursive case
        count_down_and_up(number - 1)
        print(number, 'going up')
        return
    
count_down_and_up(3)