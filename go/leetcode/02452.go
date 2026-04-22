package main

func twoEditWords(queries []string, dictionary []string) []string {
	wordLength := len(queries[0])
	output := make([]string, 0, len(queries))

	edits := 0
	for _, word := range queries {
		for _, candidate := range dictionary {
			edits = 0
			for i := range wordLength {
				if word[i] != candidate[i] {
					edits += 1
				}
				if edits > 2 {
					break
				}
			}
			if edits <= 2 {
				output = append(output, word)
				break
			}
		}
	}

	return output
}
