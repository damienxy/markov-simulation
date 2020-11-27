import numpy as np
import cv2

import config


class Customer:
    def __init__(self, tpm):
        self.tpm = tpm
        self.image = self.get_colored_icon()
        self.checkout = False
        self.direction = 'up'
        self.target_location = config.initial_section
        self.target_coordinates = self.get_semi_random_coord(
            config.initial_section)
        self.current_coordinates = self.get_semi_random_coord(
            config.initial_section)

    def get_random_color(self):
        '''
        Check out www.rgbcolors.xyz, a site I made while 
        I was trying to find out which color combinations 
        would look nice in the simulation
        '''
        red = np.random.randint(0, 90)
        green = np.random.randint(70, 255)
        blue = np.random.randint(0, 255)

        return blue, green, red

    def get_colored_icon(self):
        return np.full((config.icon_size, config.icon_size, 3), self.get_random_color(), dtype='int8')

    def get_semi_random_coord(self, section):
        xmin, xmax = config.coordinates[section]['x']
        ymin, ymax = config.coordinates[section]['y']
        x = np.random.randint(xmin, xmax)
        y = np.random.randint(ymin, ymax)
        return x, y

    def get_next_location(self):
        previous = self.target_location
        self.target_location = np.random.choice(
            list(self.tpm['location']), p=list(self.tpm[self.target_location]))
        if previous != self.target_location:
            self.target_coordinates = self.get_semi_random_coord(
                self.target_location)
        else:
            self.get_next_location()

    def get_direction(self, section):
        if section == "checkout":
            self.direction = "down"
        else:
            self.direction = np.random.choice(['up', 'down'])

    def move(self):
        target = self.target_location
        cur_x, cur_y = self.current_coordinates
        tar_x, tar_y = self.target_coordinates
        xmin, xmax = config.coordinates[target]['x']
        ymin, ymax = config.coordinates[target]['y']

        ymin_top, ymax_top = config.coordinates['top']['y']
        ymin_bottom, ymax_bottom = config.coordinates['bottom']['y']

        # if within correct x coordinates
        if xmin <= cur_x <= xmax:
            # if within correct y coordinates
            if ymin <= cur_y <= ymax:
                if self.target_location == 'checkout':
                    self.checkout = True

                else:
                    self.get_next_location()
                    self.get_direction(self.target_location)
            else:
                if cur_y < ymin:
                    cur_y += config.step
                elif cur_y > ymin:
                    cur_y -= config.step
        else:
            if self.direction == 'down':
                ymin_edge = ymin_bottom
                ymax_edge = ymax_bottom
            else:
                ymin_edge = ymin_top
                ymax_edge = ymax_top

            if cur_y < ymin_edge:
                cur_y += config.step
            elif cur_y > ymax_edge:
                cur_y -= config.step
            else:
                if cur_x < tar_x:
                    cur_x += config.step
                elif cur_x > tar_x:
                    cur_x -= config.step

        self.current_coordinates = (cur_x, cur_y)
