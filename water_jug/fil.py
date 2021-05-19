print("Water Jug Problem"); 
cap_X = int(input("capacity of Jug X : "));
cap_Y = int(input("capacity of Jug Y : "));
target = int(input("target volume : "));

water_in_X = 0 ;
water_in_Y = 0 ;

print("op-A = if the smaller jug is empty fill it."); 
print("op-B = transfer water in smaller jug to larger"); 
print("op-C = if the larger jug is full emty it"); 
print("op-D = if the Larger jug is empty fill it."); 
print("op-E = transfer water in larger jug to smaller");
print("op-F = if the smaller jug is full emty it");
while True:
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