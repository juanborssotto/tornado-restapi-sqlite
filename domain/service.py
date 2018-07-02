import json
from model import dish as dishModel


class Service:
    def __init__(self, repo):
        self.repo = repo

    def getDish(self, restaurant, dishID):
        dish = self.repo.getDish(restaurant, dishID)
        if dish is None:
            #Raise exception
            return '404 Not found'
        #Transform dish into a json
        jsonDish = json.dumps(dish.__dict__)
        return jsonDish


    def insertDish(self, restaurant, name, description, price):
        dish = dishModel.Dish()
        dish.setRestaurant(restaurant)
        dish.setName(name)
        dish.setDescription(description)
        dish.setPrice(price)
        id = self.repo.insertDish(dish)
        if(id is None):
            #Raise exception
            return 'Could not be inserted'
        dish.setId(id)
        # Transform dish into a json
        jsonDish = json.dumps(dish.__dict__)
        return jsonDish