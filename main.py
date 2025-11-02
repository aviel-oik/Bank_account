from classes.BankAccount import BankAccount


A_1 = BankAccount("aviel", 100)
A_2 = BankAccount("yoav",50)

A_1.__str__()
A_2.__str__()

A_1.transfer_funds(A_2, 10)

A_1.__str__()
A_2.__str__()