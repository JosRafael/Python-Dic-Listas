def conta(w, x):
    filt_num = list(filter(lambda i: x == i, w)) 
    return len(filt_num)

def main():
    print(conta([1,2,3,2,1,2, 1], 1))

main() 