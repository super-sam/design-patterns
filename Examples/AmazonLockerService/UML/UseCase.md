# Use Case Diagram

## System
Amazon Locker

## Actors
### Primary actors
- Customer
    - Orders Package
    - Collectes from Locker
    - Return to a Locker
- Delivery Agent
    - Add product to Locker
    - Pick up from Locker
### Secondary actors
- System
    - Notification
    - Generate Code
    - Validate Code
    - Choose Locker

## Use Cases

### Customer
- **Enter code**: To enter the code top open a locker
- **Add product**: To add the product to the locker
- **Remove product**: To pick up the product from the locker
- **Delivery notification**: To notify abount the product location
- **Submit return request**:
- **Overdue Notification** 

### Delivery Partner
- **Enter Code**: To open Locker
- **Add Product**: To the locker
- **Remove Product**: Pick up from the locker
- **Return Notification**: Notify about the product return status

### System
- **Validate code** 
- **Find Locker**
- **Lock/Unlock door**
- **Return Notification**
- **Generate Code**
- **Issue Locker**
- **Overdue Notification**
- **Delivery Notification**

## Relationships
|Customer|Deleivery Agent| System|
|--|--|--|
|Enter Code| Enter Code| Validate Code|
|Add Product| Add Product| Find Locker|
|Remove Product | Remove Product | Lock/Unlock Door |
|Delivery Notification | Return Notification | Return Notification|
|Submit return request | | Generate Code |
| Overdue notification | | Issue Locker |
| | | Overdue notifcation|
| | | Delivery notification |
