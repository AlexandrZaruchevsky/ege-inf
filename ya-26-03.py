# Данная задача сводится к отбору из основного списка таких деталей, для которых
# время шлифовки меньше времени окраски. Далее необходимо отсортировать
# полученный список по времени шлифовки.

# Класс для описания детали, где id номер строки в исходном файле,
# shlif - время шлифовки, okras - время окраса
class Detal:
  # Описываем конструктор класса
  def __init__(self, d_id: int, shlif: int, okras: int):
    self.d_id = d_id
    self.shlif = shlif
    self.okras = okras

  # Переопределяем метод для вывода информации для класса
  # Необходим для визуального контроля за сформированным списком
  def __str__(self):
    return "id[{}]: -> {} {}".format(self.d_id, self.shlif, self.okras)


with open('data/26-03.txt', 'r') as file:
  # Считываем исходные данные
  source_list = file.readlines()
  # Создаем список деталей
  shlif_list: list[Detal] = list()
  for i in range(1, len(source_list)):
    # Из строки получаем время шлифовки и кораски
    (shl, okr) = list(map(int, source_list[i].split()))
    # Сравниваем время шлифовки и окраски
    # и если время шлифовки меньше времени окраски - добавляем в список shlif_list
    if shl <= okr:
      shlif_list.append(Detal(i, shl, okr))
  #  Смотрим, не пустой ли список
  print('shl -> ', len(shlif_list))
  # Создаем новый список на основе shlif_list, сортируя по времени шлифовки по возрастанию
  s_l = [*sorted(shlif_list, key=lambda o: o.shlif, reverse=False)]
  # Выводим полученный список деталей
  # В ответе указываем id последнего элемента и количество деталей до него
  for i in range(len(s_l)):
    print(i + 1, ' -> ', s_l[i])

file.close()
