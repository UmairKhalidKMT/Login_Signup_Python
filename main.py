from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10

        self.username_label = Label(text="Username:")
        self.add_widget(self.username_label)
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_input)

        self.password_label = Label(text="Password:")
        self.add_widget(self.password_label)
        self.password_input = TextInput(password=True, multiline=False)
        self.add_widget(self.password_input)

        self.login_button = Button(text="Login")
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        # Add your login logic here
        username = self.username_input.text
        password = self.password_input.text
        # Implement your authentication logic

        print(f"Username: {username}")
        print(f"Password: {password}")


class SignUpScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10

        self.username_label = Label(text="Username:")
        self.add_widget(self.username_label)
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_input)

        self.password_label = Label(text="Password:")
        self.add_widget(self.password_label)
        self.password_input = TextInput(password=True, multiline=False)
        self.add_widget(self.password_input)

        self.signup_button = Button(text="Sign Up")
        self.signup_button.bind(on_press=self.signup)
        self.add_widget(self.signup_button)

    def signup(self, instance):
        # Add your sign-up logic here
        username = self.username_input.text
        password = self.password_input.text
        # Implement your sign-up logic

        print(f"Username: {username}")
        print(f"Password: {password}")


class MyApp(App):
    def build(self):
        login_screen = LoginScreen()
        signup_screen = SignUpScreen()

        root = BoxLayout(orientation="vertical")
        root.add_widget(login_screen)
        root.add_widget(signup_screen)

        return root


if __name__ == "__main__":
    MyApp().run()
