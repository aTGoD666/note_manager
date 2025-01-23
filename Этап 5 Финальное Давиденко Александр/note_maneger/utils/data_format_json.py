from datetime import datetime

def data_format_json(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, list):
        return [data_format_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: data_format_json(value) for key, value in obj.items()}
    else:
        return obj
    print("Дата не изменена!")