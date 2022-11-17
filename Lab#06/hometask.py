class PC:
    def __init__(self) -> None:
        self._details = {}

    def displayDetails(self):
        return self._details

class Asus(PC):
    def __init__(self):
        self._details = {
            "name":"asus",
            "specs":{
                "processor":"Ryzen 5",
                "ram":8,
                "hdd":500,
                "sdd":256,
                "graphics":"asus 750ti"
            },
            "price":580
        }

class HP(PC):
    def __init__(self):
        self._details = {
            "name":"hp",
            "specs":{
                "processor":"Core i5",
                "ram":8,
                "hdd":500,
                "sdd":256,
                "graphics":"nvidia 1080ti"
            },
            "price":680
        }

class Dell(PC):
    def __init__(self):
        self._details = {
            "name":"dell",
            "specs":{
                "processor":"Core i7",
                "ram":16,
                "hdd":256,
                "sdd":256,
                "graphics":"nvidia 3090ti"
            },
            "price":920
        }

class PC_Factory(object):
    @staticmethod
    def pc_details(name):
        objs = {
            'asus':Asus(),
            'hp':HP(),
            'dell':Dell()
        }
        for key,value in objs.items():
            if key==name:
                return value


if __name__=="__main__":
    for each in ['asus','hp','dell']:
        print(f'PC Detail : {PC_Factory.pc_details(each).displayDetails()}')