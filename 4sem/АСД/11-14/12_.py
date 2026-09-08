def kmp(P, T):
    # подготовка префикс-функции
    K = [] # список для преф. ф-ии
    t = -1  # отслеживание длины текущего суффикса, который также является префиксом
    K.append(t) 
    for k in range(1, len(P) + 1):
        while (t >= 0 and P[t] != P[k - 1]):
            t = K[t]
        t = t + 1
        K.append(t)  

    # поиск подстроки
    m = 0 # для смещения
    flag = False
    for i in range(0, len(T)):
        while (m >= 0 and P[m] != T[i]):
            m = K[m]
        m = m + 1 
        if m == len(P): # если подстрока найдена
            print(i - m + 1, i)
            m = K[m]
            flag = True 

    if not flag:
        print(-1)

text = 'Сегодня отличный день!'
find = input('Поиск: ')
if __name__ == "__main__":
    kmp(find, text)
