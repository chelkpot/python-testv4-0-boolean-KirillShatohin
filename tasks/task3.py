# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    parts = input().split()
    word1 = parts[0]
    word2 = parts[1] if len(parts) > 1 else ""
    print(str(word1 == "awesome" or word2 == "awesome"))

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()