# Lesson 1: Assignments ] Dictionaries
#Task 1:Restaurant Menue Update 
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}}
restaurant_menu['Beverages'] = {"Soda":1.15, "grape": 1.53}
print(restaurant_menu)
internal_marks = {"Steak":17.99}
restaurant_menu.update(internal_marks)
print(restaurant_menu)
del restaurant_menu["Starters"]
print(restaurant_menu)
# 3. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}}
def open(add):
    while True:
        service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}}
Nervice_tickets = {"Ticket003":{"Customer": "Bobby", "Issue":"Login problem", "Status": "open"}}
service_tickets.update(Nervice_tickets)
print(service_tickets)

def Update(status):
    while True:
        ticket_upd = {"Ticket003":{"Customer": "Bobby", "Issue":"Login problem", "Status": "complete"}}
        service_tickets.update(ticket_upd)
        print(service_tickets)

def filter(stat):
    return 
    print(service_tickets["Ticket001"])
    print(service_tickets["Ticket002"])
    print(service_tickets["Ticket003"])


