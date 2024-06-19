def ScalarMultiply(xList, exIndex):
    lagDenom = 1
    xi = xList[exIndex]
    for i in range(len(xList)):
        if(i != exIndex):
            lagDenom *= xi - xList[i]
    return lagDenom


def PolyMultiply(rootsList):
    try:
        rootsList = [float(x) for x in rootsList]
        degree = len(rootsList)
        value = [0]*degree
        output = list()
        for i in range(degree):
            for j in range(degree):
                if j == 0:
                    value[j] = value[j] + rootsList[i]
                elif j > 0 and i+j < degree:
                    value[j] = value[j] + value[j-1] * rootsList[i+j]
        output.append(degree)
        output.append(1)
        m=-1
        for i in range(degree):
            output.append(degree-i-1)
            output.append(m*value[i])
            m*=-1
        return output
    except:
        raise Exception("Please enter the roots as specified ")
    
def DOP(polyList):
    for i in range(len(polyList)-1, -1, -1):
        if polyList[i] > 0:
            return i
        else: 
            return -1


def PolyDivide(polys, divisor):
    polysLength = len(polys)
    if(polysLength > 0):
        if polysLength % 2 != 0:
            raise Exception("Please input polynomial in the correct format- exponent followed by coefficient!")
        try:
            degree = int(polys[0])
            polyList = [0]*(degree+1)
            for i in range(int(polysLength/2)):
                polyList[int(polys[2*i])]=float(polys[2*i+1])                    
        except ValueError:
            raise Exception("Exponent can be integer only and coefficient must be a rational number!")
        except:
            raise Exception("Exponents of the polynomial should be supplied in descending order!")
        quotient = dict()
        d = DOP(polyList)

        while d > 0:
            quotient[d-1] = polyList[d]
            polyList[d-1] = polyList[d-1] + quotient[d-1] * float(divisor)
            d -= 1
        return quotient, polyList[0]
            
    else:
        raise Exception("Please input a polynomial in the format- exponent followed by coefficient!")


def LagrangeInterpolation():
    try:
        xyValue = input("Enter X value followed by Y value seperated by space: ")
        xyList = xyValue.strip().split(' ')
        degree = int(len(xyList)/2)
        polyList = [0]*degree
        xList = list()
        yList = list()
        xyIndex = 0
        for item in xyList:
            xList.append(float(item)) if xyIndex%2 == 0 else yList.append(float(item))
            xyIndex += 1
        
        xMultiplyList = PolyMultiply(xList)
        
        for i in range(len(xList)):
            lagNumDict, remain = PolyDivide(xMultiplyList, xList[i])
            for j in range(degree):
                polyList[j] = polyList[j] + yList[i]*lagNumDict[j]/ScalarMultiply(xList, i)
        
        polynomial=""
        for i in range(len(polyList)-1, -1, -1):
            if polyList[i] != 0:
                polynomial += str(polyList[i])+("x" if i== 1 else "x^"+str(i) if i != 0 else "")+("" if polyList[i] >= 0 else "+")
        print(polynomial[:-1])
    except Exception as ex:
        print(ex)

LagrangeInterpolation()