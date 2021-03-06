###################################################################
#####   `         Add Recipe for KitchenWizard                #####
###################################################################
##### Version: 0.5                                            #####
##### Author:  Marcus R                                       #####
##### Tested:  ---                                            #####
#####                                                         #####
##### Purpose: The primary purpose of this mod is to add a    #####
#####          new recipe for a user                          #####
###################################################################

from packages.Log import kwlog
from packages.Items.addItem import __get_userid_from_key
from packages.Database import MySQL

def __create_recipe(recipe, userid):
    # Create recipe
    # Return: bool
    return MySQL.insert_recipe_for_user(userid, recipe)


def __add_items_to_recipe(items, rid):
    # Add items for recipe
    # Return: bool
    return MySQL.insert_items_to_recipe(rid, items)
def __check_args(recipe):
    for i in recipe:
        if i == "Error":
            return False
    for i in recipe[2]:
        for j in i:
            if j == "Error":
                return False

    return True
def add_recipe(session_key, recipe):
    # Adds a recipe for a user
    # Return string
    # recipe[] = [0:Name, 1:Discription, 2:[items], 3:image, 4:Prep Time, 5:Cook Time]
    # items[] = [gen_id, size]
    userid =  __get_userid_from_key(session_key)

    if userid == 'BAD_KEY':
        kwlog.log("Invaild session key")
        return "BAD_KEY"
    else:
        if (len(recipe[0]) > 0) and (len(recipe[1]) > 0) and (recipe[4] > 0) and (recipe[5] > 0):
            if not (__check_args(recipe)):
                return "INVAILD_FORMAT"
            if __create_recipe(recipe, userid):
                    return "COMPLETE"
            else:
                return "FAILED_TO_ADD_RECIPE"
        else:
            return "BAD_ARGUMENTS"
