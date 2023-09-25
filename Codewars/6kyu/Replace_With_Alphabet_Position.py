def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet.split()
    nums = []
    for char in text.lower():
        if char in alphabet:
            nums.append(str(alphabet.index(char) + 1))
            
	
    return ' '.join(nums)