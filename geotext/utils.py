

import math


def degrees_to_meters(lon, lat):

    """
    Convert degrees -> meters.

    Args:
        degrees (float)
    """

    half_circumference = 20037508.34

    x = lon * half_circumference / 180

    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * half_circumference / 180

    return [x, y]
