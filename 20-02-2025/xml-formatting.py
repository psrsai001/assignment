import xml.etree.ElementTree as ET

root = ET.Element("students")


def write_xml():

    def create_student_tag():
        return ET.SubElement(root, "student")

    def create_name_tag(student_tag: ET.Element):
        return ET.SubElement(student_tag, "name")

    def create_branch_tag(student_tag: ET.Element):
        return ET.SubElement(student_tag, "branch")

    def add_student(name: str, branch: str):
        student_tag = create_student_tag()
        name_tag = create_name_tag(student_tag)
        branch_tag = create_branch_tag(student_tag)
        name_tag.text = name
        branch_tag.text = branch

    add_student("alice", "it")
    add_student("bob", "eee")
    add_student("jhon", "ece")
    add_student("jane", "cse")

    tree = ET.ElementTree(root)

    tree.write("xml-data.xml", encoding="utf-8")


def read_xml():
    tree = ET.parse("xml-data.xml")
    root = tree.getroot()
    for student in root.findall("student"):
        name = ""
        branch = ""

        find_name = student.find("name")
        find_branch = student.find("branch")
        if find_name != None:
            name = find_name.text
        if find_branch != None:
            branch = find_branch.text

        print(f"Name: {name}, Branch: {branch}")


write_xml()
read_xml()
