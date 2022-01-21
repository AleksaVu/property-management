from models import Property
from models import Agent


property1 = Property(1, 'Beogradska', 4, 'Podgorica', True, 10000.0, 1)
property2 = Property(2, 'Budvanska', 6, 'Budva', False, 250000.0, 2)
property3 = Property(3, 'Tivatska', 21, 'Tivat', False, 350000.0, 1)
property4 = Property(4, 'Tivatska', 31, 'Tivat', True, 260000.0, 3)


agent1 = Agent(1, 'Aleksa', 'Vujosevic', 'aleksa@gmail.com')
agent2 = Agent(2, 'Vujos', 'Aleksic', 'vujos@gmail.com')
agent3 = Agent(3, "Nikola", "Nikolic", 'nikola@gmail.com')
agent4 = Agent(3, "Nikola", "Nikolic", 'nikola@gmail.com')

property1.create_table()
agent1.create_table()


agent1.add_agent()
agent2.add_agent()
agent3.add_agent()
agent4.add_agent()


property1.add_property()
property2.add_property()
property3.add_property()
property4.add_property()

property1.read_property_info()

property2.show_all_properties()
property2.show_available_properties()
property2.show_sold_properties()

property2.delete_property()

property1.update_price(500000.0)
property1.properies_agents()

agent1.show_alll_agents()
agent1.delete_agent()

property1.close_conn()
