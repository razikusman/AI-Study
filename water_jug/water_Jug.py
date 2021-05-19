print("Water Jug Problem"); 
cap_X = int(input("capacity of Jug X : "));
cap_Y = int(input("capacity of Jug Y : "));
target = int(input("target volume : "));

print("op-A = if the smaller jug is empty fill it."); 
print("op-B = transfer water in smaller jug to larger"); 
print("op-C = if the larger jug is full emty it"); 
print("op-D = if the Larger jug is empty fill it."); 
print("op-E = transfer water in larger jug to smaller");
print("op-F = if the smaller jug is full emty it"); 

while True:
    water_in_X = 0 ;
    water_in_Y = 0 ;
    # fil lower capacity first
    while water_in_X != target and water_in_Y != target:
        
        if cap_X < cap_Y :
            water_in_X = cap_X;
            print("op-A -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]"); 

            dis_max = cap_Y - water_in_Y;
            if dis_max >= water_in_X:
                water_in_Y += water_in_X;
                water_in_X = 0;
            else:
                water_in_X = water_in_X - dis_max; 
                water_in_Y = cap_Y;

            print("op-B -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");
        
        else:
            water_in_Y = cap_Y;
            print("op-A -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]"); 

            dis_max = cap_X - water_in_X;
            if dis_max >= water_in_Y:
                water_in_X += water_in_Y;
                water_in_Y = 0;
            else:
                water_in_Y = water_in_Y - dis_max; 
                water_in_X = cap_X;

            print("op-B -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

    if cap_X > cap_Y:
        water_in_X = 0;
        print("op-C -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");
        print("Target found ->");

    else:
        water_in_Y = 0;
        print("op-C -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");
        print("Target found ->");

    print("_________________________________________________________________________________________")
    water_in_X = 0 ;
    water_in_Y = 0 ;
# fil Higher capacity first
    while water_in_X != target and water_in_Y != target:
        
        if cap_X > cap_Y :

            if water_in_X == 0 :
                # fill
                water_in_X = cap_X;
                print("op-D -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

            # displace
            dis_max = cap_Y - water_in_Y;
            if dis_max >= water_in_X:
                water_in_Y += water_in_X;
                water_in_X = 0;
            else:
                water_in_Y += dis_max;
                water_in_X -= dis_max;
            print("op-E -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

            # expty smaller and displace
            if water_in_Y == cap_Y:
                water_in_Y = 0;
                print("op-F -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

                if cap_Y >= water_in_X and water_in_X != target:
                    water_in_Y = water_in_X;
                    water_in_X = 0;
                    print("op-E -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");
        
        else:
            while water_in_X != target and water_in_Y != target:

                # fill
                if water_in_Y == 0:
                    water_in_Y = cap_Y;
                    print("op-D -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]"); 

                # displace 
                dis_max = cap_X - water_in_X;
                if dis_max >= water_in_Y:
                    water_in_X += water_in_Y;
                    water_in_Y = 0;
                else:
                    water_in_X += dis_max;
                    water_in_Y -= dis_max;
                
                print("op-E -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

                # empty smaller and displace to smaller
                if water_in_X == cap_X:
                    water_in_X = 0;
                    print("op-F -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

                    if cap_X >= water_in_Y and water_in_Y != target:
                        water_in_X = water_in_Y;
                        water_in_Y = 0;
                        print("op-E -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");


    if cap_X > cap_Y:
        print("Target found -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

    else:
        print("Target found -> ["+ str(water_in_X) + " " + str(water_in_Y) + "]");

    break;

    # # add water reading input
    # # check jug X
    # if x < 4:
    #     water_in_X = input("pour water to X (Y/N)"); 
    #     if water_in_X == "Y":
    #         x = 4; 

    # # check jug Y
    # if y < 3:
    #     water_in_Y = input("pour water to Y (Y/N)"); 
    #     if water_in_Y == "Y":
    #         y = 3; 

    # #################################

    # if x >= 4 :
    #     print("jug x is full and its 4 l"); 
    #     x = 4; # X max = 4 

    # if y >= 3 :
    #     print("jug y is full and its 3 l"); 
    #     y = 3; # X max = 3

    # displace_to_y = input("displace water in X to Y (Y/N)"); 

    # if displace_to_y == "Y":
    #     dispalcement = 3-y; 
    #     if dispalcement >= x: 
    #         y += x;
    #         x = 0;
    #     else:
    #         x = x - dispalcement; 
    #         y += dispalcement; 
    
    # print("Y:" + str(y) + "l X:"+ str(x) + "l");  
    # displace_to_X = input("displace water in Y to x (Y/N)");  

    # if displace_to_X == "Y":
    #     dispalcement = 4-x; 
    #     if dispalcement >= y: 
    #         x += y;
    #         y = 0;

    #     else:
    #         y = y - dispalcement; 
    #         x += dispalcement;
    
    # print("Y:" + str(y) + "l X:"+ str(x) + "l"); 
    # empty_X = input("Empty the jug X (Y/N)"); 

    # if empty_X == "Y":
    #     x=0; 

    # print("Y:" + str(y) + "l X:"+ str(x) + "l"); 
    # empty_Y = input("Empty the jug Y (Y/N)"); 

    # if empty_Y == "Y":
    #     y = 0; 
    # print("Y:" + str(y) + "l X:"+ str(x) + "l"); 
    # if(x == 2 ):
    #     y=0; 
    #     print("you got the answer jug Y : "+ str(y) + "jug X : " + str(x)); 
    #     break;
    
    # if(y == 2 ):
    #     x=0; 
    #     print("you got the answer jug Y : "+ str(y) + "jug X : " + str(x)); 
    #     break;