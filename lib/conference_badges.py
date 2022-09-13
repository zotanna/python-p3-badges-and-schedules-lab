def badge_maker(name):
  return f"Hello, my name is {name}."

def batch_badge_creator(names):
  messages = []
  for name in names:
    messages.append(badge_maker(name))
  return messages

def assign_rooms(names):
  rooms = []
  for index, name in enumerate(names):
    rooms.append(f"Hello, {name}! You'll be assigned to room {index+1}!")
  return rooms

def printer(names):
  for badge in batch_badge_creator(names):
    print(badge)
  for assignment in assign_rooms(names):
    print(assignment)
