struct CustomStack {
    stack: Vec<i32>,
    stack_size: i32,
    max_size: i32
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CustomStack {

    fn new(maxSize: i32) -> Self {
        CustomStack {
            stack: Vec::new(),
            stack_size: 0,
            max_size: maxSize
        }
    }
    
    fn push(&mut self, x: i32) {
        if self.stack_size < self.max_size {
            self.stack.push(x);
            self.stack_size += 1;
        }
    }
    
    fn pop(&mut self) -> i32 {
        if let Some(val) = self.stack.pop() {
            self.stack_size -= 1;
            val
        }
        else {
            -1
        }
    }
    
    fn increment(&mut self, k: i32, val: i32) {
        for i in 0..(k.min(self.stack_size)) {
            self.stack[i as usize] += val;
        }
    }
}