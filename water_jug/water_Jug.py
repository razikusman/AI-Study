print("Water Jug Problem"); 
print("Jug X is 4L"); 
print("Jug Y is 3L"); 

x = 0; 
y = 0; 
while True:
    # add water reading input
    # check jug X
    if x < 4:
        water_in_X = int(input("pour water to X : ")); 
        x += water_in_X; 

    # check jug Y
    if y < 3:
        water_in_Y = int(input("pour water to Y : ")); 
        y += water_in_Y; 

    #################################

    if x >= 4 :
        print("jug x is full and its 4 l"); 
        x = 4; # X max = 4 
        displace_to_y = input("displace water in to Y (Y/N)"); 

        if displace_to_y == "N": 
            water_in_Y = int(input("pour water to Y : ")); 
            y += water_in_Y; 

        if displace_to_y == "y":
            dispalcement = 3-y; 
            x = x - dispalcement; 
            y += dispalcement; 

        empty_X = input("Empty the jug X (Y/N)"); 

        if empty_X == "Y":
            x=0; 

        empty_Y = input("Empty the jug Y (Y/N)"); 

        if empty_Y == "y":
            y = 0; 

    # check jug Y

    if y >= 3 :
        print("jug y is full and its 3 l"); 
        x = 3; # X max = 4 
        displace_to_X = input("displace water in to x (Y/N)"); 

        if displace_to_X == "N": 
            water_in_X = int(input("pour water to x : ")); 
            x += water_in_X; 

        if displace_to_X == "y":
            dispalcement = y-x; 
            y = y - dispalcement; 
            x += dispalcement; 

        empty_Y = input("Empty the jug X (Y/N)"); 

        if empty_Y == "Y":
            y=0; 

        empty_X = input("Empty the jug Y (Y/N)"); 

        if empty_X == "y":
            x = 0; 
    
    if(x == 2 ):
        empty_Y = input("Empty the jug Y (Y/N)"); 
        if empty_Y == "Y":
            y=0; 
            print("you got the answer jug Y : "+ y + "jug X : " + x); 
    
    if(y == 2 ):
        empty_X = input("Empty the jug X (Y/N)"); 
        if empty_X == "Y":
            x=0; 
            print("you got the answer jug Y : "+ y + "jug X : " + x); 
    
