def NOT(IN1):
    return not IN1
def NAND(IN1, IN2):
    return NOT( IN1 and IN2 )
def AND(IN1, IN2):
    return NAND(NAND(IN1, IN2), True)
def OR(IN1, IN2):
    return NAND(NAND(IN2, IN2), NAND(IN1, IN1))

print (OR(0, 0))
