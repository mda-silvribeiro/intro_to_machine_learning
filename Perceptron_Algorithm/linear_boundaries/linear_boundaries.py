def lBoundaries( x, y) :
    return 2 * x + 1 * y - 18
# this is a simple code for answer the question
def trick(linex, liney, neg, x, y, bias):
    result = -1;
    time = 0;
    while not result > 0.0 :
        linex = (linex * x) + bias;
        liney = (liney * y) + bias;
        neg = neg - bias;
        result = (linex + liney) - (neg * 1);
        print(result)
        time += 1;
    time -= 1 # because the time will count the last number in the range
    return time;

print(trick(3, 4, 10, 1, 1, 0.1));
