import sqlite3


class Property:
    ''''
        Property class represents single property.

        Atributes
        ----------
        id: integer 
        address: string (address of the property)
        address_number: integer (adress number of property)
        city: string (city where property is located)
        availability: boolean (proerty availability status)
        price: real (price of property)

        Methods
        ----------


        add_property()
        delete_property()
        read_property_info()
        update_price(new_price)


        show_all_properties()
        show_available_properties()
        show_sold_properties()


    '''

    def __init__(self, id, address, address_number, city, availability, price, agent_id):
        self.id = id
        self.address = address
        self.address_number = address_number
        self.city = city
        self.availability = availability
        self.price = price
        self.agent_id = agent_id

        self.conn = sqlite3.connect('properties.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        # self.cursor.execute(""" DROP TABLE properties""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS properties(
                         id INTEGER PRIMARY KEY,
                         address TEXT,
                         address_number INTEGER,
                         city TEXT NOT NULL,
                         availability INTEGER NOT NULL,
                         price REAL NOT NULL,
                         agent_id  NOT NULL,
                         FOREIGN KEY(agent_id) REFERENCES agents(id)
                         )""")

    def update_price(self, new_price):
        self.cursor.execute(
            """ UPDATE properties SET price = (?) WHERE id = (?)""", (new_price, self.id,))
        self.conn.commit()

    def add_property(self):
        item = [
            self.id,
            self.address,
            self.address_number,
            self.city,
            self.availability,
            self.price,
            self.agent_id,
        ]
        self.cursor.execute(
            """ INSERT OR IGNORE INTO properties VALUES (?,?,?,?,?,?,?)""", item)
        self.conn.commit()

    def delete_property(self):
        self.cursor.execute(
            "DELETE FROM properties WHERE id = (?)", (self.id,))
        self.conn.commit()

    def read_property_info(self):
        if(self.availability == True):
            print(
                f' Property with id {self.id} is available, and its located in {self.address}, {self.address_number} in {self.city}.')
        else:
            print(
                f' Property with id {self.id} is not available.')

    # Mozda ovo da napravim drug klasu npr. PropertyListing koja nasljedjuje property
    # i da tamo premjestim dolje metode, pa da napravim par funkcija sa sortiranjem
    # sort by price, availability, city ... ?
    def show_all_properties(self):
        self.cursor.execute(""" SELECT * FROM properties""")
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def show_available_properties(self):
        print('Available properties:')
        self.cursor.execute(
            """ SELECT * FROM properties WHERE availability = (?)""", (1,))
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def show_sold_properties(self):
        print('Not available properties:')
        self.cursor.execute(
            """ SELECT * FROM properties WHERE availability = (?)""", (0,))
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    # show properties that are related to specific agent
    def properies_agents(self):
        self.cursor.execute(
            """ SELECT * FROM properties WHERE agent_id = (?)""", (self.agent_id,))
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    # def __repr__(self):
    #     return f'{self.id}'

    def close_conn(self):
        self.conn.close()


class Agent:
    '''
        Agent classs represents single agent. 

        Atributes
        ----------

        id: integer
        name: string
        lastname: string
        email_address: string

        Methods
        ----------

        add_agent()
        delete_agents()
        show_all_agents()


    '''

    def __init__(self, id, name, lastname, email_address):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email_address = email_address

        self.conn = sqlite3.connect('properties.db')
        self.cursor = self.conn.cursor()

    def create_table(self):

        try:
            self.cursor.execute("""CREATE TABLE agents(
                         id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         lastname TEXT NOT NULL,
                         email_address TEXT NOT NULL
                         )""")

        except sqlite3.DatabaseError:
            print("Table already exists.")

        # self.cursor.execute(""" DROP TABLE agents""")
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS agents(
        #                  id INTEGER PRIMARY KEY,
        #                  name TEXT NOT NULL,
        #                  lastname TEXT NOT NULL,
        #                  email_address TEXT NOT NULL
        #                  )""")

    def add_agent(self):
        item = [
            self.id,
            self.name,
            self.lastname,
            self.email_address,
        ]
        self.cursor.execute(
            """ INSERT OR IGNORE INTO agents VALUES (?,?,?,?)""", item)
        self.conn.commit()

    def delete_agent(self):
        self.cursor.execute(
            "DELETE FROM agents WHERE id = (?)", (self.id,))
        self.conn.commit()

    def show_alll_agents(self):
        self.cursor.execute(""" SELECT * FROM agents""")
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def close_conn(self):
        self.conn.close()
