class Event:
    # code constructors to initialise the events attributes
    def __init__(self, id, brandname, startdate, enddate, museumsection):
        self.id = id
        self.brandname = brandname
        self.startdate = startdate
        self.enddate = enddate
        self.museumsection = museumsection

    def __str__(self): # adding the f string to show the event information
        return f"""
        Event ID: {self.id}
        Brand's name: {self.brandname}
        Event's start date: {self.startdate}
        Event's end date: {self.enddate}
        Event's museum section: {self.museumsection}
        """
    # Setters and getters for all the Specified attributes
    def setid(self, id):
        self.id = id
    def getid(self):
        return self.id

    def setbrandname(self, brandname):
        self.brandname = brandname
    def getbrandname(self):
        return self.brandname

    def setstartdate(self, startdate):
        self.startdate = startdate
    def getstartdate(self):
        return self.startdate

    def setenddate(self, enddate):
        self.enddate = enddate
    def getenddate(self):
        return self.enddate

    def setmuseumsection(self, museumsection):
        self.museumsection = museumsection
    def getmuseumsection(self):
        return self.museumsection

class Visitor: # code constructors to initialise the visitors attributes
    def __init__(self, visitor_id, visitor_name, visitor_age, visitor_agecategory, visitor_email):
        self.visitor_id = visitor_id
        self.visitor_name = visitor_name
        self.visitor_age = visitor_age
        self.visitor_agecategory = visitor_agecategory
        self.visitor_email = visitor_email

    def __str__(self): # adding the f string to show the visitors information
        return f"""
        Visitor ID: {self.visitor_id}
        Visitor's name: {self.visitor_name}
        Visitor's age: {self.visitor_age}
        Visitor's age category: {self.visitor_agecategory}
        Visitor's email: {self.visitor_email}
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

    def setvisitor_agecategory(self, visitor_agecategory):
        self.visitor_agecategory = visitor_agecategory
    def getvisitor_agecategory(self):
        return self.visitor_agecategory

    def setvisitor_email(self, visitor_email):
        self.visitor_email = visitor_email
    def getvisitor_email(self):
        return self.visitor_email

class Ticket: # code constructors to initialise the tickets attributes
    def __init__(self, ticketid, ticketprice, visitingdate):
        self.ticketid = ticketid
        self.ticketprice = ticketprice
        self.visitingdate = visitingdate

    def __str__(self): # adding the f string to show the tickets information
        return f"""
        Ticket's ID: {self.ticketid}
        Ticket's Price: {self.ticketprice} AED
        Visiting date: {self.visitingdate}
        """

    # Setters and getters for all the Specified attributes
    def setticketid(self, ticketid):
        self.ticketid = ticketid
    def getticketid(self):
        return self.ticketid

    def setticketprice(self, ticketprice):
        self.ticketprice = ticketprice
    def getticketprice(self):
        return self.ticketprice

    def setvisitingdate(self, visitingdate):
        self.visitingdate = visitingdate
    def getvisitingdate(self):
        return self.visitingdate

# objects to test the code
eventa = Event('A7-097N-88', 'Ethr coffee', '12-03-2024', '10-04-2024', 'Outdoor wing')
visitora = Visitor('784-2003-2897489', 'HAMDA ALMANSOORI', '20', 'Adult', 'hamda.almansoori@gmail.com')
ticketa = Ticket('T-07738', '20', '31-0402024')

print(eventa)
print(visitora)
print(ticketa)
