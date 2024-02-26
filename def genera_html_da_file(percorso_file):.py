def genera_html_da_file(percorso_file):
    
    with open(percorso_file, 'r') as file:
        
        contenuto_file = file.read()

    
    codice_html = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML Generato</title>
    </head>
    <body>
        <div>
            {contenuto_file}
        </div>
    </body>
    </html>
    """

    
    percorso_html = percorso_file.replace('.csv', '.html')

    
    with open(percorso_html, 'w') as html_file:
        html_file.write(codice_html)

    return codice_html


percorso_file = "/home/studente/Prova_IoT_26Feb2024_Tommaso_Graziani/Fase_1/F1.csv"
codice_html = genera_html_da_file(percorso_file)
print(codice_html)