import time
from multiprocessing import Pool

# Создайте функцию read_info(name), где name - название файла. Функция должна:

def read_info(name):

    # 1. Создавать локальный список all_data.
    all_data = []

    # 2. Открывать файл name для чтения.
    # 3. Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

# Список названий файлов (примерный шаблон, подставьте актуальные имена файлов)
filenames = [f'./file_{i}.txt' for i in range(1, 5)]  # Предполагаем, что файлы называются file_1.txt, file_2.txt, и т.д.

if __name__ == '__main__':
    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print("Линейное выполнение:", end_time - start_time)

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print("Многопроцессное выполнение:", end_time - start_time)

###   Вывод на консоль:
#     Линейное выполнение: 7.1290013790130615
#     Многопроцессное выполнение: 10.354949474334717