with open('git_log.txt','r') as fd:
    print(fd)
    data =fd.readlines()
    size=len(data)-1
    print("size", size)
    j=0
for i, line in enumerate(data):
    #print(line)
    #print("i",i)
    if "Author:" in line and size != j:
        #print(line)
        for j in range(i-1,i+5):
            #print("-->i", i)
            #print("j", j)
            if data[j] != "\n":# and size != j:
                print("J-->%d data%s" %(j, data[j]))
                #print( data[j])
        print("\n\n")