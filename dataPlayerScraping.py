from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrapting():
    # Configurer Selenium pour utiliser Chrome
    options = Options()
    options.headless = True  # pour ne pas ouvrir de fenêtre graphique

    # Lancer Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # URL de la page
    url = "https://steamcommunity.com/market/search?appid=730"
    driver.get(url)

    # Attendre que la page charge (utilise une attente implicite)
    driver.implicitly_wait(5)

    dataToScrap=[]

    try:
        # 1. Identifier le bouton pour afficher les options avancées et cliquer dessus
        advanced_button = driver.find_element(By.ID, 'market_search_advanced_show')
        advanced_button.click()  # Simuler le clic

        time.sleep(2)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[@class="_3PoANvDgGaHNvlIXvT7cEA" and text()="Basculer vers les anciens filtres"]'))
        )
        # Sélectionner le bon span avec XPath
        span_to_click = driver.find_element(By.XPATH,'//span[@class="_3PoANvDgGaHNvlIXvT7cEA" and text()="Basculer vers les anciens filtres"]')
        # Cliquer via JS (plus fiable si l'élément est caché ou stylisé)
        driver.execute_script("arguments[0].click();", span_to_click)



        time.sleep(2)

        # 1. Identifier le bouton pour afficher les options avancées et cliquer dessus
        advanced_button = driver.find_element(By.ID, 'market_search_advanced_show')
        advanced_button.click()  # Simuler le clic

        # 2. Attendre un peu pour que le contenu se mette à jour (si nécessaire)
        # 2. Attendre que le <select> avec le name "category_730_ProPlayer[]" soit visible
        select_tag = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//select[@name="category_730_ProPlayer[]"]'))
        )

        # 3. Trouver toutes les options dans ce select
        options = select_tag.find_elements(By.TAG_NAME, 'option')

        # 4. Afficher toutes les options
        for option in options:

            player=option.text.split("(")
            if len(player)!=1:
                player.pop()
                strToAdd =" ".join(player)
                dataToScrap.append(strToAdd[0:len(strToAdd)-1].lower())

    except Exception as e:
       print("Erreur :", e)

    finally:
        # Fermer le navigateur
        driver.quit()
    return dataToScrap