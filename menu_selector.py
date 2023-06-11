# version#2 - 메뉴 1 을 선택할 시 파일을 읽어와 문자열 리스트를 객체 리스트로 변환 및 출력 구현 / 메뉴 4를 선택할 시 프로그램 종료 및 Exit 출력 구현
import parking_spot_manager


def start_process(path):
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            import file_manager
            str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
            spots = parking_spot_manager.str_list_to_class_list(str_list)
            parking_spot_manager.print_spots(spots)
            # fill this block
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            return
            # fill this block
        else:
            print("invalid input")