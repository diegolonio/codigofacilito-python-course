def show_message(message):
    message = message.title()
    def show():
        print(message)
    return show
new_function = show_message('Python 3 Course')
new_function()