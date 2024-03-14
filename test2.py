# Using try and except to prevent errors
try:
    f = open('hardware.dat', 'w')
    n = int(input("Number of files to add: "))

    # creating dictionaries in a list item
    content = [
        {
            "records": 17,
            "Tool": "Hammer",
            "quantity": 76,
            "cost": 11.99
        },
        {
            "records": 37,
            "Tool": "Saw",
            "quantity": 88,
            "cost": 12.00
        },
        {
            "records": 68,
            "Tool": "Screwdriver",
            "quantity": 106,
            "cost": 6.99
        },
        {
            "records": 83,
            "Tool": "Wrench",
            "quantity": 34,
            "cost": 7.50
        }
    ]

    # Looping through the variable database
    for i in range(n):
        data = {
            "records": int(input("Input the Record Number: ")),
            "Tool": input("Input the Tool Name: "),
            "quantity": int(input("Input the Quantity: ")),
            "cost": float(input("Input the cost: "))
        }
        content.append(data)
    
    f.write(f'Write Number \t Tool Name \t Quantity')

    for parameter in content:
        f.write(f'{parameter['records']: <20} \t {parameter["Tool"]:<15} \t {parameter["quantity"]:<15} \t {parameter["cost"]}\n')
except ValueError:
    print(f'File is absent: Error! can\'t find file')

