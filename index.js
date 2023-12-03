const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

function calculateNormalForce(mass, american) {
  let force;
  if (american) {
    force = parseFloat(mass) * 0.45359237 * 9.8; // Pounds to kilograms conversion
  } else {
    force = parseFloat(mass) * 9.8;
  }
  return "Your normal force is " + force.toFixed(3) + " N";
}

readline.question("Are you American? (y/n) ", function (american) {
  american = american.toLowerCase() === "y";
  const weightQuestion = american
    ? "What is your weight in pounds?\n> "
    : "What is your weight in kilograms?\n> ";

  readline.question(weightQuestion, function (weight) {
    console.log(calculateNormalForce(weight, american));
    readline.close();
  });
});
