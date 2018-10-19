from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
max_mass = 4
current_mass = items['id']['mass'] + items['laptop']['mass'] + items['money']['mass']
# Start game at the reception
current_room = rooms["Reception"]
