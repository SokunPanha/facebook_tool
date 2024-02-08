# user_tasks = {
#     "0": [
#         {"action": "login_2fa", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
#         # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
#     ],
#     "1": [
#         {"action": "login_2fa", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$", "key":"W6NG3L7Q3WSIQZQKI7THZ6HTV5J6I3QI"}},
#         # {"action": "login", "params": {"email": "amazing.org.ca@gmail.com", "password":"Panha@#$"}},
#     ],
# }
import math

def coor_click(num_video):
    
    table = 9
    row = range(0, math.ceil(table / 3))
    col =range(0,3)
    # print(row)
    coord = []
    n = 0
    for i in row:
        x = 200
        y = 600 + i * 300
        for j in col: 
            n  = n+1
            if n<=table:
                x = x + j*150
                print(f'{n}ROW {i}{x,y}')
                coord.append({"x":x, "y":y})
    return coord


print(type(coor_click(9)[1]["x"]))
# for i in row
# for i in range (0,7):
#     if i % 3 != 0 or i == 0:
#         print("video ----")
#         x = x + 250
#         y= temp
#         print("x,y",x,y)


#     elif i!=0:
#         # print("---------")
#         x = 250
#         temp = temp + 300
#         # print("x,y",x,y)