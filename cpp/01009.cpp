int bitwiseComplement(int n) {
    int ones = 1;
    while(ones < n) {
        ones = (ones << 1) + 1;
    }
    return ones - n;
}