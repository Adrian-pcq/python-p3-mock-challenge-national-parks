class NationalPark:

    def __init__(self, name):
        self.name = name
        self.trips_list = []
        self.visitors_list = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if type(name)==str and len(name)>= 3 and not hasattr(self,"name"):
            self._name = name
        
    def trips(self):
        return self.trips_list
    
    def visitors(self):
        return list(set(self.visitors_list))
    
    def total_visits(self):
        return len(self.visitors_list)
    
    def best_visitor(self):
        visitor_amount = {}
        for visitor in self.visitors_list:
            if visitor in visitor_amount:
                visitor_amount[visitor]+=1
            else:
                visitor_amount[visitor]=1
        if len(visitor_amount)==0:
            return None
        else:
            return max(visitor_amount, key = visitor_amount.get)    


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        national_park.trips_list.append(self)
        national_park.visitors_list.append(self._visitor)

        visitor.trips_list.append(self)
        visitor.national_park_list.append(self._national_park)

        self.all.append(self)


    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self,visitor):
        if isinstance(visitor,Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park= national_park

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if type(start_date)==str and len(start_date)>=7:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self,end_date):
        if type(end_date)==str and len(end_date)>=7:
            self._end_date = end_date


class Visitor:

    def __init__(self, name):
        self.name = name
        self.trips_list = []
        self.national_park_list = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if type(name)==str and 1<= len(name) <=15:
            self._name = name
        
    def trips(self):
        return self.trips_list
    
    def national_parks(self):
        return list(set(self.national_park_list))
    
    def total_visits_at_park(self, park):
        return self.national_park_list.count(park)