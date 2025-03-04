from tortoise import Tortoise, run_async, BaseDBAsyncClient


async def execute_raw_sql():
    db = Tortoise.get_connection('default')
    users = await db.execute_query('select * from user')
    print(users)

async def init():
    await Tortoise.init(
        db_url='mysql://root:123456@localhost:4406/orm_demo',
        modules={'models': ['tortoise_demo.model_define']},
    )

    await execute_raw_sql()

if __name__ == "__main__":
    run_async(init())