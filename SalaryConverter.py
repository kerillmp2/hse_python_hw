from FileReader import FileReader
from TimeUtils import TimeUtils

class SalaryConverter():
    
    @staticmethod
    def calculate_hour_income(working_days, salary):
        assert working_days > 0, "Number of working must be more than 0"
        assert salary >= 0, "Salary can't be less than 0"
        working_hours = 8 * working_days
        return round(salary / working_hours, 2)
    
    
    @staticmethod
    def convert_salary(input_file, output_file):
        content = FileReader.read_salary_data(input_file)
        working_days = TimeUtils.get_working_days(content['year'], content['month'])
        hour_income = SalaryConverter.calculate_hour_income(working_days, content['salary'])
        output_data = SalaryConverter.form_output(content['year'], content['month'], content['salary'], hour_income)
        FileReader.write_data(output_file, output_data)
        print("Converted successfully!")
    
    
    @staticmethod
    def form_output(year, month, salary, hour_income):
        return {'year': year, 'month': month, 'salary': salary, 'hour_income': hour_income}
