import time
import threading

def sing():
    while True:
        print("我在唱歌，啦啦啦。。。")
        time.sleep(1)

def dance():
    while True:
        print("我在跳舞，呱呱呱。。。")
        time.sleep(1)


if __name__ == '__main__':
    # 创建一个唱歌线程
    sing_thread = threading.Thread(target=sing)

    # 创建一个跳舞线程
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()