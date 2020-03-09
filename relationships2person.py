from variable import color, name_var_dict
from database import get_database
from random import shuffle
from speech import speak

data = get_database('family.db','family_info',('rowid','name','gender','relation','image'))


shuffle(data)

person = data[0]

print(person)
speak(f"""This is {person['name']}
How is {'he' if person['gender'] == 'boy' else 'she'} related to you"
""")
# speak(f"How is {'he' if person['gender'] == 'boy' else 'she'} related to you")
