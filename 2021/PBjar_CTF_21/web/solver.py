import requests

session = requests.Session()

min = 100000000
max = 1000000000
mid = lambda a,b : (a+b)//2
pointer = 0

while True:
    if pointer == mid(min,max):
        print(pointer)
        break
    pointer = mid(min,max)
    r = session.get(f'http://147.182.172.217:42100/v{pointer}')
    if r.text == 'version not found':
        max = pointer
    else :
        min = pointer