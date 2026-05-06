import flet as ft
from database.connection import SessionLocal
from models.user_model import User

class LoginView(ft.View):
    def __init__(self):
        super().__init__(route="/login", bgcolor=ft.Colors.WHITE)

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.txtEmail = ft.TextField(
            border_color=ft.Colors.GREY_600,
            color=ft.Colors.GREY_900,
            prefix_icon=ft.Icon(
                ft.Icons.EMAIL,
                color=ft.Colors.GREY_900
            )
        )
        self.txtPassword = ft.TextField(
            border_color=ft.Colors.GREY_600,
            color=ft.Colors.GREY_900,
            prefix_icon=ft.Icon(
                ft.Icons.LOCK,
                color=ft.Colors.GREY_900
            ),
            password=True,
            can_reveal_password=True
        )

        self.controls = [
            ft.CircleAvatar(content=ft.Icon(icon=ft.Icons.PERSON, color=ft.Colors.WHITE, size=100), width=150, height=150),

            ft.Text("Bem-vindo(a), usuário, faça login no sistema", color=ft.Colors.BLACK, size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),

            ft.Text("E-mail:", color=ft.Colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
            self.txtEmail,

            ft.Text("Senha:", color=ft.Colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
            self.txtPassword,

            ft.Button("Login", on_click=self.login_user, width=150, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)), color=ft.Colors.WHITE),

            ft.Button("Cadastrar-se", on_click=self.go_to_register_view, width=150, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)), color=ft.Colors.WHITE)
        ]

    async def login_user(self, e):
        email = self.txtEmail.value or ""
        password = self.txtPassword.value or ""

        if not email or not password:
            self.page.show_dialog(ft.SnackBar(ft.Text("Por favor, preencha todos os campos.")))
            self.page.update()
            return
        
        session = SessionLocal()
        try:
            user = session.query(User).filter(User.email == email, User.password == password).first()

            if user:
                await self.go_to_home_view(e)
            else:
                self.page.show_dialog(ft.SnackBar(ft.Text("Email ou senha incorretos.")))
                self.page.update()

        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text("Erro ao realizar login.")))
            self.page.update()
            print("Erro login:", ex)
        finally:
            session.close()


    async def go_to_home_view(self, e):
        await self.page.push_route("/home")

    async def go_to_register_view(self):
        await self.page.push_route("/register")