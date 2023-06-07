import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://dex.pokemonshowdown.com/pokemon/")
search_input = browser.find_element_by_class_name("searchbox")

file = open("./pokemon-data/pokemon-ability-data.csv", 'w')
file.write("Pokemon, Ability, Hidden\n")

with open('./names.json') as f:
  pokemon_names = json.loads(f.read())

for name in pokemon_names[0:1068]:
  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  pokemon = name

  abilities = browser.find_elements_by_css_selector("dd.imgentry > a")
  for ability in abilities:

    if ability == abilities[len(abilities)-1] and len(abilities) > 1:
      Hidden = "true"
    else:
      Hidden = "false"

    file.write(pokemon + ","  + ability.text + "," + Hidden + "\n")

browser.close()
file.close()





