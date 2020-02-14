class MeetResults():
    """Stores and retrieves meet result data.

    Data is organized into 2 (really 3, 2 of which are split by men/women)
    dictionaries:

        event data   - keyed by event name, each value is a dictionary
                       (k,v) where k = swimmer name and
                                   v = their time in the event
        swimmer data - keyed by swimmer name, returns dictionary containing:
                          KEY      VALUE
                          age    : an integer age of the swimmer
                          team   : a string that is the swimmer's team
                          events : a list of event name strings

    It is an checked runtime error to report a result for the same event for
    a swimmer with the same name.
    """
    def __init__(self):
        self.mens_events   = {}
        self.womens_events = {}
        self.swimmers      = {}

    def __swimmer_exists(self, swimmer):
        """Raises an exception if the given swimmer did not participate in
        this meet.

        Args:
            swimmer (str): a string that is the swimmer's name

        Raises:
            NameError: No such swimmer in this meet
        """
        if swimmer not in self.swimmers:
            raise NameError('No such swimmer in this meet')

    def __select_events(self, gender):
        """Given a gender, returns the events dictionary for that gender.

        Args:
            gender (str): a string representing the swimmer's gender

        Raises:
            KeyError: 'Men' or 'Women' (case sensitive) must be supplied

        Returns:
            events: a reference to the events dictionary for the
                    corresponding gender
        """
        switch = {
            'Men':   self.mens_events,
            'Women': self.womens_events
        }
        events = switch[gender]

        return events

    def report_result(self, gender, result):
        """Takes a gender and an event result and adds the swimmer and time to
        the events dictionary for the corresponding gender and, if the swimmer
        has not yet been added to it, adds the swimmer to the
        swimmers dictionary.

        A result is a dictionary containing:
            KEY       VALUE
            swimmer : a string that is the swimmer's name
            age     : an integer age of the swimmer
            team    : a string that is the swimmer's team
            event   : a string that is the event name
            time    : a timedelta object that is the swimmer's recorded time

        Reporting a result for a swimmer of the same name in the same event
        raises a NameError exception.
        """
        events = self.__select_events(gender)

        # Add result data to events dictionary for corresponding gender
        if result['event'] not in events:
            events[result['event']] = {}
            events[result['event']][result['swimmer']] = result['time']
        else:
            if result['swimmer'] in events[result['event']]:
                raise NameError('Duplicate swimmer added to event')
            else:
                events[result['event']][result['swimmer']] = result['time']

        # add swimmer data to swimmers dictionary
        if result['swimmer'] not in self.swimmers:
            new_entry = result.copy()
            del new_entry['time']
            event = new_entry['event']
            del new_entry['event']
            new_entry['events'] = []
            new_entry['events'].append(event)
            new_entry['gender'] = gender
            self.swimmers[result['swimmer']] = new_entry
        else:
            self.swimmers[result['swimmer']]['events'].append(result['event'])

    def get_events(self, swimmer):
        """Given a swimmer name, returns a list of events they were in.

        Args:
            swimmer (str): a string that is the swimmer's name

        Raises:
            NameError: No such swimmer in this meet

        Returns:
            events: a string list of events the swimmer participated in.
        """
        self.__swimmer_exists(swimmer)

        return self.swimmers[swimmer]['events']

    def get_result(self, swimmer, event):
        """Given a swimmer name and event name, returns a timedelta object
        representing their time in that event.

        Args:
            swimmer (str): a string that is the swimmer's name
            event (str)  : a string that is the event name

        Raises:
            NameError: No such swimmer in this meet
            NameError: No such event
            NameError: No such swimmer in this event

        Returns:
            time: a timedelta object representing the swimmer's time in
                  the event
        """
        self.__swimmer_exists(swimmer)
        events = self.__select_events(self.swimmers[swimmer]['gender'])
        if event not in events:
            raise NameError('No such event')
        else:
            results = events[event]
            if swimmer not in results:
                raise NameError('No such swimmer in this event')
            else:
                return results[swimmer]
