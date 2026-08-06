from playwright.sync_api import Page, expect

class MenuPage:
    def __init__(self, page: Page):
        self.page = page

    def visitShoppingCart(self):
         self.page.get_by_role("link", name="Carrito de compra").click()

    def finish_purchase(self):
        self.page.get_by_role("link", name="Finalizar Compra").click( )   

    def click_menu(self, menu_title):
        self.page.set_viewport_size({"width": 400, "height": 824})
        viewport = self.page.viewport_size or {}
        width = viewport.get("width", 0)

        if width <= 400:
            self.page.get_by_role("button", name="Abrir menú principal").click()
            self.page.get_by_role("menuitem", name=menu_title).click()
        else:
            self.page.get_by_role("link", name=menu_title).click()