import psycopg2

def callFilmInStock():
    try:
        dbConnect = psycopg2.connect(user="postgres",password="loltehelf",host="127.0.0.1",port="5432",database="dvdrental")








        cursor = dbConnect.cursor()

        cursor.callproc('film_in_stock',[inventory_id,])

        print('Connected!')
        print()
        print('Displaying films in stock:')

        data = cursor.fetchall()
        for row in result:
            print('InventoryID: ',row[0])

    except:
        print()

callFilmInStock()
