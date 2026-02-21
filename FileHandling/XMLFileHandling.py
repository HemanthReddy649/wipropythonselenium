import xml.etree.ElementTree as ET

# read xml file

# parse xml file ito a variab
tree = ET.parse("C:/Users/thiru/PycharmProjects/PythonAdvanceProject/DataFormats/employee.xml")
root = tree.getroot()
print(root.tag)

# get the first child node / tag
print(root[0].tag)

# get the attributes of the child node
print(root[0].attrib)

# fetch all the attributes in the child node
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)
    emp_name = employee.find("name").text
    print(emp_name)

for emp in root.findall("employee"):
    name = emp.find("name").text
    role = emp.find("role").text
    exp = emp.find("experience").text
    print(name, role, exp)

# flow is root ----- child node ------attributes of the child node ---- text of the attributes

# create the root element
root = ET.Element("employees")

# create the child elements

emp1 = ET.SubElement(root, "employees", id="101")
ET.SubElement(emp1, "name").text = "Ankit"
ET.SubElement(emp1, "role").text = "dev"
ET.SubElement(emp1, "exp").text = "8"
# create the child node 2

emp2 = ET.SubElement(root, "employee", id="101")
ET.SubElement(emp2, "name").text = "Ankit"
ET.SubElement(emp2, "role").text = "dev"
ET.SubElement(emp2, "exp").text = "8"

# write to the file
tree = ET.ElementTree(root)
tree.write("C:/Users/thiru/PycharmProjects/PythonAdvanceProject/DataFormats/updatexml.xml", encoding="utf-8",
           xml_declaration=True)

# update the xml

tree = ET.parse("C:/Users/thiru/PycharmProjects/PythonAdvanceProject/DataFormats/updatexml.xml")
root = tree.getroot()

for emp in root.findall("employee"):
    if emp.get("id") == "101":
        emp.find("exp").text = "16"

ET.indent(tree, space="  ", level=0)

tree.write("C:/Users/thiru/PycharmProjects/PythonAdvanceProject/DataFormats/updatexml.xml", encoding="utf-8",
           xml_declaration=True)
