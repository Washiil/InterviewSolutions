def domain_name(url):
    parsed = url.replace('http://', '')
    parsed = parsed.replace('https://', '')
    parsed = parsed.replace('www.', '')
    
    val = parsed.find('.')
    return parsed[:val]

print(domain_name('http://google.com'))