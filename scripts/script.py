cities = {'Diésel': 0, 'Eléctrico': 1, 'Gas licuado (GLP)': 2, 'Gas natural (CNG)': 3, 'Gasolina': 4, 'Híbrido': 5, 'Híbrido enchufable': 6}

for city, value in cities.items():
    print('<option value="{}">{}</option>'.format(city, city))
