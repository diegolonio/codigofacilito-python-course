'''With nonlocal we can change the value of
a local variable in a nested function'''
def start_play_list(my_list):
    def play():
        nonlocal my_list
        my_list = [1, 2, 3]
        for value in my_list:
            print(value)
    play()
    print(my_list)
my_list = ['track 1', 'track 2', 'track 3', 'track 4']
start_play_list(my_list)