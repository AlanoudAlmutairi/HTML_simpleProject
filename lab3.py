def MyFirstPage():
  page= pickAFile()
  file =open(page,"wt")
  file.write("""<html>
  <head>

  <title>Alanoud Page </title>
  </head>
  
  <body>
  <h1>Simple Heading </h1>
  <p>Some simple text.</p>
  
  </body>
  </html>""")
  
  file.close()