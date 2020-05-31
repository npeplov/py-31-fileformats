# выводить топ 10 самых часто встречающихся в новостях слов
# длиннее 6 символов для каждого файла.
""""
1. Открыть файл newsafr.json
2. Парсером преобразовать строки в словарь
3. Нужен items.description
4. Найти одинаковые слова в списке

   сделать список из списков:
   слово: количество повторений

   for i, word in enumerate(words):
     words[0], word = 'Africa'
     count = words.count(word) // 6
     words[i].pop() // last = 'Africa'
     удалить все элементы Africa из words:
     for ind, del_word in enumerate(words):
       if word in words:
         words.pop(ind)

       my_list.append()
     my_list.append([word, words.count(word)])

   count нельзя потому что можно сравнить только со списком из 2 элементов
   нужно использовать pop

   list.count(x)

   dict.get(key[, default]) -
   возвращает значение ключа, но если его нет возвращает default (по умолчанию None).
"""
import json
import xml.etree.ElementTree as ET


def open_xml_file(file_name):
    parser = ET.XMLParser(encoding="UTF-8")
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    xml_descriptions_list = []
    xml_items = root.findall("channel/item")
    for item in xml_items:
        xml_descriptions_list.append(item.find("description").text)
    return xml_descriptions_list


def open_json_file(file_name):
    with open(file_name, encoding="utf-8") as fi:
        all_file = json.load(fi)
        return all_file


def select_items(items_dict):
    for k, val in items_dict.items():
        items_list = val["channel"]["items"]
        return items_list


def select_descriptions(items_list):
    descriptions_list = []
    for i, item in enumerate(items_list):
        descriptions_list.append(items_list[i]["description"])
    return descriptions_list


def select_words(descriptions_list):
    words_list = []
    for i, val in enumerate(descriptions_list):
        words_of_new = val.split()
        for word in words_of_new:
            if len(word) >= 6:
                words_list.append(word.lower())
    return sorted(words_list)


def counter_of_words(words_list):
    count_words = []
    for i, word in enumerate(words_list):
        count = words_list.count(word)
        count_words.append([count, word])
    i = 0
    count_words.sort(reverse=True)
    return count_words


def del_doubles(count_words):
    i = 0
    while i < len(count_words) - 1:
        # my_list[0] = [42, 'Африки'] = my_list[1]
        if count_words[i] == count_words[i+1]:
            # удаляем элемент my_list[0]
            count_words.pop(i)
            # возврат счетчика элементов к индексу 0
            # первого встреченного значения [42, 'Африки']
            i = count_words.index(count_words[i])
        else:
            # если текущий элемент 0 не равен следующему 1 [42, 'Африки']
            # переходим к след. элементу 1 [40, 'туристов']
            i += 1
    return count_words


def top_ten(input_list):
    ind = 0
    for word in input_list:
        print(ind+1, word)
        ind += 1
        if ind > 9:
            break


if __name__ == '__main__':
    print('JSON')
    json_list = del_doubles(counter_of_words(select_words(select_descriptions(select_items(open_json_file('newsafr.json'))))))
    top_ten(json_list)
    print('XML')
    xml_list = del_doubles(counter_of_words(select_words(open_xml_file('newsafr.xml'))))
    top_ten(xml_list)
