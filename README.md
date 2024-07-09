# epai5session5-template
EPAi5 Session 5 Template

# EPAi5 Session 5: Utility Functions for Mathematical and Conversion Operations

This repository houses a collection of versatile Python functions designed to facilitate various mathematical computations and unit conversions. Each function within this module serves a distinct purpose, tailored to handle specific tasks with precision and efficiency.

time_it: This function serves as a general utility for measuring the average execution time of any given function fn. It allows users to specify the number of times fn should be called (repetitions) along with any necessary positional (*args) or keyword (**kwargs) arguments. By timing multiple executions and calculating the average duration, time_it() provides valuable insights into the performance characteristics of functions, aiding in optimization and benchmarking efforts.

squared_power_list: When invoked, this function generates a list of numbers raised to various powers within a specified range. Users provide a base number, and optionally can define the start and end of the exponentiation range. This utility is particularly useful for generating sequences of numbers with exponential growth, facilitating calculations in areas such as finance, engineering, and scientific modeling.

polygon_area: Designed to compute the area of a regular polygon, this function accepts parameters defining the polygon's side length (length) and number of sides (sides). It adheres strictly to geometric constraints, supporting polygons with sides ranging from 3 to 6 inclusively. By leveraging mathematical formulas tailored to polygonal geometry, polygon_area() delivers accurate area calculations crucial in fields such as architecture, computer graphics, and geometric modeling.

temp_converter: This versatile function facilitates temperature conversions between Celsius and Fahrenheit scales. Users specify the temperature value (temp) and its initial unit (temp_given_in), choosing between Celsius ("c") or Fahrenheit ("f"). By applying established conversion formulas, temp_converter() ensures seamless and accurate transitions between temperature scales, supporting applications across meteorology, climate science, and everyday temperature monitoring.

speed_converter: Targeted at unit conversion tasks, this function transforms speeds expressed in kilometers per hour (kmph) into alternative units of distance (dist) and time (time). Users define the speed value (speed) and specify the desired output units for distance and time, including options such as meters, feet, yards, milliseconds, seconds, minutes, hours, and days. By implementing conversion factors meticulously calibrated to each unit, speed_converter() enables seamless speed transformations essential in transportation, physics, and sports analytics..
time_it(fn, *args, repetitions= 1, **kwargs), squared_power_list, polygon_area, temp_converter, speed_converter

## Functions Overview

### `time_it(fn, *args, repetitions=1, **kwargs)`
- Measures the average execution time of a specified function (`fn`) over multiple repetitions.
- **Parameters**:
  - `fn`: Function to be timed.
  - `repetitions`: Number of times to execute the function (default is 1).
  - Additional positional (`*args`) and keyword (`**kwargs`) arguments for `fn`.
- **Returns**: Average time taken for the function `fn` to execute over the specified repetitions.

### `squared_power_list(number, *args, start=0, end=5, **kwargs)`
- Generates a list of numbers raised to powers within a specified range.
- **Parameters**:
  - `number`: Base number for exponentiation (must be an integer).
  - `start`: Starting exponent (default is 0).
  - `end`: Ending exponent (default is 5).
- **Returns**: List of numbers where each element is `number` raised to the power of values from `start` to `end`.

### `polygon_area(length, *args, sides=3, **kwargs)`
- Calculates the area of a regular polygon based on its side length and number of sides.
- **Parameters**:
  - `length`: Length of each side of the polygon.
  - `sides`: Number of sides of the polygon (default is 3).
- **Returns**: Area of the polygon.
- **Constraints**: Supports polygons with 3 to 6 sides inclusive.

### `temp_converter(temp, *args, temp_given_in="f", **kwargs)`
- Converts temperatures between Celsius and Fahrenheit scales.
- **Parameters**:
  - `temp`: Temperature value to convert.
  - `temp_given_in`: Unit of the given temperature (`"c"` for Celsius, `"f"` for Fahrenheit, default is `"f"`).
- **Returns**: Converted temperature value.
- **Constraints**: Ensures valid temperature values and unit specifications.

### `speed_converter(speed, *args, dist="km", time="min", **kwargs)`
- Converts speed units from kilometers per hour (kmph) to other specified units.
- **Parameters**:
  - `speed`: Speed value to convert (in kmph).
  - `dist`: Unit of distance (`"km"`, `"m"`, `"ft"`, `"yrd"`, default is `"km"`).
  - `time`: Unit of time (`"ms"`, `"s"`, `"min"`, `"hr"`, `"day"`, default is `"min"`).
- **Returns**: Converted speed value.
- **Constraints**: Handles valid speed values and unit conversions as per specified units.

