from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time

link_detalles = []

# Search game in Amazon
def search():
    url = 'https://veinsausados.com/buscar/'

    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        executable_path="./chromedriver", options=options)
    driver.get(url)

    time.sleep(3)

    # Cantidad de páginas
    paginacion = driver.find_elements(By.CLASS_NAME, 'search-box__page-number')
    
    # Navegar entre páginas
    index = 1
    while index <= len(paginacion):
        link_detalles = []
        url = url + '?pagina=' + str(index)
        driver.get(url)

        autos = driver.find_elements(By.CLASS_NAME, 'random-vehicles__vehicle')
        for auto in autos:
            if(auto_vendido(auto, 'random-vehicles__sold') == False):
                link = auto.find_element(By.CLASS_NAME, 'random-vehicles__vehicle-link').get_attribute("href")
                link_detalles.append(link)

        for link in link_detalles:
            driver.get(link)

            modelo = driver.find_element(By.XPATH, '/html/body/form/div/div/div[1]/div[1]/div[1]/h1')
            anno = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[2]/div[1]') 
            km = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[2]/div[2]')
            transmision = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[2]/div[3]')
            combustible = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[2]/div[4]')
            traccion = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[2]/div[5]')
            cilindrado = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[2]/div[6]')
            capacidad = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[2]/div[7]')
            precio = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[1]/div[3]/div[1]')
            img = driver.find_element(By.XPATH,'/html/body/form/div/div/div[1]/div[3]/div/div/div[2]/img')
            eqBasico1 = driver.find_element(By.XPATH,'/html/body/form/div/div/div[2]/div[1]/div/div/div/div/li[1]')
            eqBasico2 = driver.find_element(By.XPATH,'/html/body/form/div/div/div[2]/div[1]/div/div/div/div/li[2]')
            eqBasico3 = driver.find_element(By.XPATH,'/html/body/form/div/div/div[2]/div[1]/div/div/div/div/li[3]')
            eqBasico4 = driver.find_element(By.XPATH,'/html/body/form/div/div/div[2]/div[1]/div/div/div/div/li[4]')
            confort1 = driver.find_element(By.XPATH,'/html/body/form/div/div/div[2]/div[1]/div/div/div/div/li[5]')
            confort2 = driver.find_element(By.XPATH,'/html/body/form/div/div/div[2]/div[1]/div/div/div/div/li[6]')
            
            print('\nModelo de auto: '+modelo.text+'\nAño del auto: '+anno.text+'\ntipo de combustible: '+combustible.text+'\nKilometraje del Vehiculo: '+km.text+'\nTipo de transmisión:'+transmision.text
            +'\nTipo de tracción: '+traccion.text+'\nCilindrado: '+cilindrado.text+'\nCapacidad de personas: '+capacidad.text+'\nPrecio regular: '+precio.text+'\nExtras: '+eqBasico1.text+'\n'+eqBasico2.text
            +'\n'+eqBasico3.text+'\n'+eqBasico4.text+'\n'+confort1.text+'\n'+confort2.text+'\nImagen: '+img)



        url = 'https://veinsausados.com/buscar/'
        index += 1

def auto_vendido(object, classname):
    try:
        object.find_element(By.CLASS_NAME, classname)
    except NoSuchElementException:
        return False
    return True

search()
        