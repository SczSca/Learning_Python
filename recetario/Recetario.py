from os import system, name, makedirs, remove
from os.path import basename, isfile, isdir
from shutil import rmtree
from pathlib import Path

class Recetario:

    __menu_content = ("[0] - read recipes", "[1] - add recipes", "[2] - add category", "[3] - remove recipes", "[4] - remove category", "[5] - end program")
    __categories_directories = {
        "Carnes": {"Etrecot_al_Malbec", "Matambre_la_Pizza"}, 
        "Ensaladas": {"Ensalada_Griega","Ensalada_Mediterranea"}, 
        "Pastas": {"Canelones_de_espinaca", "Ravioles_de_Ricotta"},
        "Postres": {"Compota_de_Manzana", "Tarta_de_Frambuesa"}
        }

    def __init__(self, absolute_path):
        self.__absolute_path = absolute_path
        self.__recipes_path = Path(self.__absolute_path, "recipes")


    '''
        Clear terminal para limpiar la pantalla en sistemas operativos compatibles.
        :return: None
    '''
    def __clear_terminal(self):
        if name == 'nt':  # Windows
            system('cls')
        elif name == 'posix':  # Linux o macOS
            system('clear')
        else:
            print("Operative system not supported.")

    
    '''
        validates the option depending on the ammount of options available in the container
        :param option: str. the user's selected option ej: "0", "1", "2", "3"
        :param container: list. the options available ej: self.__categories_directories["Carnes"]
        :return: bool. True if valid, False otherwise
    '''
    def __validate_option(self, option, container):
        #result = bool(len(option) == 1 and option.isdigit() and (0 > int(option) < len(self.__categories_directories)))
        result = bool(option.isdigit() and (0 <= int(option) < len(container)))
        return result


    '''
        prints the return option depending on the options available
        :param length_container: str. the user's selected option
        :return: None
    '''
    def __print_back_option(self, length_container):
        print(f"[{length_container}] - Go back")


    '''
        prints the starting messages
        :return: None
    '''
    def __welcome(self):
        print("Welcome to the Recipe Manager!")
        print(f"the recipes are stored in the directory {basename(self.__absolute_path)}/recipes/ .")
        print(f"There are {self.__count_recipes()} recipes stored.")
        #TODO: Mostrar lista de recetas guardadas


    '''
        counts and prints all the recipes stored
        :return: int. number of recipes ej: 10
    '''
    def __count_recipes(self):
        i = 0
        '''for recipe in self.__recipes_path.glob("**/*.txt"):
            i += 1'''
        for recipes in self.__categories_directories.values():
            i += len(recipes)
        return i

    '''
        generates the categories and recipes predefined by the system
        :return: 1
    '''
    def __generate_recipes(self):
        #Generate recipes files in the directory recipes, based on the __categories_directories dictionary.
        makedirs(self.__recipes_path, exist_ok=True)

        for category, recipes in self.__categories_directories.items():
            category_path = self.__recipes_path / category
            
            if not category_path.exists():
                makedirs(category_path, exist_ok = True)

            for recipe in recipes:
                recipe_file = category_path / f"{recipe}.txt"

                if not recipe_file.exists():
                    with open(recipe_file, "w") as f:
                        f.write(f"This is a {recipe} recipe.\n")
        

        return 1

    '''
        stored all the recipes and categories inside self.__categories_directories each time the system is loaded
        :return: None
    '''
    def __load_recipes(self, path):
        for entry in path.iterdir():
            if entry.is_file() and entry.suffix == ".txt": 
                self.__categories_directories[entry.parent.name].add(entry.stem)
            elif entry.is_dir():
                self.__load_recipes(entry)


    '''
        prints the menu options stored in self.__menu_options
        :return: None
    '''
    def __print_menu(self):
        for menu_text in self.__menu_content:
            print(menu_text)


    '''
        prints all the categories saved in the self.__categories_directories and gets the answer from the user
        :return: str. name of the category selected by the user | "0" to let the system know that user wants to go back | "-1" if user write an unvalid option
    '''
    def __ask_category(self):
        return_val = ""
        categories = []

        for idx, category in enumerate(self.__categories_directories.keys()):
            categories.append(category)
            print(f"[{idx}] - {category}")


        length = str(len(self.__categories_directories.keys()))
        self.__print_back_option(length)
        answer = input("Please select a category by the number: ")

        if self.__validate_option(answer, self.__categories_directories): 
            return_val = categories[int(answer)]

        elif answer == length:
            return_val = "0"

        else:
            return_val = "-1"

        return return_val
        

    '''
        prints all the recipes stored in the self.__categories_directories[category] and gets the answer from the user
        :param category: str. name of the category ej: "Carnes"
        :return: str. name of the recipe selected by the user | "0" to let the system know that user wants to go back | "-1" if user write an unvalid option
    '''
    def __ask_recipe(self, category):
        return_val = ""
        recipes = []
        dict_category = self.__categories_directories[category]

        for idx, recipe in enumerate(dict_category):
            recipes.append(recipe)
            print(f"[{idx}] - {recipe}")

        length = str(len(dict_category))
        self.__print_back_option(length)

        answer = input("Please select a recipe by the number: ")

        if self.__validate_option(answer, dict_category):
            return_val = recipes[int(answer)]

        elif answer == length:
            return_val = "0"

        else:
            return_val = "-1"

        return return_val

    '''
    calls ask_category and ask_recipe methods to get the selected recipe from the user and prints its content
    :return: None
    '''
    def __read_recipes(self):
        category = ""
        recipe = ""
        back_flag = False
        while True: # get the category from the recipe list
            category = self.__ask_category()
            self.__clear_terminal()
            if category == "-1":
                print("Invalid option. Please try again.")
            elif category == "0":
                #back_flag = True
                #break
                return
            else:
                break
        
        # if back_flag:
        #     return
        
        while True: #get the recipe from the recipe list

            recipe = self.__ask_recipe(category)
            self.__clear_terminal()
            if recipe == "-1":                
                print("Invalid option. Please try again.")
            elif recipe == "0":
                back_flag = True
                break
            else:
                break

        if back_flag:
            return self.__read_recipes()

        recipe_path = self.__recipes_path / category / f"{recipe}.txt"
        self.__clear_terminal()
        print("")
        with open(recipe_path, "r") as f:
            for line in f.readlines():
                print(line.strip())
        print("")
        
    
    '''
        calls ask_category  method to get where the user wants to create the recipe file and lets the user to write line-by-line until they write 'exit'
        :return: None
    '''
    def __add_recipe(self):
        title = ""
        category = ""
        message = "Please try again"
        recipe_text = []

        while True: # loop to get the category
            category = self.__ask_category()
            if category == "-1":
                print("Invalid option. Please try again.")
            elif category == "0":
                return
            else:
                break

        new_path_recipe = self.__recipes_path / category 

        while True: # loop to get the title of the recipe
            err_msg = message
            title = input("Please enter the name of the recipe or write 'back' to choose another category: ")

            if title == "":
                err_msg = f"The title cannot be empty. {err_msg}"
            elif isfile(new_path_recipe / f"{title}.txt"):
                err_msg = f"The recipe already exists. {err_msg}"
            elif title == "back":
                return self.__add_recipe()
            else:
                break

            print(err_msg)

        new_path_recipe = new_path_recipe / f"{title}.txt"

        while True:
            line_text = input("Write your recipe line-by-line. Press enter to continue to the next line or if you want to skip a parragraph. If you want to stop, write 'exit': ")
            if line_text == "exit":
                print("Exit successfully")
                break

            recipe_text.append(line_text)
        
        print("Recipe creation in progress...")

        with open(new_path_recipe, "w") as file:
            for line in recipe_text:
                file.writelines(f"{line}\n")

        self.__categories_directories[category].add(title)
        print("recipe created successfully")


    '''
        asks the user the name of the category
        :return: None
    '''

    def __add_category(self):
        while True:
            category = input("Write the name of the category you want to add or write 'back' to return to the menu: ")
            if category == "back":
                return
            elif isdir(self.__recipes_path / category):
                print("The category already exists. Please try again.")      
            elif category == "":
                print("The category name cannot be empty. Please try again.")
            else:
                break
        
        new_path_category = self.__recipes_path / category
        makedirs(new_path_category, exist_ok=True)
        self.__categories_directories[category] = set()
        print(f"Category: {category} was created successfully")



    '''
    calls ask_category and ask_recipe methods to get the selected recipe from the user and deletes it
    :return: None
    '''
    def __remove_recipe(self):
        category = ""
        recipe = ""
        back_flag = False

        while True: # get the category from the recipe list
            self.__clear_terminal()
            category = self.__ask_category()
            if category == "-1":
                print("Invalid option. Please try again.")
                continue
            elif category == "0":

                return
            else:
                break 

        while True: #get the recipe from the recipe list
            self.__clear_terminal()
            recipe = self.__ask_recipe(category)
            if recipe == "-1":
                print("Invalid option. Please try again.")
                continue
            elif recipe == "0":
                back_flag = True
                break
            else:
                break

        if back_flag:
            return self.__remove_recipe()
        
        recipe_path = self.__recipes_path / category / f"{recipe}.txt"
        answer = input(f"Are you sure you want to delete {recipe}? You are going to lose all their recipes [y/n]: ")
        if answer == "y":
            if isfile(recipe_path):
                remove(recipe_path)
                self.__categories_directories[category].remove(recipe)
                message = f"{recipe} has been removed!"
            else:
                message = f"{recipe} does not exist!"
        elif answer == "n":
            message = f"{recipe} has not been removed!"
        else:
            message = "Invalid answer, please write 'y' or 'n'."
        print(message)
        
        
    '''
        calls ask_category method and asks the user if they are sure they want to delete the category and all its recipes
        :return: None
    '''

    def __remove_category(self):
        category = ""
        message = ""
        while True: # get the category from the recipe list
            self.__clear_terminal()
            category = self.__ask_category()
            if category == "-1":
                print("Invalid option. Please try again.")
                continue
            elif category == "0":

                return
            else:
                break 
        
        category_path = self.__recipes_path / category
        answer = input("Are you sure you want to delete this category? You are going to lose all their recipes [y/n]: ")
        if answer == "y":
            rmtree(category_path)
            self.__categories_directories.pop(category, None)
            message = f"{category} has been removed!"
        elif answer == "n":
            message = f"{category} has not been removed!"
        else:
            message = "Invalid answer, please write 'y' or 'n'."
        print(message)



    '''
        runs the application
        :return: None
    '''
    def start_manager(self):
        self.__clear_terminal()
        self.__generate_recipes()
        self.__load_recipes(self.__recipes_path)
        self.__welcome()
        
        while True:
            self.__print_menu()
            option = input("Please select an option: ")
            self.__clear_terminal()
            if not self.__validate_option(option, self.__menu_content):               
                print("Invalid option. Please try again.")
                continue
            if option == "0":
                self.__read_recipes()

            elif option == "1":
                self.__add_recipe()
                self.__clear_terminal()
            elif option == "2":
                self.__add_category()
                self.__clear_terminal()
            elif option == "3":
                self.__remove_recipe()
                self.__clear_terminal()
            elif option == "4":
                self.__remove_category()
                self.__clear_terminal()
            elif option == "5":
                break  # Exit the loop
            else:
                print("Invalid option. Please try again.")
                continue
            




