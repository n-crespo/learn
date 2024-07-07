// comment
document.getElementById("button").addEventListener("click", function () {
  alert("there was a cluck");
  console.log("there was a cluck");
});

//while cursor is on button, console log hello

var count = 0;
document.getElementById("button").addEventListener("mouseenter", function () {
  console.log("hello", count++);
});
