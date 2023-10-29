def pecents():
    with open('sequence.txt', 'r') as f:
        k3=0
        k = 0
        for e in f:
            if abs(float(e[:-1]))<=3:
                k3+=1
            else:
                k+=1
        print(k3*100/(k3+k),'%'+' from -3 to 3', " ", k*100/(k3+k), '%' + ' of the rest')
