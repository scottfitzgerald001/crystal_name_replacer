import json
import os

# Load in the names file for mapping
name_data = None
with open('trainer_names.json') as json_file:
    name_data = json.load(json_file)

# Uncomment any class you want to exlcude
exlcuded_classes = [
#  'SCIENTIST', 
#  'YOUNGSTER', 
#  'SCHOOLBOY', 
#  'BIRD_KEEPER', 
#  'LASS', 
#  'COOLTRAINERM', 
#  'COOLTRAINERF', 
#  'BEAUTY', 
#  'POKEMANIAC', 
#  'GENTLEMAN', 
#  'SKIER', 
#  'TEACHER', 
#  'BUG_CATCHER', 
#  'FISHER', 
#  'SWIMMERM', 
#  'SWIMMERF', 
#  'SAILOR', 
#  'SUPER_NERD', 
#  'GUITARIST', 
#  'HIKER', 
#  'BIKER', 
#  'BURGLAR', 
#  'FIREBREATHER', 
#  'JUGGLER', 
#  'BLACKBELT_T', 
#  'PSYCHIC_T', 
#  'PICNICKER', 
#  'CAMPER', 
#  'SAGE', 
#  'MEDIUM', 
#  'BOARDER', 
#  'POKEFANM', 
#  'KIMONO_GIRL', 
#  'POKEFANF', 
#  'OFFICER'
]

# build trainer list
trainer_list = []
for trainer_class in name_data:
  if trainer_class in exlcuded_classes:
    continue # skip this class if the trainer class is on the blacklist
  for trainer_name in name_data[trainer_class]:
    trainer_list.append(trainer_name)

# build input names list
input_names = None
with open('input_names.json') as json_file:
    input_names = json.load(json_file)

for name in input_names:
  if len(name) > 10:
    # Throw error if the name is too long
    # Worth noting that this may need more nuance, each trainer class seems
    # to have it's own length max limit
    raise ValueError(f"Input: ${name} is more than 10 characters!")

# sort each by length
input_names_sorted = sorted(input_names, key=len)
trainer_names_sorted = sorted(trainer_list, key=len)

name_mapping = {}
input_names_idx = 0
for trainer in trainer_names_sorted:
  if input_names_idx >= len(input_names):
    print("WARNING: There were more input names than trainer classes!")
    break # stop running if we have more input names than trainers

  curr_name = input_names_sorted[input_names_idx]
  name_mapping[trainer] = curr_name
  input_names_idx += 1

# Read in the trainer file
trainer_file_str = None
file_path = os.path.join('pokecrystal', 'data', 'trainers', 'parties.asm')
with open(file_path, 'r') as file:
    trainer_file_str = file.read()

# Map the names!
for trainer in name_mapping:
  print(f'Replaced: "{trainer}" with "{name_mapping[trainer]}"')
  if trainer_file_str.find(f'"{trainer}@"') == -1:
    raise ValueError(f"Could not map trainer: ${trainer}, have you reset the trainer.asm file back to it's original state?")
  trainer_file_str = trainer_file_str.replace(f'"{trainer}@"', f'"{name_mapping[trainer]}@"')

#print(trainer_file_str)

# overwrite the file with the new names!
file = open(file_path, 'w')
file.write(trainer_file_str)
file.close()
