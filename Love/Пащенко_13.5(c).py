def difference(f_name):
    with open(f_name,"r") as file:
        numbers = [int(num) for num in file.read().split() if num.isdigit()]
        evens = [num for num in numbers if num % 2 == 0]
        odds = [num for num in numbers if num % 2 != 0]

        max_evens = max (evens) if evens else None
        min_odds = min (odds) if odds else None
    return max_evens,min_odds



f_name = "file"
max_evens , min_odds = difference(f_name)

if max_evens is not None and min_odds is not None:
    difference = max_evens - min_odds
    print(f"Різниця між найбільшим парним і найменшим непарним числами з компонент:{difference}")
else:
    print(None)