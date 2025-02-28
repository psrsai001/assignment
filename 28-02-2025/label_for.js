outer: for (let i = 0; i < 10; ++i) {
  console.log(i);
  inner: for (let j = 0; j < 10; ++j) {
    console.log(i);
    break outer;
  }
}
