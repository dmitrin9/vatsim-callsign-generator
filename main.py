import random

airlines = {
    "US":["DAL", "AAL", "UAL", "ASA"],
    "India":["IAC", "AIC"],
    "Britain":["BAW"],
    "Canada":["ACA"],
}

def gen(country_origin, country_dest):
    callsign = ""
    number = ""
    if country_origin == country_dest:
        airline = random.choice(airlines[country_origin])
    else:
        airline = random.choice(airlines[country_origin] + airlines[country_dest])
    for _ in range(4):
        number += str(random.randint(0, 9))
    callsign += airline + number
    return callsign

if __name__ == "__main__":
    command = input("utils > ")
    splitted = command.split(" ")
    if splitted[0] == "callsign":
        if len(splitted) < 3:
            raise Exception("Invalid number of arguments.")
        else:
            callsign = gen(splitted[1], splitted[2])
            print("CALLSIGN -> ", callsign)
