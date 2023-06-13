# version#2 - 메뉴 1을 선택할 시 파일을 읽어와 문자열 리스트를 객체 리스트로 변환 및 출력 구현 / 메뉴 4를 선택할 시 프로그램 종료 및 Exit 출력 구현
# version#3 - 메뉴 2를 선택할 시 선택한 유형에 따라 해당 필터링을 실행하는 함수 구현
# version#4 - 메뉴 3을 선택할 시 정렬을 희망하는 항목에 따라 정렬하는 함수 구현
import parking_spot_manager
import file_manager


def start_process(path):
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        # 1번 메뉴 선택시 출력
        if select == 1:
            parking_spot_manager.print_spots(spots)
        # 2번 메뉴 선택시 필터링 기능 실행
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            # 1번 선택시 이름으로 필터링
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
            # 2번 선택시 도시명으로 필터링
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            # 3번 선택시 시군구로 필터링
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            # 4번 선택시 주차장 유형으로 필터링
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            # 5번 선택시 위치 정보로 필터링
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots, locations)
            else:
                print("invalid input")
        # 3번 메뉴 선택시 정렬 기능 실행
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sorted_by_keyword(spots, keyword)
            else:
                print("invalid input")
        # 4번 메뉴 선택시 Exit을 출력하고 프로그램 종료
        elif select == 4:
            print("Exit")
            return
        else:
            print("invalid input")
