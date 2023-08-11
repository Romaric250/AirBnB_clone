import json

class FileStorage:
    __file_path = "file.json"#path to the json file
    __objects = {} # dic to store serialised objects


    def all(self):
        return self.__objects #returns all obj in the dic
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        #the above line generate a unique key for the obj
        self.__objects[key] = obj #adds obj to dict

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key]= obj.to_dict()
            #serialize each obj to a dict

        with open(self.__file_path,'w') as file:
            json.dump(serialized_objects,file)
            #writes the serialized obj to json

    def reload(self):
        try:
            with open(self.__file_path,'r') as file:
                serialised_objects = json.load(file)
                #load obj from json
                for key, obj_dict in serialised_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    #gets the class from the obj objects ey

                    obj = obj_class(**obj_dict)
                    #deserialisation
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    

