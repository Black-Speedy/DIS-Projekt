import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://dex.pokemonshowdown.com/pokemon/")
search_input = browser.find_element_by_class_name("searchbox")

file = open("./pokemon-data/pokemon-evolution-data.csv", 'w')
file.write("Pokemon, Pre-evolution, Method \n")

with open('./names.json') as f:
  pokemon_names = json.loads(f.read())

for name in pokemon_names[0:15]:

  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  pokemon = name


  evo = browser.find_element_by_xpath("// div[contains(text(),\
   'Evolves from')]").click()
  print(evo[0].text + "\n")

  #file.write(pokemon + "," + number + "," + height + "," + weight + "," + hp + "," 
   # + attack + "," + defense + "," + special_atk 
   # + "," + special_def + "," + speed + "," + total + "," + sprite 
   # + "\n")

browser.close()
file.close()





