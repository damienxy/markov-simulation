import cv2
import numpy as np
import pandas as pd

import config
from customer import Customer


class Supermarket:
    def __init__(self):
        self.image = cv2.imread(config.market_filepath)
        self.check = cv2.imread(config.check_filepath)
        self.tpm = pd.read_csv(config.tp_matrix_filepath)
        self.customers = []
        self.customer_count = 0

    def add_customers(self, number):
        for _ in range(number):
            self.generate_customer_maybe()
        if self.customer_count < config.min_customer_count:
            self.add_customers(number)

    def generate_customer_maybe(self):
        if (self.customer_count < config.max_customer_count):
            # The more customers are in the store, the smaller the probability for a new customer
            probability = 1 - self.customer_count / config.max_customer_count
            generate = np.random.choice(
                [True, False], p=[probability, 1-probability])
            if (generate):
                self.customers.append(Customer(self.tpm))
                self.customer_count = len(self.customers)

    def next_frame(self):
        self.frame = self.image.copy()
        checkout_count = len(
            [cust for cust in self.customers if cust.checkout == True])
        self.customers = [
            cust for cust in self.customers if cust.checkout == False]
        for customer in self.customers:
            customer.move()
            x, y = customer.current_coordinates
            self.frame[y:y+config.icon_size, x:x +
                       config.icon_size] = customer.image
        self.add_customers(checkout_count)
