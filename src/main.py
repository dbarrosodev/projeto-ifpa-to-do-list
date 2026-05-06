import flet as ft
from views.home_view import HomeView
from views.register_view import RegisterView
from views.login_view import LoginView
from database.init_db import create_db

def main(page: ft.Page):
    create_db()
    
    page.title = "Sistema de Login"
    page.window.width = 480
    page.window.height = 854

    def route_change():
        page.views.clear()
        
        if page.route == "/":
            pass
        elif page.route == "/register":
            page.views.append(RegisterView())
        elif page.route == "/login":
            page.views.append(LoginView())
        elif page.route == "/home":
            page.views.append(HomeView())
        
        page.update()

    page.on_route_change = route_change
    page.route = "/login"

    route_change()

ft.run(main)
