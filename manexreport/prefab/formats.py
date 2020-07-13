
###############################################################################
#   file:       podunk/widget/formats.py
#   author:     Jim Storch, Manuel Vega
###############################################################################

import locale

# ------------------------------------------------------------------Format Plain


def format_plain(value):
    """
    Returns value cast to a string.  This is the default for Field.
    """
    foo = locale.setlocale(locale.LC_ALL, ('en_US', 'utf8'))
    if value is None:
        retval = ''
    else:
        retval = value
    return retval

# -----------------------------------------------------------Format Two Decimals


def format_two_decimals(value):
    """
    Returns value rounded to two decimal places.    
    """
    foo = locale.setlocale(locale.LC_ALL, ('en_US', 'utf8'))
    if value is None:
        retval = ''
    else:
        retval = locale.format("%.2f", float(value), True)
    return retval

# -----------------------------------------------------------Format Three Decimals


def format_three_decimals(value):
    """
    Returns value rounded to three decimal places.
    """
    foo = locale.setlocale(locale.LC_ALL, ('en_US', 'utf8'))
    if value is None:
        retval = ''
    else:
        retval = locale.format("%.3f", float(value), True)
    return retval

# -----------------------------------------------------------Format US Currency


def format_us_currency(value):
    """
    Returns value in monetary format, 2 decimal places, comma separated
    every three digits with a leading dollar sign.
    """
    foo = locale.setlocale(locale.LC_ALL, ('en_US', 'utf8'))
    if value is None:
        retval = ''
    else:
        retval = '$ ' + locale.format("%.2f", float(value), True)
    return retval

# ------------------------------------------------------------------Format Title


def format_title(value):
    """
    Returns A String In Title Case
    """
    if value is None:
        retval = ''
    else:
        # retval = str(value).title()
        retval = str(value)
    return retval

# ------------------------------------------------------------------Format DMYHM


def format_dmyhm(value):
    """
    Returns the date and time in the format DD/MM/YY HH:MM. 
    """
    if value is None:
        retval = ''
    else:
        retval = value.strftime('%m/%d/%y %H:%M')
    return retval

# ------------------------------------------------------------Format Report Date


def format_report_date(value):
    """
    Returns the date and time in the format 'Jul 03, 2008 - 09:11 AM'
    """
    if value is None:
        retval = ''
    else:
        month = get_month_spanish_fullname(value.strftime('%m'))
        retval = '%s/%s/%s%s' % (value.strftime('%d'), month, value.strftime('%Y'), value.strftime(' - %H:%M:%S'))
    return retval


def get_month_spanish_fullname(month):
    month_spanish = ''
    if month == u'01':
        month_spanish = 'Enero'
    if month == u'02':
        month_spanish = 'Febrero'
    if month == u'03':
        month_spanish = 'Marzo'
    if month == u'04':
        month_spanish = 'Abril'
    if month == u'05':
        month_spanish = 'Mayo'
    if month == u'06':
        month_spanish = 'Junio'
    if month == u'07':
        month_spanish = 'Julio'
    if month == u'08':
        month_spanish = 'Agosto'
    if month == u'09':
        month_spanish = 'Septiembre'
    if month == u'10':
        month_spanish = 'Octubre'
    if month == u'11':
        month_spanish = 'Noviembre'
    if month == u'12':
        month_spanish = 'Diciembre'
    return month_spanish
