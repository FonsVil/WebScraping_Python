from firebase import firebase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time


db=firebase.FirebaseApplication('https://webscrap-python-default-rtdb.firebaseio.com/')


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
        executable_path="WebScraping_Python\chromedriver.exe", options=options)
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

            data={
                'modelo' : modelo.text,
                'anno' : anno.text,
                'km' : km.text,
                'transmision' : transmision.text,
                'combustible' : combustible.text,
                'traccion' : traccion.text,
                'cilindrado' : cilindrado.text,
                'capacidad' : capacidad.text,
                'precio' : precio.text,
                'img' : img.text,
                'eqBasico1' : eqBasico1.text,
                'eqBasico2' : eqBasico2.text,
                'eqBasico3' : eqBasico3.text,
                'eqBasico4' : eqBasico4.text,
                'confort1' : confort1.text
            }
            
            db.post("/autosUsados",data)



        url = 'https://veinsausados.com/buscar/'
        index += 1

def auto_vendido(object, classname):
    try:
        object.find_element(By.CLASS_NAME, classname)
    except NoSuchElementException:
        return False
    return True

search()
        