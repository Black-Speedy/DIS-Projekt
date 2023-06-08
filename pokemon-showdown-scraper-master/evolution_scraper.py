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

for name in pokemon_names[0:1068]:

  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  pokemon = name


  evo = browser.find_elements_by_tag_name("small")
  for elm in evo:
    if "Evolves" in elm.text:
      pre_met = (elm.text).removeprefix("Evolves from ")
      prevolution = (pre_met.split(" (", 1)[0]).replace("é", "e").replace("’", "'")
      method = (pre_met.split(" (", 1)[1]).removesuffix(")")

      file.write(pokemon + "," + prevolution + "," + method + "\n")
      break

browser.close()
file.close()





