from CBR import CBR
#0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 
def test():
    result = CBR("0 0 0 1 1 0 0 0 1 0 0 1 0 0 0 1 1 0 0 0 1 0 0 1 0 0 0 ")
    s = list(result)
    reply = ""
    for i in s:
        reply+=i
    return reply



if __name__ == '__main__':
    d = test()
    t = d.split(",")
    print(d)


