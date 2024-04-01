class artwork:# code constructors to initialised the artwoks attributes
    def __init__(self, id , title, artist, datecreated,significance,location):
        self.id=id
        self.title=title
        self.artist=artist
        self.significance=significance
        self.datecreated=datecreated
        self.location=location

    def __str__(self):# adding the f string to represt the artworks information
        return f"""
        Artwork's ID:{self.id}
        Artwork's Title: {self.title}
        Artwork Was made by the Artist : {self.artist}
        The Artwork Was crated on the :{self.datecreated}
        Its Historical significance is : {self.significance}
        You can vist the Art work in : {self.location}
        """

    # setter and getters for the id
    def setid(self, id):
        self.id = id
    def getid(self):
        return self.id

    # setter and getters for the title
    def settitle(self, title):
        self.title = title
    def gettitle(self):
        return self.title

    # setter and getters for the artist
    def setartist(self, artist):
        self.artist = artist
    def getartist(self):
        return self.artist

    # setter and getters for the Date created
    def setdatecreated(self, datecreated):
        self.datecreated = datecreated
    def getdatecreated(self):
        return self.datecreated

    # setter and getters for the historical significance
    def setsignificance(self, significance):
        self.historical_significance = significance
    def getsignificance(self):
        return self.significance

    # setter and getters for the historical significance
    def setlocation(self, location):
        self.location = location
    def getlocation(self):
        return self.location

class exhibition: # code constructors to initialised the exhibitions attributes
    def __init__(self,exhibitionid, exhibitionname, startdate, enddate,exhibitionlocation):
        self.exhibitionid=exhibitionid
        self.exhibitionname=exhibitionname
        self.startdate=startdate
        self.enddate=enddate
        self.exhibitionlocation=exhibitionlocation

    def __str__(self):# adding the f string to represt the Exibition information
        return f"""
        Exhibition's ID: {self.exhibitionid}
        Exhibition's Name: {self.exhibitionname}
        Exhibition's start date is {self.startdate}
        Exhibitions ends on {self.enddate}
        The exhibition can be found on the {self.exhibitionlocation}
"""
# setter and getters for the Exibitions attribiutes
    def setexhibitionid(self, exhibitionid):
        self.exhibitionid = exhibitionid
    def getexhibitionid(self):
        return self.exhibitionid

    def setexhibitionname(self, exhibitionname):
        self.exhibitionname = exhibitionname
    def getexhibitionname(self):
        return self.exhibitionname

    def setstartdate(self, startdate):
        self.startdate = startdate
    def getstartdate(self):
        return self.startdate

    def setenddate(self, enddate):
        self.enddate = enddate
    def getenddate(self):
        return self.enddate

    def setexhibitionlocation(self, exhibitionlocation):
        self.exhibitionlocation = exhibitionlocation
    def getexhibitionlocation(self):
        return self.exhibitionlocation

class musemssection: # code constructors to initialised the musems section attributes
    def __init__(self,sectionid,buildingsection,nameofsection):
        self.sectionid=sectionid
        self.buildingsection=buildingsection
        self.nameofsection=nameofsection

    def __str__(self):# adding the f string to represt the museme information
        return f"""
        Section's ID:{self.sectionid}
        It's in the {self.buildingsection} section of the building 
        Section's name: {self.nameofsection}
"""
    #setter and getters for the musesme section attributes
    def setsectionid(self,sectionid):
        self.sectionid=sectionid
    def getsectionid(self):
        return sectionid

    def setbuildingsection(self,buildingsection):
        self.buildingsection=buildingsection
    def getbuildingsection(self):
        return buildingsection

    def setnameofsection(self,nameofsection):
        self.nameofsection=nameofsection
    def getnameofsection(self):
        return nameofsection


#objects to test the code
Artwork=artwork('TF-0000','Tutti Frutti bracelet','Cartier','1929','Cartier made a special kind of jewellery called Tutti Frutti,which means all fruits in Italian.','louver abu dhabi, cartier exibition')
Exibition=exhibition('C-0000','Cartier, Islamic Inspiration and Modern Design','16 November 2023','24 March 2024','Exhibition co-organised by Louvre Abu Dhabi in the outdoor patio')
Musemsesection=musemssection('OP-1','Outdoor wing','wing 5')
print(Artwork)
print(Exibition)
print(Musemsesection)