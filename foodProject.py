import json
import requests


def save_to_file(filename,data):
    with open(filename,"w") as write_file:
        json.dump(data,write_file,indent = 2)


def read_from_file(filename):
    with open(filename, "r") as read_file:
        jsonData = json.load(read_file)
        return jsonData


# getting the api key and id
my_yum_api_key_json = read_from_file("api_key.json")
my_yum_api_key = my_yum_api_key_json["yum_api_key"]


# Performing the Search API request



#this method will return the json file of the search method
def getAllReipe(userInput):
    newParamater = userInput.replace(" ", "+")
    newParamater = "&q=" + newParamater

    url = "http://api.yummly.com/v1/api/recipes?_app_id="
    url_yum = url + my_yum_api_key + newParamater + "&requirePictures=true"

    yum_json = requests.get(url_yum).json()
    yum_json_file_name = "yumSearch.json"
    save_to_file(yum_json_file_name, yum_json)
    return yum_json


#will recieve the yum_json json file and return a list of all Recipes
def getRecepieList(yum_json):
    recepies = []

    for i in range(0,len(yum_json["matches"])):
        case = {"recipeName":getRecipeName(yum_json,i),"recipeCookTime":getRecipeCookTime(yum_json,i),
                "imageUrl":getImageUrl(yum_json,i),"ingredients":getIngredients(yum_json,i),
                "recipeLink":getRecipeLink(yum_json,i)}
        recepies.append(case)
    return recepies



#will recieve the json file, get the recipe ID make a request using that ID and then get
# return the original link for that recipe
def getRecipeLink(yum_json,index):


    recipeID = yum_json["matches"][index]["id"]

    newUrl ="http://api.yummly.com/v1/api/recipe/"+recipeID+"?_app_id="+my_yum_api_key
    yum_json_get = requests.get(newUrl).json()
    yum_json_file_name = "yumGet.json"
    save_to_file(yum_json_file_name, yum_json_get)

    return yum_json_get["source"]["sourceRecipeUrl"]


def getRecipeName(yum_json,i):
    return yum_json["matches"][i]["recipeName"]

def getRecipeCookTime(yum_json,i):
    return (float(yum_json["matches"][i]["totalTimeInSeconds"])/60)

def getImageUrl(yum_json,i):
    return yum_json["matches"][i]["imageUrlsBySize"]["90"]

def getIngredients(yum_json,i):
    return yum_json["matches"][i]["ingredients"]





