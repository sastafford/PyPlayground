'''
Created on Jan 24, 2011

@author: sstafford
'''

import csv
import xml.dom.minidom

def addElement(element, elemName, dictKey):
    element.appendChild(doc.createElement(elemName)).appendChild(doc.createTextNode(record[dictKey].strip()))

def write_to_file(doc, name="person.xml"):
    file_object = open(name, "w")
    doc.writexml(file_object)
    file_object.close()

reader = csv.DictReader(open('random-names.txt', 'r'), delimiter='|')
for record in reader:
    #record = (reader.__next__())
    doc = xml.dom.minidom.Document()
    person_element = doc.createElementNS("http://www.marklogic.com/random", "fake-person")
    doc.appendChild(doc.createComment("THIS DATA IS FAKE AND IS NOT REAL!!  FOR EXAMPLE PURPOSES ONLY!!"))
    doc.appendChild(person_element)
    doc.appendChild(doc.createComment("THIS DATA IS FAKE AND IS NOT REAL!!  FOR EXAMPLE PURPOSES ONLY!!"))
    
    # Add elements for each person attribute to the person element
    person_element.setAttribute("id", record["NationalID"])
    person_element.setAttribute("xmlns", "http://www.marklogic.com/random/fake-people")
    
    addElement(person_element, "gender", "Gender")
    addElement(person_element, "first-name", "GivenName")
    addElement(person_element, "middle-initial", "MiddleInitial")
    addElement(person_element, "last-name", "Surname")
    addElement(person_element, "address", "StreetAddress")
    addElement(person_element, "city", "City")
    addElement(person_element, "state", "State")
    addElement(person_element, "zipcode", "ZipCode")
    addElement(person_element, "country", "Country")
    addElement(person_element, "email", "EmailAddress")
    addElement(person_element, "telephone", "TelephoneNumber")
    addElement(person_element, "birthday", "Birthday")
    addElement(person_element, "domain", "Domain")
    addElement(person_element, "occupation", "Occupation")
    addElement(person_element, "blood-type", "BloodType")
    addElement(person_element, "pounds", "Pounds")
    addElement(person_element, "kilograms", "Kilograms")
    addElement(person_element, "feet-inches", "FeetInches")
    addElement(person_element, "centimeters", "Centimeters")
    addElement(person_element, "country", "Country")
    addElement(person_element, "password", "Password")
    addElement(person_element, "credit-card-type", "CCType")
    addElement(person_element, "credit-card-number", "CCNumber")
    addElement(person_element, "cvv2", "CVV2")
    addElement(person_element, "credit-card-expiration", "CCExpires")
    
    write_to_file(doc, "./fake-names/" + record["NationalID"] + ".xml")
 
    