import numpy as np
import matplotlib.pyplot as plt
print("1. For point load at mid span")
print("2.For 2 point loads at 'a' and 'b' distance")
print("3.For uniform loading throughout length")
print("4.For udl at a distance 'c' metres")
print("5.For uniformly varying load or triangular throughout length")
n=int(input("enter the loading type:"))
if(n==1):
    l=float(input("Enter the length of beam in meter:"))
    w=float(input("Enter the magnitude of force in N:"))
    rb=w/2 
    ra=w/2 
    print(rb,ra)
    x=np.linspace(0,l,500)
    #sfd
    SF=[]
    BM=[]
    for i in x:
        if(0<=i<l/2):
            sf=ra
            bm=(ra*i)
        else:
            sf=ra-w
            bm=(ra*i)-(w*(i-l/2))
        SF.append(sf)
        BM.append(bm)
    BM_MAX=max(BM)
    print("maximum bending moment ={}KN-m".format(BM_MAX))
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,1)
    plt.plot(x,SF)
    plt.fill_between(x,SF,color='g',alpha=0.4,hatch='/////////')
    plt.title("Shear Force Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Shear Forc,KN")
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,2)
    plt.plot(x,BM,label='*:BM MAX')
    plt.fill_between(x,BM,color='r',alpha=0.4,hatch='---')
    plt.title("Bending Moment Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Bending Moment,KN-m")
    plt.legend()
    plt.show()
elif(n==2):
    a=float(input("Enter the 'a' distance in meter:"))
    b=float(input("Enter the 'b' distance in meter:"))
    c=float(input("Enter the 'c' distance in meter:"))
    fc=float(input("Enter the magnitude of force in N:"))
    fd=float(input("Enter the magnitude of force in N:"))
    l=a+b+c
    rb=(fc*a+fd*(a+b))/l
    ra=fc+fd-rb 
    print(rb,ra)
    x=np.linspace(0,l,500)
    #sfd
    SF=[]
    BM=[]
    for i in x:
        if(0<=i<l/2):
            sf=ra
            bm=(ra*i)
        elif(a<=i<(a+b)):
            sf=ra-fc
            bm=ra*i-fc*(i-a)
        else:
            sf=ra-fc-fd
            bm=(ra*i)-fc*(i-a)-fd*(i-a-b)
        SF.append(sf)
        BM.append(bm)
    BM_MAX=max(BM)
    print("maximum bending moment ={}KN-m".format(BM_MAX))
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,1)
    plt.plot(x,SF)
    plt.fill_between(x,SF,color='g',alpha=0.4,hatch='/////////')
    plt.title("Shear Force Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Shear Forc,KN")
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,2)
    plt.plot(x,BM,label='*:BM MAX')
    plt.fill_between(x,BM,color='r',alpha=0.4,hatch='---')
    plt.title("Bending Moment Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Bending Moment,KN-m")
    plt.legend()
    plt.show()
elif(n==3):
    l=float(input("Enter the length in meter:"))
    udl=float(input("Enter the magnitude of udl in N/m:"))
    rb=udl*l/2
    ra=udl*l/2
    print(rb,ra)
    x=np.linspace(0,l,500)
    #sfd
    SF=[]
    BM=[]
    for i in x:
        if(0<=i<l):
            sf=ra-udl*i
            bm=ra*i-udl*(i**2)/2
        else:
            sf=ra-udl*i+rb
            bm=ra*i-udl*(i**2)/2
        SF.append(sf)
        BM.append(bm)
    BM_MAX=max(BM)
    print("maximum bending moment ={}KN-m".format(BM_MAX))
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,1)
    plt.plot(x,SF)
    plt.fill_between(x,SF,color='g',alpha=0.4,hatch='/////////')
    plt.title("Shear Force Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Shear Forc,KN")
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,2)
    plt.plot(x,BM,label='*:BM MAX')
    plt.fill_between(x,BM,color='r',alpha=0.4,hatch='---')
    plt.title("Bending Moment Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Bending Moment,KN-m")
    plt.legend()
    plt.show()
elif(n==4):
    a=float(input("Enter the 'a' distance in meter:"))
    b=float(input("Enter the 'b' distance in meter:"))
    c=float(input("Enter the 'c' distance in meter:"))
    udl=float(input("Enter the magnitude of udl in N/m:"))
    l=a+b+c
    rb=(udl*b)/l
    ra=(udl*b)-rb
    print(rb,ra)
    x=np.linspace(0,l,500)
    #sfd
    SF=[]
    BM=[]
    for i in x:
        if(0<=i<a):
            sf=ra
            bm=(ra*i)
        elif(a<=i<(a+b)):
            sf=ra-udl*(i-a)
            bm=ra*i-udl*((i-a)**2)/2
        elif((a+b)<=i<(a+b+c)):#need to verify
            sf=ra-udl*b
            bm=(ra*i)-udl*b*(i-(a+(b/2)))
        else:
            sf=ra-udl*b+rb
            bm=(ra*i)-udl*b*(i-(a+(b/2)))
        SF.append(sf)
        BM.append(bm)
    BM_MAX=max(BM)
    print("maximum bending moment ={}KN-m".format(BM_MAX))
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,1)
    plt.plot(x,SF)
    plt.fill_between(x,SF,color='g',alpha=0.4,hatch='/////////')
    plt.title("Shear Force Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Shear Forc,KN")
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,2)
    plt.plot(x,BM,label='*:BM MAX')
    plt.fill_between(x,BM,color='r',alpha=0.4,hatch='---')
    plt.title("Bending Moment Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Bending Moment,KN-m")
    plt.legend()
    plt.show()
elif(n==5):
    l=float(input("Enter the length in meter:"))
    uvl=float(input("Enter the magnitude of uvl in N/m:"))
    rb=uvl*l/3
    ra=(uvl*l)/2-uvl*l/3
    print(rb,ra)
    x=np.linspace(0,l,500)
    #sfd
    SF=[]
    BM=[]
    for i in x:
        if(0<=i<l):
            sf=ra-0.5*uvl*i
            bm=ra*i-0.5*uvl*i*2*(i/3)
        else:#need to check
            sf=ra-0.5*uvl*i+rb
            bm=ra*i-0.5*uvl*i*2*(i/3)
        SF.append(sf)
        BM.append(bm)
    BM_MAX=max(BM)
    print("maximum bending moment ={}KN-m".format(BM_MAX))
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,1)
    plt.plot(x,SF)
    plt.fill_between(x,SF,color='g',alpha=0.4,hatch='/////////')
    plt.title("Shear Force Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Shear Forc,KN")
    plt.figure(figsize=(6,8),dpi=200)
    #plt.subplot(2,1,2)
    plt.plot(x,BM,label='*:BM MAX')
    plt.fill_between(x,BM,color='r',alpha=0.4,hatch='---')
    plt.title("Bending Moment Diagram",c='r',size=16)
    plt.xlabel("distance,m")
    plt.ylabel("Bending Moment,KN-m")
    plt.legend()
    plt.show()


