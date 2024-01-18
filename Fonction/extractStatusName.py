def extractStatusName(page):
    status = page['properties'].get('État', {}) 
    return status.get('status', {}).get('name', '')