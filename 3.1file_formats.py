# выводить топ 10 самых часто встречающихся в новостях слов
# длиннее 6 символов для каждого файла.

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


# список всех слов с дублями, одинаковые идут друг за другом
def select_words(descriptions_list):
    words_list = []
    for i, val in enumerate(descriptions_list):
        words_of_new = val.split()
        for word in words_of_new:
            if len(word) >= 6:
                words_list.append(word.lower())
    return sorted(words_list)


# на входе список слов с дублями words_list
def counter_of_words(words_list):
    # одинаковые идут друг за другом: [advance, advance, africa, africa...]
    # создаем словарь
    count_words_dict = {}
    # идем по элементам списка
    for word in words_list:
        # считаем количество повторений:
        count = words_list.count(word)
        # словарь {слово: число}, одинаковые ключи не добавятся
        count_words_dict[word] = count
    # получили словарь {'advance': 2} и тд
    # сортируем по значениям item[1]
    return sorted(count_words_dict.items(), key=lambda item: item[1], reverse=True)


def top_ten(input_list):
    ind = 0
    for word in input_list:
        print(ind+1, word)
        ind += 1
        if ind > 9:
            break


if __name__ == '__main__':
    print('JSON')
    top_ten(counter_of_words(select_words(select_descriptions(select_items(open_json_file('newsafr.json'))))))
    print('XML')
    top_ten(counter_of_words(select_words(open_xml_file('newsafr.xml'))))