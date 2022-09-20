colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

clothes = ['left shoe', 'right shoe', 'pants', 'belt', 'top', 'mask', 'cape']

def select(option):
  if option == 'q':
    return False
  return True

running = True

while running:
  selection = input(
    'Press Q to exit\n'
  )
  running = select(selection)