from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


file_path = "file:///C:/Users/ELJOS/Documents/restapi/frontend/index.html"
# Configuración del navegador
driver = webdriver.Chrome() 
driver.get(file_path)

def test_agregar_cliente():
    

    agregar_button = driver.find_element(By.ID, "show-form-btn")
    agregar_button.click()
    time.sleep(2)


    driver.find_element(By.ID, "nombre").send_keys("Juan Pérez")
    driver.find_element(By.ID, "telefono").send_keys("123456789")
    driver.find_element(By.ID, "calle").send_keys("Calle Falsa")
    driver.find_element(By.ID, "numero").send_keys("123")
    driver.find_element(By.ID, "sector").send_keys("Centro")
    descuento_checkbox = driver.find_element(By.ID, "descuentoBool")
    descuento_checkbox.click()

    agregar_cliente_button = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
    agregar_cliente_button.click()
    time.sleep(2)

    tabla = driver.find_element(By.ID, "clientes-table")
    assert "Juan Pérez" in tabla.text, "El cliente no se agregó correctamente."

def test_editar_cliente():

    editar_button = driver.find_element(By.XPATH, "//button[contains(text(),'Editar')]")
    editar_button.click()
    time.sleep(2)


    nombre_field = driver.find_element(By.ID, "nombre")
    nombre_field.clear()
    nombre_field.send_keys("Carlos Gómez")

    telefono_field = driver.find_element(By.ID, "telefono")
    telefono_field.clear()
    telefono_field.send_keys("987654321")

  
    guardar_cambios_button = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm")
    guardar_cambios_button.click()
    time.sleep(2)


    tabla = driver.find_element(By.ID, "clientes-table")
    assert "Carlos Gómez" in tabla.text, "El cliente no se actualizó correctamente."

# Ejecutar las pruebas
try:
    test_agregar_cliente()
    print("Prueba de agregar cliente exitosa.")
    test_editar_cliente()
    print("Prueba de editar cliente exitosa.")
finally:
    driver.quit()
