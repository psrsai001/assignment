class Stack {
  constructor() {
    this.items = [];
  }
  push(element) {
    this.items.push(element);
  }
  pop() {
    if (this.isEmpty()) {
      return "Stack empty";
    }
    return this.items.pop();
  }
  isEmpty() {
    return this.items.length === 0;
  }
  peek() {
    if (this.isEmpty()) {
      return "Stack Empty";
    }
    return this.items[this.items.length - 1];
  }
  show() {
    console.log(this.items);
  }
}

let stk = new Stack();

stk.show();
stk.push(1);
stk.push(2);
stk.push(3);
stk.show();
stk.pop();
stk.show();
console.log(stk.peek());
