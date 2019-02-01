#import the necessary libraries
import numpy as np 
import time
import matplotlib.pyplot as plt

#make two numpy arrays
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([1,3,2,5,7,8,8,9,10,12])

#plot the points 
plt.scatter(x,y,color='r')
plt.show()

#reshaping the arrays to vectors from rank one matrixes
X=x.reshape(10,1)
Y=y.reshape(10,1)

#initialization of weight and bias
w=0
b=0

#initializing the learning rate
lr=0.001

#initializing the number of epochs
epochs=100

#running the optimizing loop
for i in range(epochs):

    #calculating the linear function W*X +b which is an equation of line
    yp=w*X+b

    #calculating the dependence of w and b on cost. dw=dJ/dw and db=dJ/db where J is the cost
    dw=(yp-Y)*X
    db=(yp-Y)

    #calculating the cost
    cost=0.1*np.sum(np.square(Y-yp))

    #calculating dw and db for entire dataset
    dw=0.1*np.sum(dw)
    db=np.sum(db)*0.1

    #updating the values of w and b using gradient descent.
    w=w-lr*dw
    b=b-lr*db

    #plot the cost after every iteration. You can see the line learning and can see it move in place.
    y_pred=w*x+b
    
    plt.plot(x,y,'--')
    plt.plot(x,y_pred,'--')
    plt.show(block=False)
    
    time.sleep(0.2)
    plt.close()


    #print the cost after every iteration.
    print('cost after iteration',i+1,cost)


#plot the learnt line for the last time.
y_pred=w*x+b

plt.plot(x,y_pred,'--')
plt.show()
time.sleep(5)
plt.close()

#print w and b
print(w,b)

#predict values
print('enter x')
a=input()
a=int(a)
print(w*a+b)
