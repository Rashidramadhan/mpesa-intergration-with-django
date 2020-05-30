from datetime import datetime

def get_format_date():
    unformated_date = datetime.now()
    formated_date = unformated_date.strftime("%Y%m%d%H%M%S")
    return formated_date