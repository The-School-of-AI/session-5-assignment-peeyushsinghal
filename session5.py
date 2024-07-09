"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time as time_lib
import math


def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    if repetitions >= 0:
        time_start = time_lib.time()
        for _ in range(repetitions):
            fn(*args, **kwargs)
        time_end = time_lib.time()
        time_diff = time_end - time_start
        return time_diff
    else:
        raise ValueError("Repetition should be positive number")


def squared_power_list(number, *args, start=0, end=5, **kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")

    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")

    if start > end:
        raise ValueError("Value of start should be less than end")

    if number > 10:
        raise ValueError("Value of number should be less than 10")

    if len(args) > 0:
        raise TypeError("takes maximum 1 positional arguments")
    if len(kwargs) > 0:
        raise TypeError("maximum 2 keyword/named arguments")

    list_squared_power = []
    while start < end:
        list_squared_power.append(int(math.pow(number, start)))
        start += 1
    return list_squared_power

    # Return the list of number to the power of numbers from start to end

    pass


def polygon_area(length, *args, sides=3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    if length is None:
        raise TypeError(
            "polygon_area() missing 1 required positional argument: 'length. no mandatory positonal arguments"
        )  # ("the function does not support no mandatory positonal arguments")
    if not (isinstance(length, int) or isinstance(length, float)):
        raise ValueError("incorrect values for positional argument length")
    if not isinstance(sides, int):
        raise TypeError("Integer expected for sides")
    if length <= 0:
        raise ValueError("Permissible values for len > 0")

    if len(args) > 0:
        raise TypeError(
            "polygon_area function takes maximum 1 positional arguments, more provided"
        )
    if len(kwargs) > 0:
        raise TypeError(
            "polygon_area function take maximum 1 keyword/named arguments, more provided"
        )

    # Validations
    if sides in [3, 4, 5, 6]:
        return (sides * length**2) / (4 * math.tan(math.pi / sides))

    else:
        raise ValueError("Value of sides should be 3, 4, 5 or 6 only")

    return


def temp_converter(temp, *args, temp_given_in="f", **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""
    if not (isinstance(temp, int) or isinstance(temp, float)):
        raise ValueError("incorrect values for positional argument temp")

    if not isinstance(temp_given_in, str):
        raise TypeError("Charcater string expected")
    else:
        if temp_given_in.lower() not in ["c", "f"]:
            raise ValueError("Only f or c is allowed")

    if len(args) > 0:
        raise TypeError(
            "temp_converter function takes maximum 1 positional arguments, more provided"
        )
    if len(kwargs) > 0:
        raise TypeError(
            "temp_converter function take maximum 1 keyword/named arguments, more provided"
        )

    if temp_given_in.lower() == "c":
        if temp > -273.15:
            return (temp * 9 / 5) + 32

        else:
            raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")

    if temp_given_in.lower() == "f":
        if temp > -459.67:
            return (temp - 32) * 5 / 9
        else:
            raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")


def speed_converter(speed, *args, dist="km", time="min", **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day"""
    print("*****", args, len(args))
    print("!!!!!", kwargs, len(kwargs))
    print(type(speed))

    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for distance unit")
    else:
        if dist.lower() not in ["km", "m", "ft", "yrd"]:
            raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")

    if not isinstance(time, str):
        raise TypeError("Charcater string expected")
    else:
        if time.lower() not in ["ms", "s", "min", "hr", "day"]:
            raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")

    if not (isinstance(speed, int) or isinstance(speed, float)):
        raise TypeError("Speed can be int or float type only")
    if speed < 0.0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")

    if len(args) > 0:
        raise TypeError(
            "speed_converter function takes maximum 1 positional arguments, more provided"
        )
    if len(kwargs) > 0:
        raise TypeError(
            "speed_converter function take maximum 2 keyword/named arguments, more provided"
        )

    # if (bool(speed)+len(args)) != 1:
    #     raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided. speed_converter function take maximum 2 keyword/named arguments, more provided")
    # if (kwargs is not None) and len(list(kwargs.keys())) == 0:
    #     raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided. speed_converter function take maximum 2 keyword/named arguments, more provided")

    if dist.lower() == "m":
        speed = speed * 1000
    elif dist.lower() == "ft":
        speed = speed * 3280.8375  # 3280.839895
    elif dist.lower() == "yrd":
        speed = speed * 1093.609  # 1093.6132983377
    else:
        pass

    if time.lower() == "ms":
        speed = speed / 3600000
    elif time.lower() == "s":
        speed = speed / 3600
    elif time.lower() == "min":
        speed = speed / 60
    elif time.lower() == "day":
        speed = speed * 24
    else:
        pass

    print("speed after conversion is:", round(speed))
    return round(speed)
