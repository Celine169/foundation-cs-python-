import json
import requests
import validators

Tabs = []
#this function validate the choice if it is valid or not
def validateChoice(choice):
  if choice.isnumeric() and (0 < int(choice) < 10):
    activateChoice(int(choice))
  else:
    print('Please enter a valid choice ')
    main()
    validateChoice(input())
#thisfunction checks if the file path is valid or not
def getValidPath(statement):
      path = input(statement)
      if path and path.endswith('.json'):
        return path
      else:
        return getValidPath(statement)
#this function checks if the index entered by user is less than the len(tabs) and if it is numeric
def checkIndex(statement):
  index = input(statement)
  if not index:
    return len(Tabs) - 1
  elif index.isnumeric() and 0 <= int(index) < len(Tabs):
    return int(index)
  else:
    return checkIndex(statement)
#this function checks the validation of an url entered by user
def checkUrl(statement):
  url = input(statement)
  if validators.url(url):
    return url
  else:
    return checkUrl(statement)
#this function prompts the user for the title and the url of the tab he wants to open
def openTab():
  title = input('Enter the tab title : ')
  url = checkUrl('Enter the url tab  : ')
  Tabs.append({'title': title, 'url': url, 'nestedTabs': []})
  print(f"Tab '{title}' with URL '{url}' created successfully.")
  main()
#this function prompts the user to enter the index of the tab to closes
def closeTab():
  if (len(Tabs) > 0):
    index = checkIndex('Enter the index of the tab to close: ')
    del Tabs[index]
    print(f"Tab '{index}' closed successfully.")
    main()
  else:
    print('There is no tab to close !')
    main()

#this function prompts the user to enter an index of a tab to display its html content
def switchTab():
  if (len(Tabs) > 0):
    index = checkIndex(
        'Enter the index of the tab you want to display: ')
    print('Title : ', Tabs[index]['title'])
    print('URL : ', Tabs[index]['url'])
    print('URL HTML Content:')
    print(requests.get(Tabs[index]['url']).text)
    main()
  else:
    print('There is no tab ')
    main()
# this function prompts the user to enter the index of a tab to display its title and the title otss nested tab if exist
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
#this function prompts the user to enter an index of a tab to input a title and url of a nested tab at that index
def openNestedTabs():
    index = checkIndex('Enter the index of the tab to open nested tabs: ')
    title = input('Enter the tab title : ')
    url = checkUrl('Enter the url tab : ')
    Tabs[index]['nestedTabs'].append({'title': title, 'url': url})
    print(
        f"Tab '{title}' with URL '{url}' created under the parent tab with index  '{index}' successfully."
    )
    main()

def clearAllTabs():
  Tabs.clear()
  print('All the tabs are cleared!')
  main()

def saveTabs():
  filePath = getValidPath('Enter the file path to save the tabs: ')
  with open(filePath, 'w') as file:
    json.dump(Tabs, file)
  print('The tabs are saved successfully!')
  main()

def importTabs():
  filePath = input('Enter the file path to import the tabs: ')
  with open(filePath, 'r') as file:
    Tabs.clear()
    Tabs.extend(json.load(file))
  print('The tabs are imported successfully!')
  main()

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