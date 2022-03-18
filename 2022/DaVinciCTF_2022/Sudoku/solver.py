import requests
from bs4 import BeautifulSoup
import sudoku

with requests.Session() as session:
    res = session.get("http://challs.dvc.tf:6002/home")
    bs = BeautifulSoup(res.text, 'html.parser')
    elem = bs.select("input[type='text']")
    assert len(elem) == 9*9
    sudoku_num = []
    for e in elem:
        if e.has_attr('value'):
            sudoku_num.append(int(e['value'][0]))
        else:
            sudoku_num.append(0)
    # split 9*9
    sudoku_num = [sudoku_num[i:i + 9] for i in range(0, len(sudoku_num), 9)]

    grid = sudoku.Grid(sudoku_num)
    results = sudoku.solve_all(grid)
    solve = results.pop()._values

    flat = lambda l : sum(l, [])

    post_value = {}
    for (a,b,c) in zip(flat(sudoku_num), flat(solve), range(len(flat(sudoku_num)))):
        if a == 0:
            post_value[f'{c+1}'] = f'{b}'

    res = session.post("http://challs.dvc.tf:6002/flag",data=post_value)
    print(res.text)

