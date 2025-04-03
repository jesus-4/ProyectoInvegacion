import os
from datetime import datetime 

def autoEvaluaciones(rutaCarpetaEvaluaciones):
    nomCarpetaEvaluaciones= [
        "03_01-Infraestructura equipamiento y biblioteca",
        "03_02-Convenios",
        "03_03-UA-Estructura-Gobierno-Gestion",
        "03_04-Carrera-Estructura-Gobierno-Gestion-PE",
        "03_05-Actividades curriculares",
        "03_06-Estudiantes y Graduados",
        "03_07-Cuerpo academico-Vinculaciones",
        "03_08-Investigacion y tranferencia",
        "03_09-Extension-Vinculacion con el medio",
    ]

    for carpeta in nomCarpetaEvaluaciones:
      os.makedirs(os.path.join(rutaCarpetaEvaluaciones, carpeta))


nombreCarrera= input("Ingrese el nombre de la carrera: ")
nroCiclo= "Ciclo"
nroFase= "Fase"
nombreCarperta= nombreCarrera + "_" + nroCiclo + "_" + nroFase + "_" +str(datetime.now().year)

os.makedirs(nombreCarrera)

subcapertas=["00-Procedimientos e instructivos",
             "01-Convocatoria y formalizacion CONEAU",
             "02-Evaluaciones anteriores CONEAU",
             "03-Autoevaluacion",
             "04-Planes de mejora - desarrollo",
             "05-Resolucion CONEAU",
             "06-Visita de pares",
             "07-Respuesta de visita",
             "08-Recurso de consideracion"]

for carpeta in subcapertas:
    os.makedirs(os.path.join(nombreCarperta, carpeta))
    
    if(carpeta=="03-Autoevaluacion"):
        rutaCarpeta= os.path.join(nombreCarperta,carpeta)
        autoEvaluaciones(rutaCarpeta)
