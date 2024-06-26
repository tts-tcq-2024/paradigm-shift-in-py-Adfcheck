def is_temperature_within_range(temperature):
    return 0 <= temperature <= 45

def is_soc_within_range(soc):
    return 20 <= soc <= 80

def is_charge_rate_within_range(charge_rate):
    return charge_rate <= 0.8

def battery_is_ok(temperature, soc, charge_rate):
    # Check all conditions using the interface functions
    return (is_temperature_within_range(temperature) and
            is_soc_within_range(soc) and
            is_charge_rate_within_range(charge_rate))

if __name__ == '__main__':
    # Test cases
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False

# def battery_is_ok(temperature, soc, charge_rate):
#   if temperature < 0 or temperature > 45:
#     print('Temperature is out of range!')
#     return False
#   elif soc < 20 or soc > 80:
#     print('State of Charge is out of range!')
#     return False
#   elif charge_rate > 0.8:
#     print('Charge rate is out of range!')
#     return False

#   return True


# if __name__ == '__main__':
#   assert(battery_is_ok(25, 70, 0.7) is True)
#   assert(battery_is_ok(50, 85, 0) is False)
