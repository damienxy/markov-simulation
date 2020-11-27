from time import sleep
import cv2

import config
from supermarket import Supermarket


if __name__ == '__main__':
    print('Starting simulation')
    market = Supermarket()
    market.add_customers(config.initial_customer_count)

    while True:
        sleep(0.02)
        market.next_frame()
        cv2.imshow('Supermarket', market.frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('Ending simulation')
            break


cv2.destroyAllWindows()
