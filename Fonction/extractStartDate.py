def extractStartDate(page):
    date = page['properties'].get('Date de publication', {}) 
    return date.get('date', {}).get('start', '')