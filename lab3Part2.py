def MyFirstPage():
  page= pickAFile()
  file =open(page,"wt")
  file.write("""<html>
  
  <head>
  <title>Alanoud Page </title>
  </head>
  
  <body>
  <h1>Students grades </h1>
 
  <table border ="9">
  <tr>
  <th>Student Name</th>
  <th>Total</th>
  <th>Grades<th>
  </tr>
  
  <tr>
  <td>Ahmad</td>
  <td>90</td>
  <td>A+</td>
  </tr>
  
  <tr>
  <td>Ali</td>
  <td>94</td>
  <td>A+</td>
  </tr>
  </table>
  <br>
  <tt><b>Instractor :</b></tt>
  <ul>
  <li>Dr Waleed </li>
  <li>Dr Osama </li>
  </lu>
  <br>
  <img src="images.jpg">
  
  </body>
  </html>""")
  
  file.close()