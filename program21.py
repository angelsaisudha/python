class MangoBasket:
    def __init__(self):
        self.basket = []
    def add_mango(self,x):
        self.basket.append(x)
    def remove_last_mango(self):
        if self.basket:
            self.basket.pop()
    def get_max_mango(self):
        if self.basket:
            return max(self.basket)
        else:
            return "Empty"
def process_test_case(test_case_number,operations):
    mango_basket = MangoBasket()
    result = []
    for op in operations:
        if op[0] == 'A':
            mango_basket.add_mango(int(op[1]))
        elif op[0] == 'R':
            mango_basket.remove_last_mango() 
        elif op[0] == 'Q':
            result.append(mango_basket.get_max_mango())
    print(f"Case{test_case_number}:")
    for res in result:
        print(res)
T = int(input())
for i in range(T):
    N = int(input())
    operations = [input().split() for _ in range(N)]
    process_test_case(i + 1,operations)