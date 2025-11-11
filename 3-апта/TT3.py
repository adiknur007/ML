#Student aty men bagasy
student = {
    "Adil": [50,60,70,80,90],
    "Asyl": [51,61,71,81,91],
    "Aidyn": [52,62,72,82,92],
    "Askar": [53,63,73,83,93],
    "Aslan": [54,64,74,84,94],
    "Aizhang": [55,65,75,85,90]
}
jogary_baga = {name: max(scores) for name, scores in student.items()}
print (jogary_baga)