import random
import copy

def polynom_to_array(polynom):
    liste = polynom.split("+")
    array = []
    for i in range(1,65):
        if f"x^{i}" in liste:
            array.append(i)

    return array[0:len(array)-1],array[-1]

def gen_inital(length):
    bit = [0b0,0b1]
    return [random.choice(bit) for x in range(length)]

def next(feedback,array):
    new = array[-1]
    for i in feedback:
        new = new^array[i-1]
    return new

def main(feedback,m):
    inital = gen_inital(m)
    array = []
    while True:
        if inital in array:
            break
        array.append(copy.deepcopy(inital))
        inital.insert(0,next(feedback,inital))
        inital.pop(-1)

    return array

if __name__ == "__main__":
    p_x,m = polynom_to_array(input("\n [+] enter polynom of lfsr: "))
    print(f" [+] the calculated bitlength is: {len(main(p_x,m))}")
    print("\n")
