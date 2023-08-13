def generate_hashtag(s):
    if s == '':
        return False
    
    parsed = s.strip().split(' ')
    parsed = [word.lower().title() for word in parsed]
    
    hashtag = '#' + ''.join(parsed)
    if len(hashtag) > 140:
        return False
    return hashtag
