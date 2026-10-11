"""Offline catalogue matching extraction. No requests or automatic writes."""
import difflib

def match_product(name, unit_price, catalog, category="", aliases=None):
    aliases = aliases or {}
    target = name.lower().strip()
    category = category.lower().strip()
    
    key_preco = f"{target}|{unit_price:.2f}"
    if key_preco in aliases:
        target = aliases[key_preco]
    elif f"{target}|{category}" in aliases:
        target = aliases[f"{target}|{category}"]
    elif target in aliases:
        target = aliases[target]
    
    def achar_match(candidatos_lista):
        matches_preco = [p for p in candidatos_lista if abs(p['price'] - unit_price) <= 0.05]
        if not matches_preco:
            return None
        if len(matches_preco) == 1:
            return matches_preco[0]['id']
        if category:
            matches_cat = [p for p in matches_preco if category in p.get('category', '') or p.get('category', '') in category]
            if matches_cat:
                return matches_cat[0]['id']
        return matches_preco[0]['id']
    
    if target in catalog:
        match_id = achar_match(catalog[target])
        if match_id:
            return match_id, target
            
    matches = difflib.get_close_matches(target, catalog.keys(), n=5, cutoff=0.50)
    for closest in matches:
        match_id = achar_match(catalog[closest])
        if match_id:
            return match_id, closest
            
    return None, None


