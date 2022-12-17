import re

def read_data(file_name):
    file = open(file_name)
    content = file.read()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_json(title, row):
    values = row.strip().split(',')
    entry = dict(zip(title, values))

    json_res = """
  {{
    "name": "{}",
    "id": "{}",
    "birth": "{}",
    "salary": "{}",
    "department": "{}"
  }}""".format(
        entry["name"] if entry["name"] else "null",
        entry["id"] if entry["id"] else "null" ,
        entry["birth"] if entry["birth"] else "null",
        entry["salary"] if entry["salary"] else "null",
        entry["department"] if entry["department"] else "null"
    )

    return json_res


def convert_csv_to_json(data):
    title, data = prepare_data(data)

    result = [convert_row_to_pretty_json(title, row) for row in data]
    res_str = str(result).replace("\\n", "\n").replace("\'", "")[:-1] + "\n]"
    return res_str


def main():
    data = read_data_to_list("input.csv")
    result = convert_csv_to_json(data)
    write_data("output.json", result)
