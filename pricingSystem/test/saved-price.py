import numpy as np

num_of_tasks = 50
factor = 1000
# for i in range(1, num_of_tasks+1):
#     proposed = np.array([0.23 for _ in range(i)])
#     edgeprice1 = np.array([min(np.random.normal(0.2070, 0.01, 3)) for _ in range(i)])
#     edgeprice2 = np.array([min(np.random.normal(0.2070, 0.01, 1)) for _ in range(i)])
#     edgeprice3 = np.array([min(np.random.uniform(0.17, 0.23, 3)) for _ in range(i)])
#     edgeprice4 = np.array([min(np.random.uniform(0.17, 0.23, 1)) for _ in range(i)])
#     edgeprice5 = np.array([min(np.random.normal(0.2070, 0.001, 3)) for _ in range(i)])
#     edgeprice6 = np.array([min(np.random.normal(0.2070, 0.001, 1)) for _ in range(i)])
#     saved_price1 = proposed - edgeprice1
#     saved_price1 = saved_price1.sum()
#     saved_price2 = proposed - edgeprice2
#     saved_price2 = saved_price2.sum()
#     saved_price3 = proposed - edgeprice3
#     saved_price3 = saved_price3.sum()
#     saved_price4 = proposed - edgeprice4
#     saved_price4 = saved_price4.sum()
#     saved_price5 = proposed - edgeprice5
#     saved_price5 = saved_price5.sum()
#     saved_price6 = proposed - edgeprice6
#     saved_price6 = saved_price6.sum()
#     with open ('/Users/a931759898/Desktop/edgeblockchain/pricingSystem/test/data.txt', 'a') as f:
#         f.write('%f, ' %saved_price1)
#         f.write('%f, ' %saved_price2)
#         f.write('%f, ' %saved_price3)
#         f.write('%f, ' %saved_price4)
#         f.write('%f, ' %saved_price5)
#         f.write('%f\n' %saved_price6)



num_of_users = [5, 10, 15]
for i in range(1, num_of_tasks+1):
    index = 0
#     proposed = np.array([max(np.random.normal(0.23, 0.01, num_of_users[index])) for _ in range(i)])
    edgeprice = 0.2070
    user_price1 = np.array([max(np.random.normal(0.23, 0.01, num_of_users[index])) for _ in range(i)])
    user_price2 = np.array([max(np.random.normal(0.23, 0.01, 1)) for _ in range(i)])
    index = (index + 1)%3
    user_price3 = np.array([max(np.random.normal(0.23, 0.01, num_of_users[index])) for _ in range(i)])
    user_price4 = np.array([max(np.random.normal(0.23, 0.01, num_of_users[index])) for _ in range(i)])
    index = (index + 1)%3
    user_price5 = np.array([max(np.random.normal(0.23, 0.01, num_of_users[index])) for _ in range(i)])
    user_price6 = np.array([max(np.random.normal(0.23, 0.01, num_of_users[index])) for _ in range(i)])
    index = (index + 1)%3

    saved_price1 = user_price1 - edgeprice
    saved_price1 = saved_price1.sum()
    saved_price2 = user_price2 - edgeprice
    saved_price2 = saved_price2.sum()
    saved_price3 = user_price3 - edgeprice
    saved_price3 = saved_price3.sum()
    saved_price4 = user_price4 - edgeprice
    saved_price4 = saved_price4.sum()
    saved_price5 = user_price5 - edgeprice
    saved_price5 = saved_price5.sum()
    saved_price6 = user_price6 - edgeprice
    saved_price6 = saved_price6.sum()
    with open ('/Users/a931759898/Desktop/edgeblockchain/pricingSystem/test/shuffle-data.txt', 'a') as f:
        f.write('%f, ' %saved_price1)
        f.write('%f, ' %saved_price2)
        f.write('%f, ' %saved_price3)
        f.write('%f, ' %saved_price4)
        f.write('%f, ' %saved_price5)
        f.write('%f\n' %saved_price6)

    

# print(min(np.random.normal(0.2070, 0.001, 1000)))