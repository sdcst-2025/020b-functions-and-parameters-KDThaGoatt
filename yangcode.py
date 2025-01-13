def area_rectangle(l,w):
    #print("\n\n\nThis is going to find the area of a rectangle")
    #print(l)
    #print(w)
    area = l * w
    #print(f"The area of this rectangle is {area}")
    return area
   


def output(l,w,a):
    print(f"\n\n The area of a rectangle with length {l} and width {w} is {a}")


if __name__ == "__main__":
    area =  area_rectangle(3,5)
    output(3,5,area)