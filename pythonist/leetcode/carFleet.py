def carFleet(target, position, speed ):
    cars = list(zip(position, speed))
    cars.sort(reverse=True)

    print(cars)
    fleets = 0
    slowest_car_time_to_dest = 0

    for start, speed in cars:
        print(start, speed)
        cur_car_time_to_dest = (target-start)/speed
        print(cur_car_time_to_dest, slowest_car_time_to_dest, fleets)
        if slowest_car_time_to_dest < cur_car_time_to_dest:
            fleets += 1
            slowest_car_time_to_dest = cur_car_time_to_dest
    return fleets

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', carFleet(10, [6, 8], [3, 2]))



if __name__ == "__main__":
    main()
