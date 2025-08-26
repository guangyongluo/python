import time
import asyncio
from functools import wraps

def async_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}耗时{end - start}秒")
        return result
    return wrapper

@async_time
async def main():
    print("开始执行任务")
    await asyncio.sleep(2)  # 模拟异步任务
    print("任务执行完毕")

if __name__ == "__main__":
    asyncio.run(main())