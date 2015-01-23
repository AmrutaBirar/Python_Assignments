#This is an exercise of Variables and operations on it Example 4

total_buses =  100
space_in_bus = 25.00
drivers = 30
passangers = 90
bus_not_driven = total_buses - drivers
buses_driven = drivers
bus_capacity = buses_driven * space_in_bus
avg_passangers_per_bus = passangers / buses_driven

print "Total number of cars are :",total_buses

print "There are only",drivers,"available"

print "There are ",bus_not_driven,"empty buses due to only few drivers"

print "We can  transport",bus_capacity,"passangers"
print "Passangers in each bus",avg_passangers_per_bus
