def extractStringFromPrompt(page):
    prompt = page['properties'].get('Prompt', {})
    formula = prompt.get('formula', {})
    return formula.get('string', '')