"""
Core logic for carbon-aware scheduling.
Author: Vedant Rajhans
"""

import random


class CarbonScheduler:

    def get_carbon_intensity(self, region):
        """Returns a mock carbon intensity value for the given region."""
        return random.randint(50, 400)

    def find_greenest_region(self, regions_list):
        """Iterates through regions and returns the one with the lowest carbon intensity."""
        intensities = {}
        for region in regions_list:
            intensities[region] = self.get_carbon_intensity(region)

        greenest_region = min(intensities, key=intensities.get)
        return greenest_region, intensities[greenest_region], intensities
