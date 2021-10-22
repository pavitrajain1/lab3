#2a
#data given
mean = [0, 0]
cov = [[13,-3], [-3,5]]
#using data to generate 1000 samples
a2x,a2y = np.random.multivariate_normal(mean, cov, 1000).T
#plot scatter plot
#title
plt.title("Generated Random samples",color='r')
plt.scatter(a2x,a2y)
#show grid
plt.grid(color='grey',linestyle='-.')
#show plot
plt.show()

#2b
#find eigenvalues and eigenvectors
W,V=np.linalg.eig(cov)
print("Eigenvalues are",W)
print("Eigenvectors are",V)
#origin
o=[0, 0]
#Vec1 and Vec2
ev1 = V[:,0]
ev2 = V[:,1]
# This line below plots the 2d points
plt.scatter(a2x,a2y,color=['g'])
#plot eigenvectors
plt.quiver(*o,*ev1, color=['r'], scale=4)
plt.quiver(*o,*ev2, color=['r'], scale=4)
#give title
plt.title("Eigen Vectors")
#show grid
plt.grid(color='grey',linestyle='-.')
#show plot
plt.show()


#2c
#fig1
#projection of points on Vec1
def dot(a,b,vx,vy):
    d= (a*vx + b*vy)/(((vx**2)+(vy**2))**0.5)
    prx=vx*d/(((vx**2)+(vy**2))**0.5)
    pry=vy*d/(((vx**2)+(vy**2))**0.5)
    return prx,pry
#x coordinates and y coordinates for eingenvector 1
V12cx=[]
V12cy=[]
for i in range(0,1000):
    #call function for projection
    prx,pry= dot(a2x[i],a2y[i],ev1[0],ev1[1])
    V12cx.append(prx)
    V12cy.append(pry)
#scatter points of random data
plt.scatter(a2x,a2y,color=['b'])
#plot eigenvectors
plt.quiver(*o,*ev1, color=['r'], scale=10)
plt.quiver(*o,*ev2, color=['r'], scale=4)
#plot projections corresponding to Vector1
plt.scatter(V12cx,V12cy,color=['g'],s=4)
#give title
plt.title("Projection of Vetor1")
#show grid
plt.grid(color='grey',linestyle='-.')
#show plot
plt.show()

#fig2
#x coordinates and y coordinates for eingenvector 2
V22cx=[]
V22cy=[]
for i in range(0,1000):
    #call function for projection
    prx,pry= dot(a2x[i],a2y[i],ev2[0],ev2[1])
    V22cx.append(prx)
    V22cy.append(pry)
#scatter points for random data
plt.scatter(a2x,a2y,color=['b'])
#plot eigenvectors
plt.quiver(*o,*ev1, color=['r'], scale=4)
plt.quiver(*o,*ev2, color=['r'], scale=10)
#plot projections corresponding to Vector 2
plt.scatter(V22cx,V22cy,color=['g'],s=4)
#give title
plt.title("Projection of Vetor2")
#show grid
plt.grid(color='grey',linestyle='-.')
#show plot
plt.show()

#2d
Drecx=[]
Drecy=[]
#get reconstructed data
for i in range(0,1000):
    Drecx.append(V22cx[i]+V12cx[i])
    Drecy.append(V22cy[i]+V12cy[i])
plt.title("Reconstructed data")
#scatter data
plt.scatter(Drecx,Drecy)
plt.show()
ED=[]
for i in range(0,1000):
    #calculate Eucledian distance for each  tuple.
    ED.append(round((((Drecx[i]-a2x[i])**2)+((Drecy[i]-a2y[i])**2))**0.5))
#print list of error
print(ED)
