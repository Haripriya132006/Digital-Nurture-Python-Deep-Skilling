def coordinateprinting(coordinates):
    try:
        if(len(coordinates)!=2):
            print("provide 2 coordinates")
            return
    except:
        print("enter list or tuple")
        return
    x,y=coordinates
    # isinstance checks if a specific value is of the given obj
    # if there need to check for either onr of set of objects put them in a tuple
    if(isinstance(x,int) and isinstance(y,int)):
        print("x",x)
        print("y",y)
coordinateprinting([2,3])
coordinateprinting((3,5))
coordinateprinting((3))
coordinateprinting((3,4,5))