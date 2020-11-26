package main

import (
	"fmt"
	"sync"
)

func main() {
	a := 0

	// change this value to 10000 to observe the race condition
	numThreads := 10000

	var wg sync.WaitGroup
	wg.Add(numThreads)

	for i := 0; i < numThreads; i++ {
		// create a goroutine, can roughly seem as a thread
		go func() {
			defer wg.Done()
			a++ // a = a + 1
		}()
	}

	wg.Wait()

	fmt.Printf("Expect a is %v, but got %v \n", numThreads, a)
}
