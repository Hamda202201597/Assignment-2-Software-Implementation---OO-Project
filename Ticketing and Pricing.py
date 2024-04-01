class Visitor:
    # code constructors to initialise the visitor attributes
    def __init__(self, visitor_id, visitor_name, visitor_age, visitor_category,visitor_email ):
        self.visitor_id = visitor_id
        self.visitor_name = visitor_name
        self.visitor_age = visitor_age
        self.visitor_category = visitor_category
        self.visitor_email = visitor_email

    def __str__(self): # adding the f string to show the visitors information
        return f"""
        Visitor ID: {self.visitor_id}
        Visitor's Name: {self.visitor_name}
        Visitor's Age: {self.visitor_age}
        Visitor's Category: {self.visitor_category}
        Visitor's Email: {self.visitor_email}
        """

    # Setters and getters for all the Specified attributes
    def setvisitor_id(self, visitor_id):
        self.visitor_id = visitor_id
    def getvisitor_id(self):
        return self.visitor_id

    def setvisitor_name(self, visitor_name):
        self.visitor_name = visitor_name
    def getvisitor_name(self):
        return self.visitor_name

    def setvisitor_age(self, visitor_age):
        self.visitor_age = visitor_age
    def getvisitor_age(self):
        return self.visitor_age

    def setvisitor_category(self, visitor_category):
        self.visitor_category = visitor_category
    def getvisitor_category(self):
        return self.visitor_category

    def setvisitor_email(self, visitor_email):
        self.visitor_email = visitor_email
    def getvisitor_email(self):
        return self.visitor_email

    def freeticket(self): # adding a def function to put the visitors in categories
        if self.visitor_age < 18 or self.visitor_age > 60 or self.visitor_category == 'teacher, and or student ':
            return True
        return False

class ticket:
    # code constructors to initialise the ticket attributes
    def __init__(self, ticketid, visitor, visitingdate, event=False):
        self.ticketid = ticketid
        self.visitor = visitor
        self.visitingdate = visitingdate
        self.event = event
        self.price = self.calculateprice()

    def __str__(self): # adding the f string to show the tickets information
        return f"""
        Ticket ID: {self.ticketid}
        Ticket Price: {self.price} AED
        Date of Visiting: {self.visitingdate}
        """

    # Setters and getters for all the Specified attributes
    def setticketid(self, ticketid):
        self.ticketid = ticketid
    def getticketid(self):
        return self.ticketid

    def setvisitor(self, visitor):
        self.visitor = visitor
    def getvisitor(self):
        return self.visitor

    def setvisitingdate(self, visitingdate):
        self.visitingdate = visitingdate
    def getvisitingdate(self):
        return self.visitingdate

    def setevent(self, event):
        self.event = event
    def getevent(self):
        return self.event

    def calculateprice(self):
        if self.visitor.freeticket():
            return 0
        adultpay = 63  # the price adults have to pay
        if self.event:
            pass
        else:
            vatprice = adultpay * 1.05  # coding to add the 5% vat to the bill
        return vatprice  # Assuming this is the price to be returned

# objects to test the code
VisitorA = Visitor('703-1976-736737', 'Mohammed el attar', 48, 'adult', 'mohammed.el_attar@zu.ac.ae')
ticketA = ticket('T-827', VisitorA, '31-04-2024')
print(VisitorA)
print(ticketA)
