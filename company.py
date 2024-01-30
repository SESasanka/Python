def calculate_cost(company, num_boxes):
    if num_boxes <= 100:
        cost = num_boxes * company[0]
    elif num_boxes <= 1100:
        cost = 100 * company[0] + (num_boxes - 100) * company[1]
    else:
        cost = 100 * company[0] + 1000 * company[1] + (num_boxes - 1100) * company[2]
    return cost

company1_prices = [2.99, 1.99, 1.50]
company2_prices = [2.50, 2.25, 1.75]

num_boxes = int(input("Enter the number of boxes you desire to buy: "))

cost_company1 = calculate_cost(company1_prices, num_boxes)
cost_company2 = calculate_cost(company2_prices, num_boxes)

if cost_company1 < cost_company2:
    print("In this case, you should go with Company 1.")
elif cost_company2 < cost_company1:
    print("In this case, you should go with Company 2.")
else:
    print("Both companies will cost the same. You may choose either.")

    

    
    
