print("Water Jug Problem"); 
print("Jug X is 4L"); 
print("Jug Y is 3L"); 

x = 0; 
y = 0; 
while True:
    # add water reading input
    # check jug X
    if x < 4:
        water_in_X = input("pour water to X (Y/N)"); 
        if water_in_X == "Y":
            x = 4; 

    # check jug Y
    if y < 3:
        water_in_Y = input("pour water to Y (Y/N)"); 
        if water_in_Y == "Y":
            y = 3; 

    #################################

    if x >= 4 :
        print("jug x is full and its 4 l"); 
        x = 4; # X max = 4 

    if y >= 3 :
        print("jug y is full and its 3 l"); 
        y = 3; # X max = 3

    displace_to_y = input("displace water in X to Y (Y/N)"); 

    if displace_to_y == "Y":
        dispalcement = 3-y; 
        if dispalcement >= x: 
            y += x;
            x = 0;
        else:
            x = x - dispalcement; 
            y += dispalcement; 
    
    print("Y:" + str(y) + "l X:"+ str(x) + "l");  
    displace_to_X = input("displace water in Y to x (Y/N)");  

    if displace_to_X == "Y":
        dispalcement = 4-x; 
        if dispalcement >= y: 
            x += y;
            y = 0;

        else:
            y = y - dispalcement; 
            x += dispalcement;
    
    print("Y:" + str(y) + "l X:"+ str(x) + "l"); 
    empty_X = input("Empty the jug X (Y/N)"); 

    if empty_X == "Y":
        x=0; 

    print("Y:" + str(y) + "l X:"+ str(x) + "l"); 
    empty_Y = input("Empty the jug Y (Y/N)"); 

    if empty_Y == "Y":
        y = 0; 
    print("Y:" + str(y) + "l X:"+ str(x) + "l"); 
    if(x == 2 ):
        y=0; 
        print("you got the answer jug Y : "+ str(y) + "jug X : " + str(x)); 
        break;
    
    if(y == 2 ):
        x=0; 
        print("you got the answer jug Y : "+ str(y) + "jug X : " + str(x)); 
        break;