def expiration_date(bloodType):
    if bloodType == 'complete':
        return 35
    if bloodType == 'plasma':
        return 365
    if bloodType == 'platelet':
        return 5
