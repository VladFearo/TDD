"""
Name: Vladislav Shevtsov
ID: 322162553
Name: Omer Halfon
ID: 315429951
"""

# 1st test height and weight are 0:
import math


def test1():
    print("input: (height= 0, weight= 0)")
    print("expected output: False")
    print("actual output:", BMI(0, 0))


"""
the code:
def BMI(weight, height):
    return weight / height ** 2
"""
# test failed error thrown
"""
input: (height= 0, weight= 0)
expected output: False
actual output: error
"""
# refactoring to pass the test
# 1st test after refactoring:
"""
input: (height= 0, weight= 0)
expected output: False
actual output: False
"""
"""
code after reformation:
def BMI(weight, height):
    if weight <= 0 or height <= 0:
        return False
    return weight / height ** 2
"""


# 2nd test input non-numeric strings

def test2():
    print("input: (height= a, weight= b)")
    print("expected output: False")
    print("actual output:", BMI('a', 'b'))


# test failed error thrown
"""
input: (height= a, weight= b)
expected output: False
actual output: error
"""
# refactoring
# 2nd test after refactoring:
"""
input: (height= a, weight= b)
expected output: False
actual output: False
"""
"""
code after refactoring:
def BMI(weight, height):
    try:
        weight, height = float(weight), float(height)
    except ValueError:
        return False
    if weight <= 0 or height <= 0:
        return False
    return weight / height ** 2
"""


# 3rd test input numeric strings:
def test3():
    print("input: (height= 1, weight= 2)")
    print("expected output: 0.25")
    print("actual output:", BMI('1', '2'))


# test pass

# 4th test inputs need to be in normal range weight between 10 and 500 and height between 100 and 300
# testing height > 300
def test4():
    print("input: (height= 4000, weight= 40)")
    print("expected output: False")
    print("actual output:", BMI(height=4000, weight=40))


# test fail
"""
 input: (height= 4000, weight= 40)
expected output: False
actual output: 2.5e-06

"""
# refactoring
"""
4th test after refactoring:
input: (height= 4000, weight= 40)
expected output: False
actual output: False

code after refactoring:
def BMI(weight, height):
    try:
        weight, height = float(weight), float(height)
    except ValueError:
        return False
    if not (1 <= weight <= 300) or not (30 <= height <= 300):
        return False
    return weight / height ** 2
"""


# 5th test inputs need to be in normal range weight between 10 and 500 and height between 100 and 300 testing height<100
def test5():
    print("input: (height= 50, weight= 50)")
    print("expected output: False")
    print("actual output:", BMI(50, 50))


# pass


# 6th test function needs to return BMI and print if its normal overweight or underweight

def test6():
    print("input: (weight= 80, height= 180)")
    print("expected output:\nNormal\n24")
    print("actual output:", BMI(80, 180))


# test fail

"""
test output:
input: (weight= 80, height= 180)
expected output:
Normal
24
actual output: 24.69135802469135
"""

# refactoring
"""
test after refactoring:
input: (weight= 80, height= 180)
expected output:
Normal
24
Normal
actual output: 24


code after refactoring:
def BMI(weight, height):
    try:
        weight, height = float(weight), float(height)
    except ValueError:
        return False
    if not (1 <= weight <= 300) or not (100 <= height <= 300):
        return False
    C_BMI = weight / (height/100) ** 2
    if C_BMI < 18.5:
        print("Underweight")
    elif 18.5 <= C_BMI <= 25:
        print("Normal")
    else:
        print("Overweight")
    return math.floor(C_BMI)
"""


# 7th test bad input trying to input list [1,2]

def test7():
    print("input: (weight= [1,2], height= [1,2])")
    print("expected output: False")
    print("actual output:", BMI([1, 2], [1, 2]))


# Test fail
"""
input: (weight= [1,2], height= [1,2])
expected output: False
actual output: error
"""

# refactoring

"""test after refactoring:
input: (weight= [1,2], height= [1,2])
expected output: False
actual output: False

code after refactoring:
def BMI(weight, height):
    try:
        weight, height = float(weight), float(height)
    except TypeError:
        return False
    except ValueError:
        return False
    if not (1 <= weight <= 300) or not (100 <= height <= 300):
        return False
    C_BMI = weight / (height / 100) ** 2
    if C_BMI < 18.5:
        print("Underweight")
    elif 18.5 <= C_BMI <= 25:
        print("Normal")
    else:
        print("Overweight")
    return math.floor(C_BMI)
"""


# 8th test checking false input {1,2}
def test8():
    print("input: (weight= {1, 2}, height= {1, 2})")
    print("expected output: False")
    print("actual output:", BMI({1, 2}, {1, 2}))


# pass


# 9th test checking input to get Overweight
def test9():
    print("input: (weight= 100, height= 160)")
    print("expected output:\nOverweight\n39")
    print("actual output:")
    print(BMI(100, 160))


# pass

def test10():
    print("input: (weight= 40, height= 160)")
    print("expected output:\nUnderweight\n15")
    print("actual output:")
    print(BMI(40, 160))


# pass


def BMI(weight: float, height: float) -> int:
    """
    A function that calculates a persons BMI
    and prints if the BMI is normal overweight or underweight
    :param weight: float
    :param height: float
    :return: int
    """
    try:
        weight, height = float(weight), float(height)
    except TypeError:
        return False
    except ValueError:
        return False
    if not (1 <= weight <= 300) or not (100 <= height <= 300):
        return False
    c_bmi = weight / (height / 100) ** 2
    if c_bmi < 18.5:
        print("Underweight")
    elif 18.5 <= c_bmi <= 25:
        print("Normal")
    else:
        print("Overweight")
    return math.floor(c_bmi)


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()


if __name__ == '__main__':
    main()
