# input is 2 strings of 4 numbers: 0<=n<=10.
# first two numbers are coordinates (x,y) of the bootom left corner of rectangular second 2 are coordinates of top right
# rectangulars are not touching or crossing each other
# find minimal area of a square containing both rectangulars

def SquareMinArea(firstRect, secondRect):
    firstRect_coords = firstRect.split(' ')
    secondRect_coords = secondRect.split(' ')

    xcoords = []
    ycoords = []

    xcoords.append(int(firstRect_coords[0]))
    xcoords.append(int(firstRect_coords[2]))
    xcoords.append(int(secondRect_coords[0]))
    xcoords.append(int(secondRect_coords[2]))

    ycoords.append(int(firstRect_coords[1]))
    ycoords.append(int(firstRect_coords[3]))
    ycoords.append(int(secondRect_coords[1]))
    ycoords.append(int(secondRect_coords[3]))

    side = max((max(xcoords)-min(xcoords)), (max(ycoords)-min(ycoords)))
    return side**2
