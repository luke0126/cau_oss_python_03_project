# version#2 - parking_spot 생성자 및 get 메서드 구현 / 파일을 읽어와 문자열 리스트를 객체 리스트로 변환 후 출력 구현

# parking_spot 클래스
class parking_spot:
    # 객체의 정보를 출력하는 메서드
    def __str__(self):
        item = self.__item
        s = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    # 생성자
    def __init__(self, name, city, district, ptype, longitude: float, latitude: float):
        self.__item = dict()
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = longitude
        self.__item['latitude'] = latitude

    # 매개변수 keyword를 입력받고 __item[keyword] 값을 반환하는 메서드
    def get(self, keyword):
        return self.__item[keyword]


# 문자열 리스트를 입력 받아 객체 리스트로 반환하는 메서드
def str_list_to_class_list(str_list):
    res = list()
    for info in str_list:
        temp = info.split(',')
        place_info = parking_spot(temp[1], temp[2], temp[3], temp[4], temp[5], temp[6])
        res.append(place_info)
    return res


# 객체 리스트를 입력받아 하나씩 출력하는 메서드
def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for i in spots:
        print(i)


# 이름으로 필터링하여 새로운 객체 리스트를 반환하는 메서드
def filter_by_name(spots, name):
    res = list()
    for spot in spots:
        if name in spot.get('name'):
            res.append(spot)
    return res


# 도시명으로 필터링하여 새로운 객체 리스트를 반환하는 메서드
def filter_by_city(spots, city):
    res = list()
    for spot in spots:
        if city in spot.get('city'):
            res.append(spot)
    return res


# 시군구로 필터링하여 새로운 객체 리스트를 반환하는 메서드
def filter_by_district(spots, district):
    res = list()
    for spot in spots:
        if district in spot.get('district'):
            res.append(spot)
    return res


# 주차장 유형 필터링하여 새로운 객체 리스트를 반환하는 메서드
def filter_by_ptype(spots, ptype):
    res = list()
    for spot in spots:
        if ptype in spot.get('ptype'):
            res.append(spot)
    return res


# 위치 필터링하여 새로운 객체 리스트를 반환하는 메서드
def filter_by_location(spots, locations):
    res = list()
    for spot in spots:
        if locations[0] < float(spot.get('latitude')) < locations[1] and locations[2] < float(spot.get('longitude')) < locations[3]:
            res.append(spot)
    return res


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)

if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)

    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
