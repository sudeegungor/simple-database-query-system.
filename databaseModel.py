# -*- coding: utf-8 -*-
"""

"""
import re
import csv
import json


# Define the Student class
class Student:
    def __init__(self, id, name, lastname, email, grade):
        self.name = name
        self.id = id
        self.lastname = lastname
        self.email = email
        self.grade = grade
        
# Print student information
def print_info(st):
    if hasattr(st, 'id'):
        print(st.id)
    if hasattr(st, 'name'):
        print(st.name)
    if hasattr(st, 'lastname'):
        print(st.lastname)
    if hasattr(st, 'email'):
        print(st.email)
    if hasattr(st, 'grade'):
        print(st.grade)
        
# Get specific information from a student
def get_info(student, columns,st):
    if "id" in columns:
        print("ID:", student.id)
        st.id=student.id
    if "name" in columns:
        print("name:", student.name)
        st.name=student.name
    if "surname" in columns:
        print("surname:", student.lastname)
        st.lastname=student.lastname
    if "email" in columns:
        print("email:", student.email)
        st.email=student.email
    if "grade" in columns:
        print("grade:", student.grade)
        st.grade=student.grade
    if "all" in columns:
        print("ID:", student.id)
        st.id=student.id
        print("name:", student.name)
        st.name=student.name
        print("surname:", student.lastname)
        st.lastname=student.lastname
        print("email:", student.email)
        st.email=student.email
        print("grade:", student.grade)
        st.grade=student.grade



# Compare two values using an operator
def compare(a, b, operator):
    if(operator == '<'):
        if a < b:
            return True
        else:
            return False
    elif(operator == '>'):
        if a > b:
            return True
        else:
            return False
    elif(operator == '='):
        if a == b:
            return True
        else:
            return False
    elif(operator == '!='):
        if a != b:
            return True
        else:
            return False
    elif(operator == '<='):
        if a <= b:
            return True
        else:
            return False
    elif(operator == '>='):
        if a >= b:
            return True
        else:
            return False
    elif(operator == '!>'):
        if a <= b:
            return True
        else:
            return False
    elif(operator == '!<'):
        if a >= b:
            return True
        else:
            return False

flag=True
while flag:
     # Load data from a CSV file
    def load_data_from_csv(file_path):
        data = []
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                data.append(row)
                return data

    file_path = 'students.csv'
    data = load_data_from_csv(file_path)
    #take input query from user
    query = input('Enter a query (or "exit" to quit): ')
    query_parts = query.split(' ')
    if query_parts[0]=="exit": #first command word
        flag=False
        print("You have exited the system")
        break
    # Check if the query is a SELECT statement
    if query_parts[0].lower() == 'select':
        #find wanted select statements
        columns = query_parts[1].split(',')
        where_clause = query_parts[5:-3]
        order_clause = query_parts[-1].lower()
        if len(where_clause) > 3:
            raise ValueError(
                "Invalid query format: Too many conditions in WHERE clause")
        condition1 = where_clause[0]
        #operator in first where clause
        operator1 = re.findall(r'\W', condition1)
        end1 = condition1.find(operator1[0])
        #corresponded row in csv
        col1 = condition1[0:end1].lower()
        #value to compare
        value1 = condition1[end1+1:]
        #find AND/OR
        operator_main = where_clause[1].lower()
        condition2 = where_clause[2]
        operator2 = re.findall(r'\W', condition2)
        end2 = condition2.find(operator2[0])
        col2 = condition2[0:end2].lower()
        value2 = condition2[end2+1:]
        records = []
        output=[]
        with open('students.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in reader:
                student = Student(row[0], row[1], row[2], row[3], row[4])
                # Applying conditions to filter records
                if line_count > 0:
                    #if compared values connected with AND
                    if operator_main=="and":
                        #first if for first element in where clause
                        if col1 == "id":
                            #second if for second element in where clause
                            if col2 == "name":
                                if compare(row[0], value1, operator1[0]) == True and compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[0], value1, operator1[0]) == True and compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[0], value1, operator1[0]) == True and compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[0], value1, operator1[0]) == True and compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "name":
                            if col2 == "id":
                                if compare(row[1], value1[1:-1], operator1[0]) == True and compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[1], value1[1:-1], operator1[0]) == True and compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[1], value1[1:-1], operator1[0]) == True and compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[1], value1[1:-1], operator1[0]) == True and compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "lastname":
                            if col2 == "id":
                                if compare(row[2], value1[1:-1], operator1[0]) == True and compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "name":
                                if compare(row[2], value1[1:-1], operator1[0]) == True and compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[2], value1[1:-1], operator1[0]) == True and compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[2], value1[1:-1], operator1[0]) == True and compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "email":
                            if col2 == "id":
                                if compare(row[3], value1[1:-1], operator1[0]) == True and compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "name":
                                if compare(row[3], value1[1:-1], operator1[0]) == True and compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[3], value1[1:-1], operator1[0]) == True and compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[3], value1[1:-1], operator1[0]) == True and compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "grade":
                            if col2 == "id":
                                if compare(row[4], value1, operator1[0]) == True and compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "name":
                                if compare(row[4], value1, operator1[0]) == True and compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[4], value1, operator1[0]) == True and compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[4], value1, operator1[0]) == True and compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                    #if two statements are connected with OR
                    if operator_main=="or":
                        if col1 == "id":
                            if col2 == "name":
                                if compare(row[0], value1, operator1[0]) == True or compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[0], value1, operator1[0]) == True or compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[0], value1, operator1[0]) == True or compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[0], value1, operator1[0]) == True or compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "name":
                            if col2 == "id":
                                if compare(row[1], value1[1:-1], operator1[0]) == True or compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[1], value1[1:-1], operator1[0]) == True or compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[1], value1[1:-1], operator1[0]) == True or compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[1], value1[1:-1], operator1[0]) == True or compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "lastname":
                            if col2 == "id":
                                if compare(row[2], value1[1:-1], operator1[0]) == True or compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "name":
                                if compare(row[2], value1[1:-1], operator1[0]) == True or compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[2], value1[1:-1], operator1[0]) == True or compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[2], value1[1:-1], operator1[0]) == True or compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "email":
                            if col2 == "id":
                                if compare(row[3], value1[1:-1], operator1[0]) == True or compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "name":
                                if compare(row[3], value1[1:-1], operator1[0]) == True or compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[3], value1[1:-1], operator1[0]) == True or compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "grade":
                                if compare(row[3], value1[1:-1], operator1[0]) == True or compare(row[4], value2, operator2[0]) == True:
                                    records.append(student)

                        if col1 == "grade":
                            if col2 == "id":
                                if compare(row[4], value1, operator1[0]) == True or compare(row[0], value2, operator2[0]) == True:
                                    records.append(student)
                            if col2 == "name":
                                if compare(row[4], value1, operator1[0]) == True or compare(row[1], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "lastname":
                                if compare(row[4], value1, operator1[0]) == True or compare(row[2], value2[1:-1], operator2[0]) == True:
                                    records.append(student)
                            if col2 == "email":
                                if compare(row[4], value1, operator1[0]) == True or compare(row[3], value2[1:-1], operator2[0]) == True:
                                    records.append(student)

                #incerement line with 1
                line_count += 1
                #order selected values according to id
            if order_clause=="asc":
                records = sorted(records, key=lambda student: student.id)
            elif order_clause=="dsc":
                records = sorted(records, key=lambda student: student.id, reverse=True)
                #print selected students and add to json file
            for index in records:
                st=Student
                get_info(index, columns,st)
                output.append(st)
                student_data = [data.__dict__ for data in records]
                with open("output.json", "w") as json_file:
                    json.dump(student_data, json_file, indent=4)
            print("Data written to the JSON file.")

    def parse_delete_query(query):
        query_parts = query.split()
        if len(query_parts) < 4:
            raise ValueError("Invalid query format: Missing table name or conditions")
# Checking the format of the DELETE query
        if query_parts[0].upper() != 'DELETE' or query_parts[1].upper() != 'FROM' or query_parts[3].upper() != 'WHERE':
            raise ValueError("Invalid query format: DELETE query expected")
# Extracting table name and conditions from the query
        table_name = query_parts[2]
        conditions = ' '.join(query_parts[4:])

        return table_name, conditions

    def delete_records_from_csv(file_path, query):
            # Checking if the query starts with DELETE
        if not query.upper().startswith('DELETE'):
            return

        # Extract table name and conditions from the query
        table_name, conditions = parse_delete_query(query)

        # Load data from CSV file
        data = []
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                data.append(row)

        # Find indices of the columns to check for the delete conditions
        headers = data[0]
        condition_column_indices = []
        condition_values = []
        condition_operators = []

        condition_parts = conditions.split(' ')
        condition_len = len(condition_parts)
        i = 0
        while i < condition_len:
            column = condition_parts[i]
            if column.upper() == 'AND' or column.upper() == 'OR':
                i += 1
                continue

            operator = condition_parts[i + 1]
            value = condition_parts[i + 2].strip('‘’"')

            condition_column_indices.append(headers.index(column))
            condition_operators.append(operator)
            condition_values.append(value)

            i += 3

        # Filter records that match the delete conditions
        filtered_data = [row for row in data[1:] if not all(
            compare(row[idx], value, operator) for idx, operator, value in
            zip(condition_column_indices, condition_operators, condition_values)
        )]

        # Write the filtered data back to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            writer.writerow(headers)
            writer.writerows(filtered_data)

        # Write the filtered data to a JSON file
        json_data = {'deleted_records': filtered_data}
        json_file_path = 'output.json'
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Deleted records based on the query: {query}")
        print(f"Deleted records saved to {json_file_path}")
    # Example usage
    file_path = 'students.csv'
    delete_records_from_csv(file_path, query)
    def insert_records_to_csv(file_path, query):
         # Checking if the query starts with INSERT INTO
        if not query.upper().startswith('INSERT INTO'):
            return

        # Extract values from the query
        values_start_index = query.index('VALUES') + len('VALUES')
        values_str = query[values_start_index:].strip('()')

        # Split the values string and remove whitespace
        values = [value.strip() for value in values_str.split(',')]

        # Load data from CSV file
        data = []
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                data.append(row)

        headers = data[0]

        # Append the new record to the data
        data.append(values)

        # Write the updated data back to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow(headers)
            writer.writerows(data)

        # Write the entire data (including the inserted record) to a JSON file
        json_data = {'all_records': data}
        json_file_path = 'output.json'
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Inserted 1 record into the CSV file.")
        print(f"All records saved to {json_file_path}")

    # Example usage
    file_path = 'students.csv'
    insert_records_to_csv(file_path, query)



