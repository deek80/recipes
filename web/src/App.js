import React from "react";
import Instruction from "./components/Instruction";
import test_recipe from "./test/get_recipe.json";

const App = () => {
  //console.log(test_recipe.instructions);
  return <Instruction {...test_recipe.instructions[0]} />;
};

export default App;
