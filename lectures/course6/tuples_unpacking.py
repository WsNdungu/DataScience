
girl_names = ['JADA', 'Emily', 'Ava', 'SERENITY', 'Claire', 'SOPHIA', 'Sarah', 'ASHLEY', 'CHAYA',      'ABIGAIL', 'Zoe', 'LEAH', 'HAILEY', 'AVA', 'Olivia', 'EMMA', 'CHLOE', 'Sophia', 'AALIYAH', 'Angela', 'Camila', 'Savannah', 'Serenity', 'Chloe', 'Fatoumata', 'ISABELLA', 'MIA', 'FIONA', 'Skylar', 'Ashley', 'Rachel', 'Sofia', 'Alina', 'MADISON', 'RACHEL', 'CAMILA', 'CHANA', 'TAYLOR', 'Kayla', 'Miriam', 'Leah', 'Grace', 'ANGELA', 'Isabella', 'Emma', 'KAYLA', 'SOFIA', 'Madison', 'Aaliyah', 'Taylor', 'GENESIS', 'Esther', 'MAKAYLA', 'Victoria', 'Chaya', 'Brielle', 'Anna', 'Samantha', 'ESTHER', 'GRACE', 'Mariam', 'Mia', 'NEVAEH', 'GABRIELLE', 'EMILY', 'London', 'TIFFANY', 'Chana', 'Valentina', 'OLIVIA', 'LONDON', 'MIRIAM', 'SARAH', 'ELLA']
print(girl_names)


boy_names = ['JOSIAH', 'ETHAN', 'David', 'Jayden', 'MASON', 'RYAN', 'CHRISTIAN', 'ISAIAH', 'JAYDEN',   'Michael', 'NOAH', 'SAMUEL', 'SEBASTIAN', 'Noah', 'Dylan', 'LUCAS', 'JOSHUA', 'ANGEL', 'Jacob', 'Matthew', 'Josiah', 'JACOB', 'Muhammad', 'ALEXANDER', 'Jason', 'Ethan', 'DANIEL', 'Joseph', 'AIDEN', 'Moshe', 'Jeremiah', 'William', 'Alexander', 'Sebastian', 'ERIC', 'MOSHE', 'Jack', 'Eric', 'MUHAMMAD', 'Lucas', 'BENJAMIN', 'Aiden', 'Ryan', 'Liam', 'JASON', 'KEVIN', 'Elijah', 'Angel', 'JAMES', 'Daniel', 'Samuel', 'Amir', 'Mason', 'Joshua', 'ANTHONY', 'JOSEPH', 'Benjamin', 'JUSTIN', 'JEREMIAH', 'MATTHEW', 'Carter', 'James', 'TYLER', 'DAVID', 'JACK', 'ELIJAH', 'MICHAEL', 'CHRISTOPHER']
print(boy_names)


# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))