def main():
    nodes = 10
    file1 = open("distance.txt","r") 
    f1 = file1.readlines()
    i =0
    x =[]
    y =[]
    for l in f1:
        if i<nodes:
            vals = l.split(" ")
            x.append(float(vals[1]))
            y.append(float(vals[2]))
            i+=1
        else:
            break