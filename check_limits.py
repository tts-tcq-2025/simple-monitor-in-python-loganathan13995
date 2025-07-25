
def battery_is_ok(temperature, soc, charge_rate):
    # Define checks as a list of (condition_lambda, message) tuples
    checks = [
        (lambda t: t < 0 or t > 45, 'Temperature is out of range!'),
        (lambda s: s < 20 or s > 80, 'State of Charge is out of range!'),
        (lambda cr: cr > 0.8, 'Charge rate is out of range!')
    ]

    # Map parameters to a tuple for easier iteration
    params = (temperature, soc, charge_rate)

    for i, (condition_func, message) in enumerate(checks): # CCN: +1 (for loop)
        # Pass the correct parameter to the lambda function
        param_value = params[i] # This relies on the order of checks matching params
        if condition_func(param_value): # CCN: +1 (if)
            print(message)
            return False
    return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
