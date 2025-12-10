# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input().split())
    print(a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()