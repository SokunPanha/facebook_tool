from flet import * 
from flet_route import Params, Basket
class NavBar(UserControl):
    def __init__(self,page: Page, params: Params, basket: Basket):
        self.page = page
    def build(self):
        return View(
            controls=[
                AppBar(
            leading= IconButton(on_click= lambda _: self.page.go(f"/"), icon= icons.ARROW_BACK),
        leading_width=40,
        title=Text("Home"),
        center_title=False,
        bgcolor=colors.GREY_900,
        elevation= 10,
        actions=[
              
        ],
        )
            ]
        )