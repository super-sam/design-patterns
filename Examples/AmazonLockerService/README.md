# Amazon Locker Service

## Problem 
Amazon is an online retail platform that allows its customers to place orders and buy products online. There are times when the customer is not available in the particular location to pick up the order. In such a case, Amazon Locker can be one of the most secure way of delivery.

Amazon Locker is also known as Amazon Hub or Amazon Hub Locker. It is a fully automated package delivery service provided by Amazon. Customers can choose any locker location as their delivery address and pick up the package from that location at no additional cost. In particular, when a customer places an order and chooses to get their item delivered to locker service, the system suggests the nearest available locker based on preferences. The order is packaged and placed in the locker. The customer gets the notification containing the code to open the locker, and they can pick up the package using that code within a valid amount of time. This is how the Amazon Locker service functions.

## Design Pattern
- Strategy design pattern
- Repository design pattern


## Requirement
1. While ordering the item(s), the customer can choose the nearest location to pick up the order package from the locker
2. One or more items can be contained in one order.
3. Different sizes of locker including
    - extra small
    - small
    - medium
    - large
    - extra large
4. Locker is assigned to customer based on size of the order package
5. When order is delivered to the locker, a 6 digit code is sent to the customer to open the locker
6. The package is kept inside the locker for 3 days only
7. If the customer doesnt pickup the packege, the refund process will be intiated and the customer wont be allowed to pickup the package
8. Only eligible package can be place in the locker
9. There can be multiple locker at every location
10. Locker can be access withiing a specific time. Every locker has opening and closing time
11. Item can be returned by customer based on return policy
12. Customer can choose nearest Locker location. 
13. Once customer picksup the package, locker will be closed