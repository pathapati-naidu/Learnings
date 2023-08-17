personal_details={
    "Name":"P Mahesh Kumar",
    "Age":20,
    "Country":"USA"
}
print(personal_details.get("Age"))
print(personal_details.keys())

# Set the values for all the keys as same using the dict.fromkeys() method
persons_info=["Mahesh","Gowtham","Gowtham k"]
new_dict=dict.fromkeys(persons_info,"Germany")
print(new_dict)