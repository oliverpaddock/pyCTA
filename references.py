from stops import stops

class Error:
    """
    References for error messages for each of the Train Tracker API's.
    
    References available for Arrivals, Positions, and Follow.
    """
    class Arrivals:
        ref = {
            0   : {'message' : 'OK',                                                  'description' : 'No error.'},
            100 : {'message' : 'Required parameter [value] is missing.',              'description' : 'The query string does not contain one of the required parameters, currently: "mapid or stpid", "key".'},
            101 : {'message' : 'Invalid API key',                                     'description' : 'The value for the required parameter "key" is not a valid API key.'},
            102 : {'message' : 'Maximum Daily CTA Train Tracker API usage exceeded.', 'description' : 'The number of successful API Requests using the supplied "key" have exceeded the maximum daily value.'},
            103 : {'message' : 'Invalid mapid: [value]',                              'description' : 'At least one of the supplied values for the "mapid" parameter is not valid. The first invalid id is returned.'},
            104 : {'message' : 'Mapid\'s need to be integers: [value]',               'description' : 'At least one of the supplied values for the "mapid" parameter is not an integer value. The first invalid id is returned.'},
            105 : {'message' : 'Maximum of mapid\'s you can request is 4.',           'description' : 'A maximum of 4 values may be specified for the parameter "mapid". More than 4 were supplied.'},
            106 : {'message' : 'Invalid Route Identifier: [value]',                   'description' : 'At least one of the supplied values for the "rt" parameter is invalid. Supported values are: "Red", "Blue", "Brn", "G", "Org", "P", "Pink", "Y".'},
            107 : {'message' : 'Maximum of rt\'s you can request is 4.',              'description' : 'A maximum of 4 values may be specified for the parameter "rt". More than 4 were supplied.'},
            108 : {'message' : 'Invalid stpId specified: [value]',                    'description' : 'At least one of the supplied values for the "stpId" parameter is invalid. The first invalid value is returned.'},
            109 : {'message' : 'Maximum of stpid\'s you can request is 4.',           'description' : 'A maximum of 4 values may be specified for the parameter "stpId". More than 4 were supplied.'},
            110 : {'message' : 'Invalid max specified: [value]',                      'description' : 'A non-integer value was specified for the "max" parameter.'},
            111 : {'message' : 'Parameter \'max\' must be a positive integer.',       'description' : 'A value less than 1 was specified for the "max" parameter. The value must be an integer greater than zero.'},
            112 : {'message' : 'Stpid\'s need to be integers: [value]',               'description' : 'At least one of the supplied values for the "stpid" parameter is not an integer value. The first invalid id is returned.'},
            500 : {'message' : 'Invalid parameter: [value]',                          'description' : 'The query string contains a parameter that is not supported by the train tracker API, currently supported parameters are: "mapid", "key", "rt", "stpid", "max".'},
            900 : {'message' : 'Server Error',                                        'description' : 'A server error occurred.'}
        }

        def err(errCd:int, detail=False):
            """
            Returns the description of specified error code.

            Optional parameter 'detail' set to True will return a more detailed description of error code.
            """
            if errCd not in Error.Arrivals.ref.keys():
                raise ValueError('Error code not found')
            if detail:
                return Error.Arrivals.ref[errCd]['description']
            return Error.Arrivals.ref[errCd]['message']

    class Positions:
        ref = {
            0   : {'message' : 'OK',                                              'description' : 'No error.'},
            100 : {'message' : 'Required parameter [value] is missing.',          'description' : 'One of the required parameters (rt, key) was not provided.'},
            101 : {'message' : 'Invalid API key',                                 'description' : 'The API key given in the parameter \'key\' was either not found or inactive.'},
            102 : {'message' : 'Maximum Daily Train Tracker API usage exceeded.', 'description' : 'Key usage has exceeded daily limits. Limits are reset at midnight.'},
            106 : {'message' : 'Invalid Route Identifier: [value]',               'description' : 'Valid route identifiers are: red, blue, brn, g, org, p, pink, y'},
            107 : {'message' : 'Maximum of rt\'s you can request is 4.',          'description' : 'No more than 8 routes can be issued per request. Note duplicates are counted but not returned.'},
            500 : {'message' : 'Invalid parameter: [value]',                      'description' : 'The indicated parameter is not valid. Valid parameters are: rt, key.'},
            900 : {'message' : 'Server Error',                                    'description' : 'A server error occurred.'}
        }

        def err(errCd:int, detail=False):
            """
            Returns the description of specified error code.

            Optional parameter 'detail' set to True will return a more detailed description of error code.
            """
            
            if errCd not in Error.Positions.ref.keys():
                raise ValueError('Error code not found')
            if detail:
                return Error.Positions.ref[errCd]['description']
            return Error.Positions.ref[errCd]['message']
        
    class Follow:
        ref = {
            0   : {'message' : 'OK',                                              'description' : 'No error.'},
            100 : {'message' : 'Required parameter [value] is missing.',          'description' : 'One or more of the required parameters is missing. For this API, the required parameters are: “runnumber”, and “key”'},
            101 : {'message' : 'Invalid API key',                                 'description' : 'The supplied API key was not a valid API key.'},
            102 : {'message' : 'Maximum Daily Train Tracker API usage exceeded.', 'description' : 'The daily usage limit for the supplied key has been exceeded.'},
            500 : {'message' : 'Invalid parameter: [value]',                      'description' : 'Valid parameters for this API are: “runnumber”, and “key”.'},
            501 : {'message' : 'No trains with runnumber [value] were found.',    'description' : 'The indicated train may have left service or may simply be incorrect.'},
            502 : {'message' : 'Unable to determine upcoming stops.',             'description' : 'The indicated train has an unexpected exit station id, and the system cannot reliably determine which predictions to report.'},
            503 : {'message' : 'Unable to find predictions.',                     'description' : 'The train exists, however none of the available predictions are for active stations.'},
            900 : {'message' : 'Server Error',                                    'description' : 'A server error occurred.'}
        }

        def err(errCd:int, detail=False):
            """
            Returns the description of specified error code.

            Optional parameter 'detail' set to True will return a more detailed description of error code.
            """
            if errCd not in Error.Follow.ref.keys():
                raise ValueError('Error code not found')
            if detail:
                return Error.Follow.ref[errCd]['description']
            return Error.Follow.ref[errCd]['message']

class Query:
    """
    String query references for Train Tracker APIs, and parameter descriptions.
    
    References available for Arrivals, Positions, and Follow.
    """
    class Arrivals:
        query = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'

        params = {
            'mapid' : {'value' : 'Numeric station identifier (required if stpid not specified)', 'description' : 'A single five-digit code to tell the server which station you\'d like to receive predictions for. See appendix for information about valid station codes.'},
            'stpid' : {'value' : 'Numeric stop identifier (required if mapid not specified)',    'description' : 'A single five-digit code to tell the server which specific stop (in this context, specific platform or platform side within a larger station) you\'d like to receive predictions for. See appendix for information about valid stop codes.'},
            'max'   : {'value' : 'Maximum results (optional)',                                   'description' : 'The maximum number you\'d like to receive (if not specified, all available results for the requested stop or station will be returned)'},
            'rt '   : {'value' : 'Route code (optional)',                                        'description' : 'Allows you to specify a single route for which you\'d like results (if not specified, all available results for the requested stop or station will be returned)'},
            'key'   : {'value' : 'Alphanumeric API key (required)',                              'description' : 'Your unique API key, assigned to you after agreeing to DLA and requesting a key be generated for you.'},
        }

        def paramDesc(param:str, detail=False):
            """
            Returns the description of specified paramater.

            Optional arg 'detail' set to True will return a more detailed description of parameter
            """
            if param not in Query.Arrivals.params.keys():
                raise ValueError('Parameter not found')
            if detail:
                return Query.Arrivals.params[param]['description']
            return Query.Arrivals.params[param]['value']

    class Positions:
        query = 'http://lapi.transitchicago.com/api/1.0/ttpositions.aspx'

        params = {
            'rt' : {'value' : 'Train route(s) (required)', 'description' : 'Allows you to specify one or more routes for which you\'d like train location information.'},
            'key' : {'value' : 'Alphanumeric API key (required)', 'description' : 'Your unique API key, assigned to you after agreeing to DLA and requesting a key be generated for you.'}
        }

        def paramDesc(param:str, detail=False):
            """
            Returns the description of specified paramater.

            Optional arg 'detail' set to True will return a more detailed description of parameter
            """
            if param not in Query.Positions.params.keys():
                raise ValueError('Parameter not found')
            if detail:
                return Query.Positions.params[param]['description']
            return Query.Positions.params[param]['value']

    class Follow:
        query = 'lapi.transitchicago.com/api/1.0/ttfollow.aspx'

        params = {
            'runnumber' : {'value' : 'Train Run Number (required)',     'description' : 'Allows you to specify a single run number for a train for which you\'d like a series of upcoming arrival estimations.'},
            'key'       : {'value' : 'Alphanumeric API key (required)', 'description' : 'Your unique API key, assigned to you after agreeing to DLA and requesting a key be generated for you.'}
        }

        def paramDesc(param:str, detail=False):
            """
            Returns the description of specified paramater.

            Optional arg 'detail' set to True will return a more detailed description of parameter
            """
            if param not in Query.Follow.params.keys():
                raise ValueError('Parameter not found')
            if detail:
                return Query.Follow.params[param]['description']
            return Query.Follow.params[param]['value']


class Stops:
    """
    Reference for stops.

    Get stop IDs, stop names, and other information about specific stops for all CTA train stops.
    """
    _stops = stops

    stopIDs = list(set(stops[i]['stop_id'] for i in range(len(stops))))
    stopNames = list(set(stops[i]['stop_name'] for i in range(len(stops))))
    stopIDs.sort()
    stopNames.sort()

    def getStop(stp):
        """
        Returns a dict of information about specified stop.

        'stp' can be stop ID (int) or stop name (str). See Stops.stopIDs or Stops.stopNames for a list of available stops.
        """
        if type(stp) == str:
            for stop in Stops._stops:
                if stop['stop_name'] == stp:
                    return stop
            raise KeyError('Enter valid stop ID or stop name')
            
        elif type(stp) == int:
            for stop in Stops._stops:
                if stop['stop_id'] == stp:
                    return stop
            raise KeyError('Enter valid stop ID or stop name')
            
        else:
            raise KeyError('Enter valid stop ID or stop name')

class Routes:
    """
    Reference for CTA train routes.

    Get route names, codes (for query), and direction codes 
    """
    names = ['red', 'blue', 'brown', 'green', 'orange', 'purple', 'pink', 'yellow']

    codes = {
        'red'    : 'red',
        'blue'   : 'blue',
        'brown'  : 'brn',
        'green'  : 'g',
        'orange' : 'org',
        'purple' : 'p',
        'pink'   : 'pink',
        'yellow' : 'y'
    }

    directions = {
        'red'  : {1: 'Howard', 5: '95th/Dan Ryan'},
        'blue' : {1: 'O\'Hare', 5: 'Forest Park'},
        'brn'  : {1: 'Kimball', 5: 'Loop'},
        'g'    : {1: 'Harlem/Lake', 5: 'Ahsland/63rd or Cottage Grove'},
        'org'  : {1: 'Loop', 5: 'Midway'},
        'p'    : {1: 'Linden', 5: 'Howard or Loop'},
        'pink' : {1: 'Loop', 5: '54th/Cermak'},
        'y'    : {1: 'Skokie', 5: 'Howard'}
    }

    def code(rt):
        """
        Returns code name for specified route.
        """
        return Routes.codes[rt]

    def direction(rt, dir=None):
        """
        Returns direction names for specified route.
        If 'dir' is specified (1 or 5), returns only that direction
        """
        if dir:
            return Routes.directions[Routes.code(rt)][dir]
        else:
            return Routes.directions[Routes.code(rt)]