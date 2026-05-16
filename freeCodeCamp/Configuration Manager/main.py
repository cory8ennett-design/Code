test_settings = {
    'theme': 'light',
    'color': 'black',
    'size': 'small'
}

def add_setting(dictionary, settings):
    key, val = settings

    if key.lower() in dictionary:
        return(f'Setting \'{key.lower()}\' already exists! Cannot add a new setting with this name.')
    else:
        dictionary[key.lower()] = val.lower()
        return(f'Setting \'{key.lower()}\' added with value \'{val.lower()}\' successfully!')

def update_setting(dictionary, settings):
    key, val = settings

    if key.lower() in dictionary:
        dictionary[key.lower()] = val.lower() 
        return(f'Setting \'{key.lower()}\' updated to \'{val.lower()}\' successfully!')
    else:
        return f'Setting \'{key.lower()}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(dictionary, key):

    if key.lower() in dictionary:
        del dictionary[key.lower()]
        return f'Setting \'{key.lower()}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(dictionary):
    if len(dictionary) == 0:
        return 'No settings available.'
    else:
        formatted_settings = 'Current User Settings:\n'

        for key, val in dictionary.items():
            formatted_settings += f'{key.capitalize()}: {val.lower()}\n'
        return formatted_settings

add_setting(test_settings, ('volume', 'high'))
add_setting(test_settings, ('THEME', 'dark'))
update_setting(test_settings, ('volume', 'high'))
delete_setting(test_settings, 'theme')
print(view_settings(test_settings))