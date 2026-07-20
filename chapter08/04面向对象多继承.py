class Car:

    def __init__(self, brand, model, color, owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner

    def start(self):
        print(f"{self.brand} {self.model} {self.color} 正在启动...")

    def run(self):
        print(f"{self.__owner} : {self.brand} {self.model} {self.color} 正在行驶...")
        self.__control_fuel()

    def stop(self):
        print(f"{self.__owner} : {self.brand} {self.model} {self.color} 停止行驶...")

    def __control_fuel(self):
        print(f"{self.__owner} : {self.brand} {self.model} {self.color} 正在控制油门")

    def get_owner(self):
        return self.__owner[0:1] + "**"

class HuaweiAiDriving:

    def __init__(self, version="v1.0"):
        self.version = version

    def run(self):
        print(f"使用华为AI智能驾驶系统{self.version}驾驶汽车。。。")

class WenjieCar(Car, HuaweiAiDriving):
    def __init__(self, brand, model, color, owner, version):
        Car.__init__(self, brand, model, color, owner)
        HuaweiAiDriving.__init__(self, version)

if __name__ == "__main__":
    car = WenjieCar("问界", "M9", "白色", "luowei", "v2.0")
    car.run()