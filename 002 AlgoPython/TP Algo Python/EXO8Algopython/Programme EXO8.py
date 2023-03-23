students = []
while True:
    print("Saisissez les informations de l'étudiant:")
    phone = input("Numéro de téléphone: ")
    if len(phone)>=9 and phone[:2] in ["77","78","76","70","75"]:
        name = input("Nom: ")
        first_name = input("Prénom: ")
        class_name = input("Classe: ")
        homework_grade = float(input("Note de devoir: "))
        project_grade = float(input("Note de projet: "))
        exam_grade = float(input("Note d'examen: "))
    
        average = (homework_grade + project_grade + exam_grade) / 3

        students.append({
            "phone": phone,
            "name": name,
            "first_name": first_name,
            "class": class_name,
            "homework_grade": homework_grade,
            "project_grade": project_grade,
            "exam_grade": exam_grade,
            "average": average
        })
    
    answer = input("Voulez-vous saisir les informations pour un autre étudiant? (oui/non) ")
    if answer != "oui":
        break

print("_"*103)
print("Informations des étudiants:")
print("_"*103)
print("|{:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10}|".format(
    "Téléphone", "Nom", "Prénom", "Classe", "Dev", "Proj", "Exam", "Moyenne",
))
print("_"*103)
for student in students:
    print("|{:<10} | {:<10} | {:<10} | {:<10} | {:<10.2f} | {:<10.2f} | {:<10.2f} | {:<10.2f}|".format(
        student["phone"], student["name"], student["first_name"], student["class"],
        student["homework_grade"], student["project_grade"], student["exam_grade"], student["average"]
    ))
    print("_"*103)
