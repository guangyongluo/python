from pydantic import BaseModel, ValidationError

class LoginForm(BaseModel):
    username: str
    password: str

class RegisterForm(BaseModel):
    username: str
    password: str
    confile_password: str
    email: str = None
    phone: str = None

def login(login_form: LoginForm):
    try:
        data = login_form.model_dump()
        print(data)
    except ValidationError as e:
        return e.errors()

def register(register_form: RegisterForm):
    try:
        data = register_form.model_dump(exclude_unset=True)
        print(data)
    except ValidationError as e:
        return e.errors()


if __name__ == '__main__':
    # login_form = LoginForm(username="Tom", password="123456")
    # login(login_form)

    register_form = RegisterForm(username="Tom", password="123456", confile_password="123456")
    register(register_form)
