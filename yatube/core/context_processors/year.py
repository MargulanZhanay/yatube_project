import datetime as dt


def year(request):
    """Add variable with current year"""
    year = dt.datetime.now().strftime('%Y')
    return {
        'year': int(year)
    }
