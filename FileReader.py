import json

class FileReader():
        
    @staticmethod
    def read_data(file_name):
        file = open(file_name)
        content = file.read()
        file.close()
        return content
    
    
    @staticmethod
    def read_salary_data(file_name):
        content = FileReader.read_data(file_name)
        parsed_content = json.loads(content)
        for option in ['year', 'month', 'salary']:
            if option not in parsed_content:
                raise ValueError("No option {} in file {}".format(option, file_name))
        parsed_content['year'] = int(parsed_content['year'])
        parsed_content['salary'] = float(parsed_content['salary'])
        assert parsed_content['salary'] >= 0, "salary can't be negative"
        return parsed_content

    
    @staticmethod
    def write_data(file_name, data):
        file = open(file_name, 'w')
        file.write(data)
        file.close()
