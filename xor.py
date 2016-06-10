def sgn (x1,x2,w1,w2,theta):

	diff = (w1*x1 + w2*x2)-theta
	if diff > 0 :
		return 1.0
	else :
		return 0.0

def not_or(x1,x2):
	w1 = float(-1.0)
	w2 = float(-1.0)
	theta = float(-0.1)
	return sgn(x1,x2,w1,w2,theta)


def logical_and(x1,x2):
	w1 = float(1.0)
	w2 = float(1.0)
	theta = float(1.9)
	return sgn(x1,x2,w1,w2,theta)

def  logical_or(x1,x2):
	w1 = float(0.5)
	w2 = float(0.5)
	theta = float(0.4)
	return sgn(x1,x2,w1,w2,theta)


x1 = float(input("Enter x1 : "))
x2 = float(input("Enter x2 : "))
nor = not_or(x1,x2)
da = logical_and(x1,x2)

result = logical_or(nor,da)
print("Result Is : ", result)

