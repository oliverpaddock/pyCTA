import csv
from os.path import exists
import requests

Routes = {
    "red"    : "red",
    "blue"   : "blue",
    "brown"  : "brn",
    "green"  : "g",
    "orange" : "org",
    "purple" : "p",
    "pink"   : "pink",
    "yellow" : "y"
}

def ctaSetKey(key:str):
    global __ctakey__
    __ctakey__ = key

def ctaGetKey():
    return __ctakey__

def ctaGetPositionData(getUrl:str):
    """
    Returns a dictionary of data for query string with base url

    http://lapi.transitchicago.com/api/1.0/ttpositions.aspx
    """
    positions = requests.get(getUrl).json()
    newData = positions['ctatt']
    newRoutes = newData['route']

    csvData = []

    for route in newRoutes:
        if len(route) > 0:
            for train in route['train']:
                csvData.append({
                    'tmst'       : newData['tmst'], 
                    'errCd'      : newData['errCd'], 
                    'errNm'      : newData['errNm'], 
                    'route'      : route['@name'],
                    'rn'         : train['rn'], 
                    'destSt'     : train['destSt'], 
                    'destNm'     : train['destNm'], 
                    'trDr'       : train['trDr'], 
                    'nextStaId'  : train['nextStaId'], 
                    'nextStpId'  : train['nextStpId'], 
                    'nextStaNm'  : train['nextStaNm'], 
                    'prdt'       : train['prdt'], 
                    'arrT'       : train['arrT'], 
                    'isApp'      : train['isApp'], 
                    'isDly'      : train['isDly'], 
                    'flags'      : train['flags'], 
                    'lat'        : train['lat'], 
                    'lon'        : train['lon'], 
                    'heading'    : train['heading']
                })

    return csvData

def ctaWritePositionsCSV(path:str, write:str, rts=None):
    """
    Writes current CTA data to csv file in specified path. If file does not exist, creates a file.

    Parameters:

    path - path/to/csv
    write - 'w' to write new data or 'a' to append data to file.
    rts - list of routes to gather data for. See documentation for more details
    """

    rtStr = ''

    if not rts:
        rts = Routes
    
    if isinstance(rts, (list,tuple)):
        for rt in rts:
            rtStr += f'&rt={rt}'
    elif isinstance(rts, dict):
        for key in rts:
            rtStr += f'&rt={rts[key]}'
    elif isinstance(rts, str):
        if rts[0:4].lower() == '&rt=':
            rtStr = rts.lower()
        else:
            rtStr = f'&rt={rts}'

    rtcheck = rtStr.split('&rt=')[1:]

    # assert that arguments are in correct format
    assert (r in Routes.values() for r in rtcheck), 'Incorrect route format'
    assert write in ('w', 'a'), 'variable \'write\' must be either \'w\' or \'a\''

    # create the file if does not exist
    if not exists(path):
        write += '+' # 'w+' and 'a+' create the file if it does not exist

    # query data
    getUrl = f'http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key={__ctakey__}{rtStr}&outputType=JSON'
    data = ctaGetPositionData(getUrl)

    f = open(path, write, encoding='UTF8', newline='')

    # data headers for csv file
    header = ['tmst', 'errCd', 'errNm', 'route', 'rn', 
            'destSt', 'destNm', 'trDr', 'nextStaId', 
            'nextStpId', 'nextStaNm', 'prdt', 'arrT', 
            'isApp', 'isDly', 'flags', 'lat', 'lon', 'heading']

    writer = csv.DictWriter(f, header)

    if write != 'a':
        writer.writeheader()
    
    writer.writerows(data)
    f.close()