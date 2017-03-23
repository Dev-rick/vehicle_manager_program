# -*- coding: utf-8 -*-
"""A big pharmaceutical company in your home town has a lot of different cars and other vehicles. So far they have been using
books to keep track of them, but now they'd like to have a computer program to do this.

Each vehicle has these attributes:
    brand
    model
    kilometers done so far
    general service date

The program should allow user to:

    see a list of vehicles the company has
    edit kilometers and the general service date for each vehicle
    add new vehicle

Use TXT file to store data about vehicles in. When you finish, push your code on GitHub and share it on the forum."""


class Vehicle(object):
    def __init__(self, brand, model, km_done_so_far, gen_service_date ):
        self.brand = brand
        self.model = model
        self.km_done_so_far = km_done_so_far
        self.gen_service_date = gen_service_date
    def __repr__(self):
        return "Brand: %s\n" \
               "Model: %s\n" \
               "Km done so far: %s\n" \
               "General service date: %s\n" % (self.brand, self.model, self.km_done_so_far, self.gen_service_date)



def get_brand_and_model(list_of_vehicles):
    for index, vehicle in enumerate(list_of_vehicles):
        print "\nID:%s| %s %s" % (index + 1, vehicle.brand, vehicle.model)

def get_km_done_so_far_and_gen_service_date():
    print "\n1)Km done so far\n2)General service date\n"


def edit_vehicle(list_of_vehicles):
    get_brand_and_model(list_of_vehicles)
    while True:
        try:
            selected_vehicle = int(raw_input("\nEnter the ID of the vehicle you want to change:\n>> "))-1
            break
        except ValueError:
            "Oops that was false. Try again!"
            continue
    selected_vehicle1 = list_of_vehicles[selected_vehicle]
    get_km_done_so_far_and_gen_service_date()
    while True:
        selected_attribute = int(raw_input("Enter the number of what you want to change:\n>> "))
        if selected_attribute == 1:
            selected_vehicle1.km_done_so_far = raw_input("Km done so far:\n>> ")
            break
        elif selected_attribute == 2:
            selected_vehicle1.gen_servie_date = raw_input("General service date:\n>> ")
            break
        else:
            print "Oops that was false. Try again!"
            continue
    print "\nYour vehicle was edited successfully!"




def get_everything(list_of_vehicles):
    for index, vehicle in enumerate(list_of_vehicles):
        print "\nID: %s)\n%s" % (index+1, vehicle)
    if not list_of_vehicles:
        print "\nSorry, you don't have registered vehicles\n"


def add_vehicle(list_of_vehicles):
    brand = raw_input("\nBrand:\n>> ")
    model = raw_input("Model:\n>> ")
    km_done_so_far = raw_input("Km done so far:\n>> ")
    gen_service_date = raw_input("General service date:\n>> ")
    new = Vehicle(brand, model, km_done_so_far, gen_service_date)
    list_of_vehicles.append(new)
    print "\nYour vehicle was successfully added!\n"


def delete_vehicle(list_of_vehicles):
    get_brand_and_model(list_of_vehicles)
    while True:
        try:
            selected_vehicle = int(raw_input("\nEnter the ID of the vehicle you want to delete:\n>> "))-1
            break
        except ValueError:
            print "Oops that was false. Try again!"
            continue
    selected_vehicle1 = list_of_vehicles[selected_vehicle]
    list_of_vehicles.remove(selected_vehicle1)

    print "Your vehicle was deleted successfully!"

def main():


    example = Vehicle("Toyota","CHR", "234", "2013")

    list_of_vehicles = [example]

    print "Welcome to your vehicle manage program!"
    while True:
        choice = raw_input("\nWhat do you want to do?\n"
                          "a) See a list of vehicles already registered\n"
                          "b) Register a vehicle\n"
                          "c) Edit a vehicle and recieve your list as list_of_vehicles.txt\n"
                          "d) Delete a registered vehicle\n"
                          "e) Exit\n>> ")
        if choice.lower() == "a":
            get_everything(list_of_vehicles)
        elif choice.lower() == "b":
            add_vehicle(list_of_vehicles)
        elif choice.lower() == "c":
            edit_vehicle(list_of_vehicles)
        elif choice.lower() == "d":
            delete_vehicle(list_of_vehicles)
            continue
        elif choice.lower() == "e":
            with open("list_of_vehicles.txt", "w+") as list_of_vehicles_file:
                list_of_vehicles_file.write("Your registered vehicles:\n\n")
                for index, vehicles in enumerate(list_of_vehicles):
                    list_of_vehicles_file.write("\nID: %s\n"
                                                "Brand: %s\n"
                                                "Model: %s\n"
                                                "Km done so far: %s\n"
                                                "General service date: %s\n" % (
                                                index + 1, vehicles.brand, vehicles.model, vehicles.km_done_so_far,
                                                vehicles.gen_service_date))
            break
        else:
            "Please choose one of the listed things!"
            continue



if __name__ == '__main__':
    main()
