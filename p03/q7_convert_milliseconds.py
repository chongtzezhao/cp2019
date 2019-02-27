def convert_ms(num):
    hours=num//3600000
    minutes=(num%3600000)//60000
    seconds=(num%60000)//1000
    return f"{hours}:{minutes}:{seconds}"
