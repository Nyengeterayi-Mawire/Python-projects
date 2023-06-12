import csv

#class called person
class Person: 
    def __init__(self,firstname,lastname,dateofbirth,age,gender,address,city): 
        self.firstname = firstname
        self.lasttname = lastname
        self.dateofbirth = dateofbirth
        self.age = age
        self.gender = gender
        self.address = address
        self.city = city  

    
#doctor class inheriting from peson
class Doctor(Person): 
    #number_of_doctors = 0
    def __init__(self,firstname,lastname,dateofbirth,age,gender,address,city,specialisation,salary): 
        super().__init__(firstname,lastname,dateofbirth,age,gender,address,city)
        self.specialisation = specialisation
        self.salary = salary  
        self.patients = []


    def add_patients(self,patient):
        self.patients.append(patient)

    def show_patients(self): 
        print(self.patients)

#Patient class inheriting from person
class Patient(Person): 
    #number_of_patients = 0 
    def __init__(self,firstname,lastname,dateofbirth,age,gender,address,city,weight,height,insurance_name,insurance_code): 
        super().__init__(firstname,lastname,dateofbirth,age,gender,address,city)
        self.weight = weight
        self.height = height
        self.insurance_name = insurance_name 
        self.insurance_code = insurance_code  
       
#Nurse class inheriting from person
class Nurse(Person):
    #number_of_nurses = 0
    def __init__(self,firstname,lastname,dateofbirth,age,gender,address,city,position,salary):
        super().__init__(firstname,lastname,dateofbirth,age,gender,address,city)
        self.position = position 
        self.salary = salary

#In_Patient class inheriting from patient
class In_Patient(Patient): 
    #number_of_in_patients = 0
    def __init__(self,firstname,lastname,dateofbirth,age,gender,address,city,weight,height,insurance_name,insurance_code,date_of_entry,date_of_discharge): 
        super().__init__(firstname,lastname,dateofbirth,age,gender,address,city,weight,height,insurance_name,insurance_code)
        self.date_of_entry = date_of_entry 
        self.date_of_discharge = date_of_discharge
        self.doctor =  None 
        self.diagnosis = []
        self.medication = []

    def add_doctor(self,doc):
        self.doctor = doc  
#method to add medication to patient 
    def add_diagnosis(self,diagnosis): 
        self.diagnosis.append(diagnosis)

#method to add medication to patient 
    def add_medication(self,medication):
        self.medication.append(medication)

#method to calculate the bill of the patient
    def calculate_bill(self):
        list = []
        total = 0
        meds_tests_list= self.medication
        meds_tests_list.append(self.tests)
        
        #open csv file with list of drugs and the prices
        with open('Drugs.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile,)
            for row in csvreader:
                list.append(row)
        #open csv file with list of test and the prices
        with open('tests.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile,)
            for row in csvreader:
                list.append(row)
        #function to search through the lists of medication and tests to obtain the prices of the medication assigned to patient and prices of diagnosis ran on patient
        def search(word,list):
            new = ''
            for i in list : 
                if i[0]==word:
                    print(f'the price of {word} is {i[1]}')
                    for j in i[1]:
                        if i == '$':
                            pass 
                        else : 
                            new = new + i 
                    return float(new)
                    break                    
                else: 
                    pass
        #loop to iterate list of patients medication and diagnosis to calculate total price
        for i in meds_tests_list:
            search_word=i 
            total = total + search(search_word,list) 
        
        print(f'Your bill comes to a total of : {total}')

class Out_Patient(Patient): 
    number_of_in_patients = 0
    def __init__(self,firstname,lastname,dateofbirth,age,gender,address,city,weight,height,insurance_name,insurance_code,date_of_entry): 
        super().__init__(firstname,lastname,dateofbirth,age,gender,address,city,weight,height,insurance_name,insurance_code)
        self.date_of_entry = date_of_entry 
        self.doctor =  None 
        self.medication = []
        self.diagnosis = []
    #method to add doctor
    def add_doctor(self,doc):
        self.doctor = doc 
    #method to add a diagnosis to patient
    def add_diagnosis(self,diagnosis): 
        self.tests.append(diagnosis)
#method to add medication to patient 
    def add_medication(self,medication):
        self.medication.append(medication)
#method to calculate the bill of the patient
    def calculate_bill(self):
        list = []
        total = 0
        meds_tests_list= self.medication
        meds_tests_list.append(self.tests)
        

        with open('Drugs.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile,)
            for row in csvreader:
                list.append(row)
        
        with open('tests.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile,)
            for row in csvreader:
                list.append(row)
        
        def search(word,list):
            new = ''
            for i in list : 
                if i[0]==word:
                    print(f'the price of {word} is {i[1]}')
                    for j in i[1]:
                        if i == '$':
                            pass 
                        else : 
                            new = new + i 
                    return float(new)
                    break                    
                else: 
                    pass

        for i in meds_tests_list:
            search_word=i 
            total = total + search(search_word,list) 
        
        print(f'Your bill comes to a total of : {total}')

        


a=Person('tim','mawire','10-01-03',20,'M','krakowska 18f','Rzeszow')
print(a.firstname)
