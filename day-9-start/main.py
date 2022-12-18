programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

print (programming_dictionary["Bug"])

for item in programming_dictionary:
    print (item)

#Nesting dictionary in a disctionary
travel_log = {
    "France": {
        "cities_visited": ["Paris","Lille","Dijon"],  
        "total_visits": 12
        },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]

}

#Nesting dictionary in aList

travel_log = [
    {
        "country": "France",         
        "cities_visited": ["Paris","Lille","Dijon"],  
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
        "total_visits": 3,
    },

]