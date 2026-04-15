func robotSim(commands []int, obstacles [][]int) int {
    var x = 0
    var y = 0

    dx := 0
    dy := 1

    maxDist := 0

    for _, cmd := range commands {
        if cmd == -2 { // left
            dx, dy = -dy, dx
        } else if cmd == -1 { // right
           dx, dy = dy, -dx
        } else {
            for range cmd {
                valid := true
                for _, obs := range obstacles {
                    if obs[0] == x + dx && obs[1] == y + dy {
                        valid = false
                        break
                    }
                }
                
                if !valid {
                    break
                }

                x += dx
                y += dy
            }

            dist := (x * x) + (y * y)
            if dist > maxDist {
                maxDist = dist
            }
        }
    }

    return maxDist
}
