package a

type RingBuffer struct {
	size   int
	front  int
	behind int
	data   []int
}

func (r *RingBuffer) pop() (v int) {
	if !r.isEmpty() {
		v = r.data[r.behind]
		r.behind++
		if r.behind == r.size {
			r.behind = 0
		}
	}
	// 空了
	return
}

func (r *RingBuffer) add(v int) bool {
	if !r.isFull() {
		r.data[r.front] = v
		r.front++
		if r.front == r.size {
			r.front = 0
		}
		return true
	}
	// 满了
	return false
}

func (r *RingBuffer) isFull() bool {
	var nextPoint int
	if r.front+1 < r.size {
		nextPoint = r.front + 1
	} else {
		nextPoint = 0
	}

	if nextPoint == r.behind {
		return true
	}
	return false
}

func (r *RingBuffer) isEmpty() bool {
	if r.behind == r.front {
		return true
	}
	return false
}
