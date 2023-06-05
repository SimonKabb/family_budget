from datetime import datetime
datetime_string = '05/Jun/2023 11:36 PM'
datetime_format = '%d/%b/%Y %I:%M %p'  # Указываем формат строки
date = datetime.strptime(datetime_string, datetime_format)
print(date)
