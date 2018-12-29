def sun_angle(time):
    #replace this for solution
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])

    if hour < 6 or (hour > 18 and minute < 0):
        return "I don't see the sun!"
    time_minuite = (hour - 6) * 60 + minute
    kakudo_per_minute = 180 / (12 * 60)
    return time_minuite * kakudo_per_minute


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(sun_angle("07:00"))# == 15
    print(sun_angle("01:23"))# == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")