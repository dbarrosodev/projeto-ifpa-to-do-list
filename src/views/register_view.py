import flet as ft
from database.connection import SessionLocal
from models.user_model import User

class RegisterView(ft.View):
    def __init__(self):
        super().__init__(route="/register", bgcolor=ft.Colors.WHITE)

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.txtName = ft.TextField(border_color=ft.Colors.GREY_600, color=ft.Colors.GREY_900, prefix_icon=ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREY_900))
        self.txtEmail = ft.TextField(border_color=ft.Colors.GREY_600, color=ft.Colors.GREY_900, prefix_icon=ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREY_900))
        self.txtPassword = ft.TextField(border_color=ft.Colors.GREY_600, color=ft.Colors.GREY_900, prefix_icon=ft.Icon(ft.Icons.LOCK, color=ft.Colors.GREY_900), password=True, can_reveal_password=True)
        self.txtConfirmPassword = ft.TextField(border_color=ft.Colors.GREY_600, color=ft.Colors.GREY_900, prefix_icon=ft.Icon(ft.Icons.LOCK, color=ft.Colors.GREY_900), password=True, can_reveal_password=True)

        self.controls = [
            ft.CircleAvatar(content=ft.Icon(icon=ft.Icons.PERSON, color=ft.Colors.WHITE, size=100), width=150, height=150),  
            ft.Text("Bem-vindo(a), usuário, faça seu cadastro no sistema", color=ft.Colors.BLACK, size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            
            ft.Text("Nome completo:", color=ft.Colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
            self.txtName,

            ft.Text("E-mail:", color=ft.Colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
            self.txtEmail,

            ft.Text("Senha:", color=ft.Colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
            self.txtPassword,
            
            ft.Text("ConfirmarSenha:", color=ft.Colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
            self.txtConfirmPassword,

            ft.Button("Cadastrar", on_click=self.register_user, width=150, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)), color=ft.Colors.WHITE),

            ft.Button("Possuo Login", on_click=self.go_to_login_view, width=150, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)), color=ft.Colors.WHITE)
        ]

    async def register_user(self, e):
        name = self.txtName.value or ""
        email = self.txtEmail.value or ""
        password = self.txtPassword.value or ""
        confirm_password = self.txtConfirmPassword.value or ""

        if not name or not email or not password:
            self.page.show_dialog(ft.SnackBar(ft.Text("Por favor, preencha todos os campos.")))
            self.page.update()
            return
        
        if password != confirm_password:
            self.page.show_dialog(ft.SnackBar(ft.Text("As senhas digitadas devem ser iguais.")))
            self.page.update()
            return

        session = SessionLocal()
        try:
            existing_user = session.query(User).filter(User.email == email).first()
            if existing_user:
                self.page.show_dialog(ft.SnackBar(ft.Text("Este email já está cadastrado!")))
                self.page.update()
                session.close()
                return

            new_user = User(name=name, email=email, password=password)
            session.add(new_user)
            session.commit()
            
            await self.go_to_login_view(e)

        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text("Erro no sistema.")))
            self.page.update()
            print("Erro:", ex)
        finally:
            session.close()

    async def go_to_login_view(self, e):
        await self.page.push_route("/login")