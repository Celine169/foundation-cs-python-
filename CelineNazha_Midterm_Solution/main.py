import requests

Tabs = []
def validateChoice(choice):
  if choice.isnumeric() and (0 < int(choice) < 10):
    activateChoice(int(choice))
  else:
    print('Please enter a valid choice ')
    main()
    validateChoice(input())

def checkIndex(statement):
  index = input(statement)
  if not index:
    return len(Tabs) - 1
  elif index.isnumeric() and 0 <= int(index) < len(Tabs):
    return int(index)
  else:
    return checkIndex(statement)


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


def openTab():
  title = input('Enter the tab title : ')
  url = input('Enter the url tab  : ')
  Tabs.append({'title': title, 'url': url, 'nestedTabs': []})
  print(f"Tab '{title}' with URL '{url}' created successfully.")
  main()


def closeTab():
  if (len(Tabs) > 0):
    index = checkIndex('Enter the index of the tab to close: ')
    del Tabs[index]
    print(f"Tab '{index}' closed successfully.")
    main()
  else:
    print('There is no tab to close !')
    main()

def switchTab():
  def switchTab():
    if (len(Tabs) > 0):
      index = checkIndex('Enter the index of the tab you want to display: ')
      print('Title : ', Tabs[index]['title'])
      print('URL : ', Tabs[index]['url'])
      print('URL HTML Content:')
      print(requests.get(Tabs[index]['url']).text)
      main()
    else:
      print('There is no tab ')
      main()
    

def displayAllTabs():
  def displayAllTabs():
    if (len(Tabs) > 0):
      for index, tab in enumerate(Tabs):
        print('Tab ', index, ' : ', tab['title'])
        if (len(tab['nestedTabs']) > 0):
          for nestedTab in tab['nestedTabs']:
            print('**', nestedTab['title'])
      main()
    else:
      print('There is no tabs to display!')
      main()

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
