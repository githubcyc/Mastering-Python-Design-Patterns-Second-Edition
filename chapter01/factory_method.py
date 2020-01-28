"""
Factory Method(工厂方法)：执行单独的函数，通过传参提供需要的对象的信息。
"""
import json
import xml.etree.ElementTree as etree

class DataExtractor:
    def __init__(self, filepath):
        self.filepath = filepath
    
    @property
    def parsed_data(self):
        pass


class JSONDataExtractor(DataExtractor):

    def __init__(self, filepath, **kwargs):
        super().__init__(filepath)
        print(kwargs)
        print(f"super's parsed_data: {super().parsed_data}")

    @property
    def parsed_data(self):
        data = dict()
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data


class XMLDataExtractor(DataExtractor):

    @property
    def parsed_data(self):
        tree = etree.parse(self.filepath)
        return tree


def data_extraction_factory(filepath):
    """
    return: DataExtractor class
    """
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    sqlite_factory = extract_data_from('data/person.sq3')
    print()

    json_factory = extract_data_from('data/movies.json')
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['director']
        if director:
            print(f"Director: {director}")
        genre = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()

    xml_factory = extract_data_from('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f'found: {len(liars)} persons')
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text) 
              for p in liar.find('phoneNumbers')]
        print()
    print()


if __name__ == '__main__':
    main()
