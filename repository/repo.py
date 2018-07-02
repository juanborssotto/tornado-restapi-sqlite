import sqlite3 as sqlite
from model import dish as dishModel


class Repo:
    def __init__(self):
        self.conn = None
        try:
            self.verifyDatabase()
        except Exception as e:
            print(e)

    def getDish(self, restaurant, dishID):
        dish = None
        try:
            conn = sqlite.connect('app.db')
            c = conn.cursor()
            args = (dishID, restaurant)
            c.execute('select id,\
                              restaurant,\
                              name,\
                              description,\
                              price\
                         from dishes\
                        where id = ?\
                          and restaurant = ?', args)
            result = c.fetchone()

            if result is not None:
                dish = dishModel.Dish()
                dish.setId(result[0])
                dish.setRestaurant(result[1])
                dish.setName(result[2])
                dish.setDescription(result[3])
                dish.setPrice(result[4])

            conn.close()
        except Exception as e:
            #Raise exception
            print(e)
        finally:
            return dish

    def insertDish(self, dish):
        dishID = None
        try:
            conn = sqlite.connect('app.db')
            try:
                c = conn.cursor()
                args = (dish.getRestaurant(), dish.getName(), dish.getDescription(), dish.getPrice())
                c.execute('insert into dishes(restaurant, name, description, price)\
                                       values(?,?,?,?)', args)
                conn.commit()
                dishID = c.lastrowid
            except Exception as e2:
                #Raise exception
                print(e2)
            finally:
                conn.close()
        except Exception as e:
            # Raise exception
            print(e)
        return dishID

    def verifyDatabase(self):
        conn = sqlite.connect('app.db')
        c = conn.cursor()
        try:
            c.execute('SELECT * FROM dishes')
        except:
            print('Creating table \'dishes\'')
            c.execute('CREATE TABLE dishes (\
                        id INTEGER PRIMARY KEY,\
                        price decimal(4,2),\
                        name text,\
                        description text,\
                        restaurant text)')
            print('Successfully created table \'dishes\'')
        conn.commit()
        conn.close()
