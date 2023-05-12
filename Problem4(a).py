
import numpy as np
 
 
def getInput():
    matrix_a = np.mat([[21.0,67.0,88.0,73.0], [76.0,63.0,7.0,20.0], [0.0,85.0,56.0,54.0], [19.3,43.0,30.2,29.4]],dtype=float)
    matrix_b = np.mat([141.0,109.0,218.0,93.7])
    return matrix_a, matrix_b
 
def SequentialGauss(mat_a):
    for i in range(0, (mat_a.shape[0])-1):
        if mat_a[i, i] == 0:
            print(mat_a)
            break
        else:
            for j in range(i+1, mat_a.shape[0]):
                mat_a[j:j+1 , :] = mat_a[j:j+1,:] - \
                                                    (mat_a[j,i]/mat_a[i,i])*mat_a[i, :]
    return mat_a
 
 
def revert(new_mat):
    x = np.mat(np.zeros(new_mat.shape[0], dtype=float))
    number = x.shape[1]-1
    # print(number)
    b = number+1
    x[0,number] = new_mat[number,b]/new_mat[number, number]
    for i in range(number-1,-1,-1):
        try:
            x[0,i] = (new_mat[i,b]-np.sum(np.multiply(new_mat[i,i+1:b],x[0,i+1:b])))/(new_mat[i,i])
        except:print("wrong")
    print(x)
if __name__ == "__main__":
    mat_a, mat_b = getInput()
    print("original:")
    print(np.hstack((mat_a, mat_b.T)))
    new_mat = SequentialGauss(np.hstack((mat_a, mat_b.T)))
    print("triangular matrix:")
    print(new_mat)
    print("Answer of 4(a):")
    revert(new_mat)
    