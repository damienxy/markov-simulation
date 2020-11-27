market_filepath = './img/market2.png'
check_filepath = './img/check.png'
tp_matrix_filepath = './transition_probabilities.csv'


icon_size = 40
step = int(icon_size / 4)

min_customer_count = 10
max_customer_count = 30

initial_customer_count = 5
initial_section = 'entrance'

coordinates = {
    'drinks': {'x': (100, 230 - icon_size), 'y': (250, 350 - icon_size)},
    'dairy': {'x': (340, 460 - icon_size), 'y': (250, 350 - icon_size)},
    'spices': {'x': (570, 690 - icon_size), 'y': (250, 350 - icon_size)},
    'fruit': {'x': (800, 920 - icon_size), 'y': (250, 350 - icon_size)},
    'checkout': {'x': (150, 430 - icon_size), 'y': (680, 750 - icon_size)},
    'entrance': {'x': (800, 920 - icon_size), 'y': (660, 750 - icon_size)},
    'top': {'x': (100, 920 - icon_size), 'y': (100, 170 - icon_size)},
    'bottom': {'x': (100, 920 - icon_size), 'y': (475, 540 - icon_size)},
}
