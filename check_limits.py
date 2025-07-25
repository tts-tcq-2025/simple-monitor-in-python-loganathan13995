def is_temperature_ok(t):
    return 0<=t <= 45

def is_soc_ok(s):
    return 20<=s <=80

def is_charge_rate_ok(cr):
    return cr <=0.8


def battery_is_ok(temperature, soc, charge_rate):
    # Define checks as a list of (condition_lambda, message) tuples
    checks = [
        (is_temperature_ok, 'Temperature is out of range!'),
        (is_soc_ok, 'State of Charge is out of range!'),
        (is_charge_rate_ok, 'Charge rate is out of range!')
    ]

    # Map parameters to a tuple for easier iteration
    params = (temperature, soc, charge_rate)

    for i, (condition_func, message) in enumerate(checks): # CCN: +1 (for loop)
        if not condition_func(params[i]):
            print(message)
            return False
    return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
