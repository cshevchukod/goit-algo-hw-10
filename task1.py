# task1.py

import pulp

def task1():

    water_max = 100
    sugar_max = 50
    lemon_juice_max = 30
    fruit_puree_max = 40

    model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    model += lemonade + fruit_juice

    model += 2 * lemonade + fruit_juice <= water_max      # вода
    model += lemonade <= sugar_max                        # цукор
    model += lemonade <= lemon_juice_max                  # лимонний сік
    model += 2 * fruit_juice <= fruit_puree_max           # фруктове пюре

    model.solve(pulp.PULP_CBC_CMD(msg=False))    # без логу

    print("Status:", pulp.LpStatus[model.status])
    print("Lemonade:", int(lemonade.varValue))
    print("Fruit Juice:", int(fruit_juice.varValue))
    print("Max total products:", int(pulp.value(model.objective)))


if __name__ == "__main__":
    task1()
