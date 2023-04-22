import utils
import read_csv
import charts
import pandas as pd
#con el run ejecutamos el arhivo como un script
#si utilizamos pandas, ya nos lee y filtra columnas y filas del csv sin
#tener que escribir la lógica nosotros.
def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
    '''
  df = pd.read_csv('data.csv')  #con este paso nos ahorramos todo el archivo
  # de reac_csv que hemos creado aparte
  df = df[df ['Continent'] == 'South America'] #esta línea es igual a la primerea comentada arriba

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'],labels, values)
    
  

if __name__ == '__main__':
  run()

#este if, le dice a main que si es ejecutado desde la terminal, puedes ejecutar el método run,
#pero si es ejecutado desde otro archivo no se va a ejecutar