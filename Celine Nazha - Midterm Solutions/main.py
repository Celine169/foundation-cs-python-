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