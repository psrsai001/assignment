function ask(question, yes, no) {
  if (confirm(question)) yes();
  else no();
}

function showOk() {
  alert("You agreed.");
}

function showCancel() {
  alert("You canceled the execution.");
}

// usage: functions showOk, showCancel are passed as arguments to ask
ask("Do you agree?", showOk, showCancel);

{
  function a() {
    console.log("I am a");
    function b() {
      console.log("I am b");
    }
    b();
  }
}

a();
b(); // should not work as the functions are block scoped.
console.log(a);
