"""

TASK 1 
------------------------------------------------------------------------------------------------
ticket_type() <- ("OneAdult","OneChild","Onesenior","FamilyTicket, "GroupTicket")
one_day_booking_cost() <- (20, 12, 16, 60, 15)
two_day_booking_cost() <- (30, 18, 24, 90, 22.5)
extra_attraction() <- ("Lionfeed", "Penguinfeed", "Barbecue(only 2day ticket)")
extra_attraction_cost <- (2.5, 2, 5)
days_of_the_week <- ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
choice <- ""
extra_choice <- "" 

family_group <- 0

num_of_tickets <- 0
ticket_selected <- 0 
booking_day <- 0 
booking_ID <- 0

cost <- 0 
extra_selected <- 0


For count = 1 To 5
    PRINT ("Ticket type = ", ticket_type(count), ":", "Cost1 Day="one_day_booking_cost(count),":"
    , "Cost 2 day =", two_day_booking_cost(count))
Next
PRINT ("Entra attraction optons are displayed below:")
For count = 1 To 3
    PRINT ("Attraction", extra_attraction_cost(count), "=", extra_attraction(count))
Next


TASK 2
------------------------------------------------------------------------------------------------
PRINT ("Do you want to buy tickets? Y/N ")
PRINT ("Enter Ticket Catagory number: 1= OneAdult , 2 = OneChild, 3 = Onesenior 4 = Family Ticket, 5 = Group ticket")
INPUT ticket_selected


If ticket_selected = 5 Then
    PRINT ("Is this family group? Y/N")
    INPUT family_group
End If


PRINT ("Confirm booking for One day or Two days? 1 = one day, 2 = two days")
INPUT booking_day

PRINT ("Enter number of tickets")
INPUT num_of_tickets

booking_ID = booking_ID + 1  # This is for unique booking ID
If booking_day = 1 Then
    cost = num_of_tickets * one_day_booking_cost(ticket_selected)
    ElseIf booking_day = 2 Then
    cost = num_of_tickets * two_day_booking_cost(ticket_selected)
End If

PRINT("Your booking_ID for this booking is: " , booking_ID)

PRINT("Cost of ticket:",ticket_type(ticket_selected),"tickets=",num_of_tickets," Cost=",cost)

PRINT ("Do you want Extra attraction? Y/N")
INPUT extra_choice
IF extra_choice = Y Then
    PRINT ("Extra attraction num: 1= Lionfeed, 2= Penguinfeed, 3= Barbecue")
    INPUT extra_selected
    WHILE extra_selected =3 AND booking_day =1 # Validation check for BBQ which is only for 2 day tickets (We are doing this so that we can check if they entered the number and then tell them it isn't available)
        PRINT ("Barbecue is available for two day tickets only, Input again")
        INPUT extra_selected
    END WHILE

    cost = cost + extra_attraction_cost(extra_selected)
    
    PRINT (
        " Cost of:",ticket_type(ticket_selected), 
        " Num of tickets:", numofticket, "+", extra_attraction(extra_selected), 
        " TOTAL=", cost)
    
    Else
        PRINT (
            " Your ticket cost :", ticket_type(ticket_selected),
            " Num of tickets: ", num_of_tickets,
            " No attraction "," Cost = ", cost)
END IF


TASK 3
------------------------------------------------------------------------------------------------

best_offer  <- 0

IF TotalMember>=6 :
    IF(VisitingDays=1) THEN
        Groupcost=Totalmember()
    ELSEIF(VistingDays=2)  
        Groupcost=Totalmember*22.50
Print(“Total Cost Calculation for tickets :”,TotalTicketcost)
Print("The Group cost is:",Groupcost)

    IF( TotalTicketcost > Groupcost)THEN
        Print("Taking group ticket is the best offer")
        offer=input("Do you want this offer Y/N")
      IF (offer = "Y" or offer="y") THEN
            TotalTicketcost=Groupcost
      ELSE
        Print("Family ticket is the best offer")
     END IF
    END IF


If best_offer > 0 Then
    PRINT ("Take BEST offer & save = ", cost - best_offer)
    PRINT (
            "Best offer = ", best_offer
            "For Best offer do a NEW Booking: Y/N, Do you want new booking? "
            )
    
    INPUT choice
    
    If choice = Y Then
        GoTo Task 2
        Else
            PRINT ("Best offer not selected")
    End If
End If

PRINT (
        "Ticket Type = ", ticket_type(ticket_selected)
        ", Number = ", num_of_tickets
        " ,Cost = ", cost
        
    )

"""


















































































































































































































































































































































































































































































