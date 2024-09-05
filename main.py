# important stuff

"""
For example, say we have a 90% fill rate requirement for Target with a 1% penalty rate. If the PO is for 100 units and a total 
amount of $150 but we only deliver 80 units, then we will be fined

"""
# $0.15 = (10 units * 0.01 * $1.50/unit).

# (units_missing * penalty_rate * unit_cost)

"""
1. Sum the units and amounts across all POs.
2. Write a function to determine the penalty if we ship nothing. Ie, we incur the maximum
penalty possible.
3. Write a function to determine how much of each PO we should fulfill to minimize the
penalty. Calculate the expected penalty with your approach.

"""

import json


def sum_units_and_amounts():
    pass


with open('purchase_orders.json', 'r') as file:
    data = json.load(file)
    
