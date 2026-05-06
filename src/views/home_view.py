import flet as ft
from database.connection import SessionLocal
from models.task_model import Task

class HomeView(ft.View):
    def __init__(self):
        super().__init__(
            ft.Tabs(
                selected_index=0,
                length=3,
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        ft.TabBar(
                            tab_alignment=ft.TabAlignment.CENTER,
                            tabs=[
                                ft.Tab(label="Adicionar", icon=ft.Icons.ADD),
                                ft.Tab(label="Tarefas", icon=ft.Icons.TASK),
                                ft.Tab(label="Perfil", icon=ft.Icons.PERSON),
                            ],
                            indicator_color=ft.Colors.BLACK,
                            label_color=ft.Colors.BLACK
                        ),
                        ft.TabBarView(
                            expand=True,
                            controls=[
                                self.tab_add_task(),
                                self.tab_tasks_list(),
                                ft.Container(
                                    content=ft.Text("Perfil",
                                        color=ft.Colors.BLACK),
                                    alignment=ft.Alignment.CENTER),
                            ]
                        )
                    ]
                )
            ),
            route="/home",
            bgcolor=ft.Colors.WHITE,
        )

    def tab_add_task(self):
        self.txtTitle = ft.TextField(
            label="Título da Tarefa",
            border_color=ft.Colors.GREY_600, 
            color=ft.Colors.GREY_900,
            prefix_icon=ft.Icon(ft.Icons.TASK, color=ft.Colors.GREY_900)
        )
        self.txtDescription = ft.TextField(
            label="Descrição",
            border_color=ft.Colors.GREY_600,
            color=ft.Colors.GREY_900,
            prefix_icon=ft.Icon(ft.Icons.DESCRIPTION, color=ft.Colors.GREY_900),
            multiline=True,
            min_lines=3,
            max_lines=5
        )
        
        return ft.Container(
            content=ft.Column([
                ft.Text("Nova Tarefa:", color=ft.Colors.BLACK, size=18, weight=ft.FontWeight.BOLD),
                self.txtTitle,
                self.txtDescription,
                ft.Button(
                    "Adicionar Tarefa", 
                    on_click=self.add_task,
                    width=200, 
                    height=50,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            alignment=ft.Alignment.CENTER
        )

    def tab_tasks_list(self):
        self.tasks_list = ft.Column()
        self.load_tasks()
        return ft.Container(
            content=ft.Column([
                ft.Text("Minhas Tarefas:", color=ft.Colors.BLACK, size=18, weight=ft.FontWeight.BOLD),
                self.tasks_list
            ], spacing=10),
            padding=20,
            alignment=ft.Alignment.TOP_CENTER,
            expand=True
        )

    async def add_task(self, e):
        title = self.txtTitle.value or ""
        description = self.txtDescription.value or ""
        
        if not title or not description:
            self.page.show_dialog(ft.SnackBar(ft.Text("Preencha título e descrição!")))
            self.page.update()
            return
        
        session = SessionLocal()
        try:
            new_task = Task(title=title, description=description)
            session.add(new_task)
            session.commit()
            
            self.txtTitle.value = ""
            self.txtDescription.value = ""
            
            self.load_tasks()
            
            self.page.show_dialog(ft.SnackBar(ft.Text("Tarefa adicionada com sucesso!")))
            self.page.update()
            
        except Exception as ex:
            self.page.show_dialog(ft.SnackBar(ft.Text("Erro ao adicionar tarefa.")))
            self.page.update()
            print("Erro:", ex)
        finally:
            session.close()

    def load_tasks(self):
        session = SessionLocal()
        try:
            tasks = session.query(Task).all()
            self.tasks_list.controls.clear()
            
            if not tasks:
                self.tasks_list.controls.append(
                    ft.Text("Nenhuma tarefa cadastrada", 
                          color=ft.Colors.GREY_600, 
                          size=16,
                          text_align=ft.TextAlign.CENTER)
                )
            else:
                for task in tasks:
                    task_card = ft.Container(
                        content=ft.Column([
                            ft.Text(task.title, 
                                  size=16, 
                                  weight=ft.FontWeight.BOLD,
                                  color=ft.Colors.BLACK),
                            ft.Text(task.description, 
                                  size=14,
                                  color=ft.Colors.GREY_700),
                            ft.Text(f"ID: {task.id}", 
                                  size=12,
                                  color=ft.Colors.GREY_500)
                        ], spacing=5),
                        padding=15,
                        bgcolor=ft.Colors.GREY_50,
                        border_radius=10,
                        border=ft.BorderSide(1, ft.Colors.GREY_200)
                    )
                    self.tasks_list.controls.append(task_card)
            
            self.tasks_list.update()
        except Exception as ex:
            print("Erro ao carregar tarefas:", ex)
        finally:
            session.close()
