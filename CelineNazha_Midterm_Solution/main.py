Tabs = []
def validateChoice(choice):
  if choice.isnumeric() and (0 < int(choice) < 10):
    activateChoice(int(choice))
  else:
    print('Please enter a valid choice ')
    main()
    validateChoice(input())

def openTab():
  title = input('Enter the tab title : ')
  url = input('Enter the url tab  : ')
  Tabs.append({'title': title, 'url': url, 'nestedTabs': []})
  print(f"Tab '{title}' with URL '{url}' created successfully.")
  main()

def closeTab():
  print('the tab closed')

def switchTab():
  print('the tab switched')

def displayAllTabs():
  print('the tabs displayed')

def openNestedTabs():
  print('the nested tabs opened')

def clearAllTabs():
  print('all tabs cleared')

def saveTabs():
  print('the tabs saved')

def importTabs():
  print('the tabs imported')

def exit():
  print('the program exited')

def activateChoice(choice):
  if choice == 1:
    openTab()
  elif choice == 2:
    closeTab()
  elif choice == 3:
    switchTab()
  elif choice == 4:
    displayAllTabs()
  elif choice == 5:
    openNestedTabs()
  elif choice == 6:
    clearAllTabs()
  elif choice == 7:
    saveTabs()
  elif choice == 8:
    importTabs()
  elif choice == 9:
    print("Exiting program,Goodbye! ")
    exit()


def main():
  print("\n")
  print('1. Open Tab')
  print('2. Close Tab')
  print('3. Switch Tab')
  print('4. Display All Tabs')
  print('5. Open Nested Tab')
  print('6. Clear All Tabs')
  print('7. Save Tabs')
  print('8. Import Tabs')
  print('9. Exit')
  print("enter a choice :")
  validateChoice(input())



print('Hello, welcome to the program!')
main()

