def densest_protein (fasta, aa_weights):

    suma = 0
    cadena_size = 0
    cadena = ""
    density_anterior = float ("-inf")
    id = fasta.readline ()
    fasta = fasta.readlines ()

    for string in fasta:
        string = string.strip ()

        if string.startswith (">"):

            if (suma / cadena_size) > density_anterior:
                density_anterior = suma / cadena_size
                densest_cadena = cadena
                densest_id = id

            cadena_size = 0
            suma = 0
            cadena = ""
            id = string

        else:
            cadena += string

            for letra in string:
                cadena_size += 1

                if letra in aa_weights:
                    suma += aa_weights [letra]
    
    write_fasta = open ("densest_protein.faa", "w")
    write_fasta.write (densest_id)
    write_fasta.write (" "+str(density_anterior))
    write_fasta.write ("\n")
    write_fasta.write (densest_cadena)
    write_fasta.write ("\n")
        
aa_weights = {"A":89.1, "R":174.2,"N":132.1,"D":133.1,"C":121.2,"E":147.1,"Q":146.2,"G":75.1,"H":155.2,
"I":131.2,"L":131.2,"K":146.2,"M":149.2,"F":165.2,"P":115.1,"S":105.1,"T":119.1,"W":204.2,
"Y":181.2,"V":117.1}
fasta = open ("mg_prots.faa")

densest_protein (fasta, aa_weights)