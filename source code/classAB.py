import csv
import numpy as np
import math

def loadData(path):
    with open(path, "r") as f:
        data = csv.reader(f)
        data = np.array(list(data))

    data = np.delete(data, 0, 0)
    data = np.delete(data, 0, 1)

    np.random.shuffle(data)    
    return data

def loadDataTest(path):
    with open(path, "r") as f:
        data = csv.reader(f)
        data = np.array(list(data))

    data = np.delete(data, 0, 0)
    data = np.delete(data, 0, 1)   
    return data

def distance(trainSet, num1, num2):
    dis_arr = []
    num1 = float(num1)
    num2 = float(num2)
    
    for row in trainSet:
        dis = math.sqrt(math.pow(num1 - float(row[0]), 2) + math.pow(num2 - float(row[1]), 2))
        dis_arr.append((dis, row[2]))

    dis_arr.sort(key=lambda x: x[0])
    return dis_arr

if __name__ == "__main__":
    trainSet = loadData("C:/NHA/AI/data/classAB.csv")
    testSet  = loadDataTest("C:/NHA/AI/data/classAB_test.csv")
    sumT = 0
    k=3
    for test in testSet:
        dis_arr = distance(trainSet, test[0], test[1])
        dis_arr = dis_arr[:k]
        count_A = sum(1 for _, class_label in dis_arr if class_label == 'A')
        count_B = sum(1 for _, class_label in dis_arr if class_label == 'B')
        
        if count_A > count_B :
            print(f"{test[0]} ; {test[1]} --> A")
            if test[-1]== "A":
                sumT+=1
        else:
            print(f"{test[0]} ; {test[1]} --> B")
            if test[-1]=="B":
                sumT+=1
    print("accuracy ",sumT/len(testSet)*100, "%")
