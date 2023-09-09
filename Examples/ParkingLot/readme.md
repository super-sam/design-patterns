# Parking Lot
- --

## Requiments Gathering
- R1: Max Capacity 40000
- R2: 4 types of Parking Spot
  - Handicapped
  - Compact
  - Large
  - Motorcycle
- R3: Multiple Entrance
- R4: 4 types of vehicle:
  - Car
  - Truck
  - Van
  - Motorcycle
- R5: Display board, show free parking spot by type(R4)
- R6: Shouldn't allow more than max cap
- R7: Parking full message
- R8: Collect ticket at entrance and Pay at exit
- R9: Pay with 
  - Automated panel
  - Parking Agent
- R10: Rate is hourly
- R11: Payment by Cash/Debit/Credit card

## System
Parking Lot

## Actors
### Primary Actors
- Customer
- Parking Agent

### Secondary Actors
 - Admin
 - System

## Use Cases
### Admin
- Add Spot
- Add Agent
- Add/Modify Rate
- Add Entry/Exit Panel
- Update Account
- Login/Logot
- View Account

### Customer
- Take Ticket
- Scan Ticket
- Pay Ticket
- Cash
- Credit Card
- Park Vehicle

### Parking Agent
- Update Account
- Login/Logout
- View account
- Take ticket
- Scan ticket
- Pay Ticket
- Cash
- Credit Card
- Park Vehicle

## System
- Assign parking spots to vehicles
- Remove Spot
- Show full
- Show Available

# Relationships
- ## Generalization
  - Parking Agent --|> Customer
  - Cash | Credit Card --|> Pay ticket

- ## Associations
  |Admin | Customer | Parking Agent | System|
  |--|--|--|--|
  |Add Spot| Take ticket|Update Account|Assign Parking spots to vehicles|
  |Add Agent | | | |
  |Add/Modify Rate | | | |























