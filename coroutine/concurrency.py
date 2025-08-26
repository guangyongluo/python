import asyncio
from coroutine import async_time


async def greet(name, delay):
    await asyncio.sleep(delay)  # 模拟异步延迟
    return f"Hello, {name}!"

async def greet_with_error(name, delay):
    await asyncio.sleep(delay)  # 模拟异步延迟
    if name == "Bob":
        raise ValueError("An error occurred!")
    return f"Hello, {name}!"

@async_time
async def main1():
    result1 = await greet("Alice", 1)
    result2 = await greet("Bob", 2)

    print(result1)
    print(result2)

@async_time
async def main2():
    task1 = asyncio.create_task(greet("Alice", 1))
    task2 = asyncio.create_task(greet("Bob", 2))

    result1 = await task1
    result2 = await task2
    print(result1)
    print(result2)

@async_time
async def main3():
    results = await asyncio.gather(
        greet("Alice", 1),
        greet("Bob", 2),
        greet("Charlie", 3)
    )
    print(results)

@async_time
async def main4():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(greet_with_error("Alice", 1))
            task2 = tg.create_task(greet_with_error("Bob", 2))
            task3 = tg.create_task(greet_with_error("Charlie", 3))
    except Exception as e:
        print(e)

    print(task1.result())
    print(task2.result())
    print(task3.result())


@async_time
async def main5():
    try:
        results = await asyncio.gather(
            greet_with_error("Alice", 3),
            greet_with_error("Bob", 2),
            greet_with_error("Charlie", 3),
            greet_with_error("David", 4),
            greet_with_error("Eve", 5),
            # return_exceptions=True
        )
        print(results)
    except Exception as e:
        print(e)
    for task in asyncio.all_tasks():
        if task.get_name() == 'Task-1':
            continue
        result = await task
        print(result)

if __name__ == "__main__":
    asyncio.run(main5())