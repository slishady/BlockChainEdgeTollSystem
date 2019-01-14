import numpy as np
import matplotlib.pyplot as plt
factor = 1000000000000000000
gasPrice = 1000000000
def read_txt(file_path):
    saved_money = []
    gas_cost = []
    total_time = []
    with open(file_path, 'r') as f:
        while True:
            a = f.readline()
            if not a:
                break
            if a.startswith('#') or a == '\n':pass
            else:
                c = a.split(', ')
                # print(c)
                saved_money.append(float(c[2].strip('\n')))
                gas_cost.append(int(c[1]))
                total_time.append(int(c[0]))
            # print(a)
            # print(type(a))
        return total_time, gas_cost, saved_money


# def read_txt(file_path):
#     saved_price1 = []
#     saved_price2 = []
#     saved_price3 = []
#     saved_price4 = []
#     saved_price5 = []
#     saved_price6 = []
#     with open(file_path, 'r') as f:
#         while True:
#             a = f.readline()
#             if not a:
#                 break
#             if a.startswith('#') or a == '\n':pass
#             else:
#                 c = a.split(', ')
#                 # print(c)
#                 saved_price1.append(float(c[0].strip('\n')))
#                 saved_price2.append(float(c[1].strip('\n')))
#                 saved_price3.append(float(c[2].strip('\n')))
#                 saved_price4.append(float(c[3].strip('\n')))
#                 saved_price5.append(float(c[4].strip('\n')))
#                 saved_price6.append(float(c[5].strip('\n')))
#             # print(a)
#             # print(type(a))
#         return np.array(saved_price1), np.array(saved_price2), np.array(saved_price3), np.array(saved_price4), np.array(saved_price5), np.array(saved_price6)


a, b, c = read_txt('/Users/a931759898/Desktop/edgeblockchain/pricingSystem/test/data1.txt')
a2, b2, c2 = read_txt('/Users/a931759898/Desktop/edgeblockchain/pricingSystem/test/data2.txt')
a2[0] = 222
# print(int('  66'))
a, b, c, a2, b2, c2 = np.array(a),np.array(b),np.array(c),np.array(a2),np.array(b2),np.array(c2)

# saved_price1, saved_price2, saved_price3, saved_price4, saved_price5, saved_price6 = read_txt('/Users/a931759898/Desktop/edgeblockchain/pricingSystem/test/data.txt')
#the fig for time cost
x = range(5, 51)
# plt.figure(figsize=(10,5))
# print(c)
# print(c2)
# plt.figure(figsize=(10,7))
# plt.title("the figure of users' task versus total time cost")
# plt.style.use('ggplot')
# plt.xlabel("the number of users' task")
# plt.ylabel("the total time")
# plt.plot(x,a, label="with system")
# plt.plot(x,a2,color='r', label="without system")
# plt.legend()
# plt.show()
# plt.savefig('time.jpg')

System1 = (b * gasPrice).astype('float')/factor
no1 = (b2 * gasPrice).astype('float')/factor
System4 = (b * gasPrice*4).astype('float')/factor
no4 = (b2 * gasPrice*4).astype('float')/factor
System7 = (b * gasPrice*7).astype('float')/factor
no7 = (b2 * gasPrice*7).astype('float')/factor
plt.figure(figsize=(10,7))
plt.title("the figure of users' task versus total gas cost")
plt.style.use('ggplot')
plt.xlabel("the number of users' task")
plt.ylabel("Gas fee (ether)")
# plt.plot(x,b, label="with system")
# plt.plot(x,b2,color='r', label="without system")
plt.plot(x, System1, 'ro-', label="Proposed, gas price = 1 Gwei", fillstyle='none')
plt.plot(x, no1, 'r*-', label="Traditional, gas price = 1 Gwei", fillstyle='none')
plt.plot(x, System4, 'bs--', label="Proposed, gas price = 4 Gwei", fillstyle='none')
plt.plot(x, no4, 'bx--', label="Traditional, gas price = 4 Gwei", fillstyle='none')
plt.plot(x, System7, 'k^-.', label="Proposed, gas price = 7 Gwei", fillstyle='none')
plt.plot(x, no7, 'kp-.', label="Traditional, gas price = 7 Gwei", fillstyle='none')
plt.legend()
plt.show()
plt.savefig('gas.jpg')

# plt.figure(figsize=(10,7))
# plt.title("the figure of users' task versus saved price")
# plt.style.use('ggplot')
# plt.xlabel("the number of users' task")
# plt.ylabel("Saved Price (ether)")
# # plt.plot(x,b, label="with system")
# # plt.plot(x,b2,color='r', label="without system")
# plt.plot(x, saved_price1, 'ro-', label="Proposed, distribution = normal, mean = 0.2070, stdev = 0.01", fillstyle='none')
# plt.plot(x, saved_price2, 'r*-', label="Traditional, distribution = normal, mean = 0.2070, stdev = 0.01", fillstyle='none')
# plt.plot(x, saved_price3, 'bs--', label="Proposed, distribution = uniform", fillstyle='none')
# plt.plot(x, saved_price4, 'bx--', label="Traditional, distribution = uniform", fillstyle='none')
# plt.plot(x, saved_price5, 'k^-.', label="Proposed, distribution = normal, mean = 0.2070, stdev = 0.001", fillstyle='none')
# plt.plot(x, saved_price6, 'kp-.', label="Traditional, distribution = normal, mean = 0.2070, stdev = 0.001", fillstyle='none')
# plt.legend()
# plt.show()
# plt.savefig('gas.jpg')

# plt.figure(figsize=(10,7))
# plt.title("the figure of users' task versus total saved price")
# plt.style.use('ggplot')
# plt.xlabel("the number of users' task")
# plt.ylabel("the saved price")
# plt.plot(x,c, label="with system")
# plt.plot(x,c2,color='r', label="without system")
# plt.legend()
# plt.show()
# plt.savefig('gas.jpg')