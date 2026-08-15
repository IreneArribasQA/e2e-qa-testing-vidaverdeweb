from playwright.sync_api import Page, expect

from pages.menu_page import MenuPage

def test_visit(page: Page):

    menu_page = MenuPage(page)

    print("Given the user opens the home page")
    page.goto("https://web-qa.dev.adalab.es/")

    print("When they visit the menu “About us”")
    menu_page.click_menu("Quiénes Somos")
    #page.get_by_role("menuitem", name="Quiénes Somos").click()
    print("And they should see the title “About Us”")
    #expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()
    print("Then they should see the URL “https://web-qa.dev.adalab.es/about”")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/about")

    print("When they visit the menu “Products”")
    menu_page.click_menu("Productos")
    #page.get_by_role("link", name="Productos").click()
    print("And they should see the title “Product Catalog”")
    #expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/products”](https://web-qa.dev.adalab.es/products”")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/products")

    print("When they visit the menu “Contact”")
    menu_page.click_menu("Contacto")
    #page.get_by_role("link", name="Contacto").click()
    print("And they should see the title “Contact Us”")
    #expect(page.get_by_role("heading", name="Contáctanos")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/products”](https://web-qa.dev.adalab.es/products”")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/contact")

    print("When they visit the menu “Home”")
    menu_page.click_menu("Inicio")
    #page.get_by_role("link", name="Inicio", exact=True).click()
    print("And they should see the title “Vida Verde”")
    #expect(page.get_by_role("heading", name="Vida Verde")).to_be_visible()
    print("Then they should see the URL “[https://web-qa.dev.adalab.es/”](https://web-qa.dev.adalab.es/”)")
    expect(page).to_have_url("https://web-qa.dev.adalab.es/")