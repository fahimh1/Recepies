import os, shutil
from pathlib import Path
from os import system
my_dir =Path('C:/Users/Fahim/Documents/udemypy/day 6 files and folders/Recipes/Recipes')
#
#
# for txt in Path(my_dir).glob('**/*.txt'):
#     print(txt)


def choose_category():
    valid_category = [i for i in os.listdir(my_dir)]
    # it is a list of all the categories that are in the directory
    valid_check = [i.lower() for i in valid_category]
    # is same list as before but with all entities in lower case to compare to user input
    #print(valid_category)
    user_choice = ''
    while user_choice not in valid_check:
        user_choice = input('By typing the name please choose a category  ' + ', '.join(valid_category) + ' ').lower()
        # takes the user input
        if user_choice in valid_check:
            category_index = (valid_check.index(user_choice))
            # compares the input to the available categories in the list a return the index of the item
            file_paths = list((Path(my_dir/valid_check[category_index]).glob('*.txt')))
            # is a list of all the file paths in the directory
            file_dir = Path(my_dir/valid_check[category_index])
            #is a file path of the selected category directory
            file_names = [i.name for i in file_paths]
            # is a list of all the files names in the chosen directory
            #print(file_paths)
            return file_names, file_paths, file_dir
        else:
            print('Input is not recognised. Please try again ')

# The function above asks the user to choose an option from the provided categories.
# The user inputs their choice, it is compared to the valid_categories (existing directories).
# The file path of the directory as well as the names and files paths of the files located in the directory are returned.


def choose_recipes(category,file_paths):
    #print(category)
    user_recipe = ''
    valid_recipes = [items.lower().strip('.txt') for items in category]
    # is a list of recipes that exists in the file path given
    #print(valid_recipes)
    while user_recipe not in valid_recipes:
        if len(valid_recipes) < 1:
            print('No recipes for this category :( ')
            break
        # if there are no recipes in the directory it outputs a message and breaks the loop.
        user_recipe = input('Enter a recipe from the following recipes -------> ' + ', '.join(items.strip('.txt')
                                                                                             for items in
                                                                                             category) + '.\n').lower()
        if len(valid_recipes) < 1:
            break
        # takes the user input for the recipes and also displays the all recipes in the directory
        if user_recipe in valid_recipes:
            # checks if the user's input is valid (is and actual file in the directory)
            recipe_index = valid_recipes.index(user_recipe)
            # gets the correct index from the valid list for the users input
            system("cls")
            #clears the terminal
            print(file_paths[recipe_index].read_text())
            # using the index attained the correct file path is obtained from the list
            # and displays the contents of the chosen txt file
            return file_paths[recipe_index]
        else:
            print('Recipe not found. please try again '.upper())

# The function above takes the users choice of recipe (.txt file).
# The function takes the argument of category (which is the chosen directory) and file_paths (which is the
# file path of the chosen directory). It then aks the user to choose a recipe from the displayed options and checks
# if it is in the directory if not it then asks the user to try again. If the user input is valid it then gets the
# file path from a list and then displays the contents of the txt file.


def new_recipe(file_dir):
    os.chdir(file_dir)
    # changes the directory to the chosen directory
    recipe_name = input('Enter the name of you new recipe ')
    recipe_content = input('Enter the new recipe ')
    # asks the user to input the name of th new recipe and the contents of it
    with open(f'{recipe_name}.txt','w' ) as file:
        file.writelines(recipe_content)
    # writes the user input to the file

# The function above creates a new recipe (.txt file) in the chosen directory
# The function takes an argument of 'file_dir' which is a file path of the user chosen directory obtained from
# another function. The function creates a new recipe in a chosen directory.
# Firstly the directory is changed to the correct one, the user is then asked to input the name of the file and then
# the content of the file which is then written to the file and the file the is added to the directory.

def new_category():
    all_categories = [i for i in os.listdir(my_dir)]
    print('These are the current categories ' + ','.join(all_categories) + '\n')
    os.chdir(my_dir)
    new_user_category = input("Enter the name of the new category ")
    os.makedirs(new_user_category)

# The function above created a new category(directory).
# It First displays the current categories and asks the user to input a new one, which is then created

def remove_category(file_dir):
    shutil.rmtree(file_dir)
    all_categories = [i for i in os.listdir(my_dir)]
    print('You have delete the category, the remaining categories are as follows -------> '+','.join(all_categories)+'\n')

# The function above removes a category(directory)
# It displays the categories the exists and asks the user to pick one to delete, all the files in the directory are
# also deleted.


def remove_file(file):
    if file is None:
        system("cls")
        print ('This directory is empty no files to delete')
    # If there are no recipes in the chosen directory

    else:
        system("cls")
        print('you have deleted the file ' + file.name)
        os.remove(file)

# This function deletes a recipe(.txt file)
# The user choose a file from the choose_recipe function, it is passed through to this function and deleted the file



#category, file_paths, file_dir = choose_category()

#file = choose_recipes(category, file_paths)

#new_recipe(file_dir)

#new_category()

#remove_category(file_dir)

#remove_file(file)






#####################################################################################################################
##################################**************** MAIN **********************#######################################
#####################################################################################################################

# The first while loop compares the user input to a string if they both match the program is terminated.
# If not the user has to enter a 1,2,3,4 or 5 for to choose the options displayed
# The functions are then called to the corresponding user choice
user = ''

while user.upper() != 'EXIT':
    user = input('''Welcome, please enter 1,2,3,4 or 5 for the following options Do you want to
    \n[1] - View a category/recipe
    \n[2] - Create a new recipe
    \n[3] - Delete a recipe
    \n[4] - Create a new category
    \n[5] - Delete a category
    \nOr if you want to exit the program exit the program type EXIT ''')

    if user == str(1) or user == str(2) or user == str(3):
        system('cls')
        category, file_paths, file_dir = choose_category()
        user = input('''Do you want to
        \n[1] - Do you want to view a recipe
        \n[2] - Create a new recipe
        \n[3] - Delete a recipe
        \nor type back to go the the main menu\n''')

        while user != str(1) or str(2) or str(3) or 'back':
            if user == str(1):
                file = choose_recipes(category,file_paths)
                input('Press any key to return to the main menu ')
                system('cls')
                break
            elif user == str(2):
                new_recipe(file_dir)
                input('Press any key to return to the main menu ')
                system('cls')
                break
            elif user == str(3):
                file = choose_recipes(category, file_paths)
                remove_file(file)
                input('Press any key to return to the main menu ')
                system('cls')
                break
            elif str(user).lower() == 'back':
                system('cls')
                break
            else:
                system('cls')
                print(user)
                user = input(
                    'Do you want to \n1)Do you want to view a recipe\n 2)Create a new recipe\n 3)Delete a recipe'
                    'or type back to go the the main menu\n')

    elif user == str(4):
        system('cls')
        new_category()
        input('Press any key to return to the main menu ')
        system('cls')


    elif user == str(5):
        system('cls')
        category, file_paths, file_dir = choose_category()
        remove_category(file_dir)
        input('Press any key to return to the main menu ')
        system('cls')


    elif str(user).upper() == 'EXIT':
        system('cls')
        print('Ok Bye Bye')
        exit()
    else:
        system('cls')
        print(user)
        print('**************************INPUT NOT RECOGNISED************************************\n ')









































































# while is_valid == False:
#     user_choice = input('By typing the name please choose a category Meat, Salad, Dessert, Pasta ').lower()
#     if user_choice == 'meat':
#         file_paths = list((Path(my_dir/'Meat').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     elif user_choice == 'salad':
#         file_paths = list((Path(my_dir / 'Salad').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     elif user_choice == 'dessert':
#         file_paths = list((Path(my_dir / 'Dessert').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     elif user_choice == 'pasta':
#         file_paths = list((Path(my_dir / 'Pasta').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     else:
#         print('Input is not recognised. please try again ')
















