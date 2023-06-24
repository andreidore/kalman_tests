import numpy as np


class GPS:

    def __init__(self):
        print("Init GPS.")

    def generate_gps_measurement(self, sensor_x, sensor_y):
        """
        Generates a GPS measurement.

        Returns:
            np.ndarray: The GPS measurement.
        """

        return np.array([0, 0])
