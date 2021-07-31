import sys
class ParseXsv:
    def __init__(self, file_path, sep) -> None:
        #sep = input ("¿Cuál es el delimitador? ->  ")
        print ("Bienvenido al parseador de Xcsv")
        self.file = open (file_path)
        self.headers = [i [1:-1] for i in self.file.readline ().split (sep)]
        self.body = [i.split(sep) for i in self.file.readlines ()]
    
    def retrieve_fields (self, list_args):
        for field in list_args:
            field = field.strip ()
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
    
    def sum_fields (self, list_args):

        final_sum = 0
        for field in list_args:
            field = field.strip ()
            if field in self.headers:
                print (field, end="\t")
                index = self.headers.index (field)

                for i in self.body:
                    try:
                        float (i[index])
                        final_sum += float (i [index])
                    except:
                        continue
            else:
                print (f"Este campo no existe {field}")
        print ("")
        print (final_sum)
        return
    
    def mean_fields (self, list_args):

        final_sum = 0
        total_values = 0
        for field in list_args:
            field = field.strip ()
            if field in self.headers:
                print (field, end="\t")
                index = self.headers.index (field)

                for i in self.body:
                    try:
                        float (i[index])
                        final_sum += float (i [index])
                    except:
                        if i [index].isspace () or not (i [index]) == "N.A." or i[index]:
                            continue
                    total_values += 1
            else:
                print (f"Este campo no existe {field}")
        print ("")
        print (final_sum / total_values)
        return
    
    def count_fields_values (self, list_args):
        count = 0
        for field in list_args:
            field = field.strip ()
            if field in self.headers:
                print (field, end="\t")
                index = self.headers.index (field)

                for i in self.body:
                    if i [index] == "" or i [index].isspace ():
                        continue
                    count += 1
            else:
                print (f"Este campo no existe {field}")
        print ("")
        print (count)
        return

sep = input ("what is the document separator? -> ")
file_path = sys.argv [1]
obj = ParseXsv (file_path, sep)
fn = sys.argv [2]
args = sys.argv [3].split (",")

if fn == "select":
    print ("select")
    obj.retrieve_fields (args)
elif fn == "sum":
    print ("sum")
    obj.sum_fields (args)
elif fn == "mean":
    print ("mean")
    obj.mean_fields (args)
elif fn == "count":
    print ("count")
    obj.count_fields_values (args)
