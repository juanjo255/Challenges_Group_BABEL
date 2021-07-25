class ParseXsv:
    def __init__(self, file_path) -> None:
        #sep = input ("¿Cuál es el delimitador? ->  ")
        print ("Bienvenido al parseador de Xcsv")
        sep ="\t"
        self.file = open (file_path)
        self.headers = [i [1:-1] for i in self.file.readline ().split (sep)]
        self.body = [i.split(sep) for i in self.file.readlines ()]
    
    def retrieve_fields (self, *args):

        for field in args:
            if field in self.headers:
                print (field)
                index = self.headers.index (field)
                n = 0

                for i in self.body:
                    if n == 5:
                        break
                    n += 1
                    print (i [index])
                    
            else:
                print (f"Este campo no existe {field}")
        return
    
    def sum_fields (self, *args):

        final_sum = 0
        for field in args:
            if field in self.headers:
                print (field, end="\t")
                index = self.headers.index (field)

                for i in self.body:
                    if i [index].isnumeric () :
                        final_sum += float (i [index])
            else:
                print (f"Este campo no existe {field}")
        print ("")
        print (final_sum)
        return
    
    def mean_fields (self, *args):

        final_sum = 0
        total_values = 0
        for field in args:
            if field in self.headers:
                print (field, end="\t")
                index = self.headers.index (field)

                for i in self.body:
                    if i [index].isnumeric () :
                        final_sum += float (i [index])
                    elif i [index].isspace () or not (i [index]) == "N.A." or i[index]:
                        continue
                    total_values += 1
            else:
                print (f"Este campo no existe {field}")
        print ("")
        print (final_sum / total_values)
        return
    
    def count_fields_values (self, *args):
        count = 0
        for field in args:
            if field in self.headers:
                print (field, end="\t")
                index = self.headers.index (field)

                for i in self.body:
                    if not (i [index]) or i [index].isspace ():
                        continue
                    count += 1
            else:
                print (f"Este campo no existe {field}")
        print ("")
        print (count)
        return

file_path = "earthquakes(-2150-2021).tsv"
if __name__ == "__main__":
    ParseXsv (file_path)
