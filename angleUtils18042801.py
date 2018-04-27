import numpy as np

#https://stackoverflow.com/questions/15927755/opposite-of-numpy-unwrap
#https://stackoverflow.com/questions/37358016/numpy-converting-range-of-angles-from-pi-pi-to-0-2pi
def wrapToPi(a):
    return (a+np.pi)%(2*np.pi)-np.pi
def wrapTo2Pi(a):
    return (a)%(2*np.pi)
def wrapTo180(a):
    return (a+180)%(360)-180
def wrapTo360(a):
    return (a)%(360)

# radius,angle to complex
#https://stackoverflow.com/questions/16444719/python-numpy-complex-numbers-is-there-a-function-for-polar-to-rectangular-co
def rect(r,phi):
    return r*np.exp(1j*phi)

#import cmath.rect
def nprect(r,phi):
    import cmath
    nprect1 = np.vectorize(cmath.rect)
    return nprect1(r,phi)

def subAngles(angle2,angle1):
    return wrapToPi(angle2-angle1)

if __name__ == "__main__":
    
    c1 = rect(1,np.deg2rad(30))
    c2 = nprect(1,np.deg2rad(30))
    print (c1,c2)
    
    list1 = np.arange(-180,181,15)
    #print (list1)
    print (wrapTo360(list1))
    list1 = np.deg2rad(list1)
    list2 = wrapTo2Pi(list1)
    print (np.rad2deg(list2))
    #list3 = (list2+np.pi)%(2*np.pi)-np.pi
    print (np.rad2deg(wrapToPi(list2)))
    print (wrapTo180(np.rad2deg(list2)))
    #print (np.rad2deg(list3))
    
    import itertools
    #https://qiita.com/wakamezake/items/0744268e928a28810c20
    #a = np.array(list(itertools.product( np.arange(-180,181,1),np.arange(-180,181,1))))
    #numpy only ver
    a = np.array(np.meshgrid(np.arange(-180,181,1),np.arange(-180,181,1))).T.reshape(-1,2)
    a1 = np.deg2rad(a)
    a1 = wrapToPi(a1)
    a2 = wrapTo2Pi(a1)
    a3 = wrapToPi(a1[:,0]-a1[:,1])- wrapToPi(a2[:,0]-a2[:,1])
    print (np.max(np.abs(wrapToPi(a3))))   
    print (np.allclose( wrapToPi(a3), 0))
    
    a5 = a1[:,0] + a1[:,1]
    a6 = subAngles(a5,a1[:,0])
    print (np.max(np.abs(wrapToPi(a6-a1[:,1]))))
    print (np.allclose( wrapToPi(a6-a1[:,1]), 0))
    
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,10))
    for ang1 in np.arange(0,360,45):
        xList=[]
        yList=[]
        for ang2 in np.arange(0,360,1):
            rad1=np.deg2rad(ang1)
            rad2=np.deg2rad(ang2)
            xList.append(ang2)
            a = wrapToPi(rad2-rad1)
            yList.append( np.rad2deg( a ) )
        plt.plot(xList,yList,label="{}".format(ang1))
    
    plt.legend()
    plt.show()
    plt.clf()
    plt.close()
    
