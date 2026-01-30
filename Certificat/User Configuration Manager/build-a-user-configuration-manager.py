# ----start of main.py---- 

def add_setting(settings:dict, mytuple:tuple):
    key, value = mytuple
    key = key.lower()
    value = value.lower()
    if key in set(settings.keys()):
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value    
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings:dict, mytuple:tuple):
    key, value = mytuple
    key = key.lower()
    value = value.lower()
    if key in set(settings.keys()):
        settings.update([(key, value)])
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings:dict, key:str):
    key = key.lower()
    if key in set(settings.keys()):
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"    
    return f"Setting not found!"
    
def view_settings(settings:dict):
    if not len(settings):
        return 'No settings available.'   
    output = 'Current User Settings:\n'
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    return output

test_settings = {'Theme': 'dark',
'Notifications': 'enabled',
'Volume': 'high'}

test_settings_2 = {'theme': 'light'}
print(update_setting(test_settings_2, ('theme', 'dark')))
print(view_settings(test_settings))

# -----end of main.py-----

