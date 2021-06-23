import React from "react";
import Ingredient from "./Ingredient";

const Instruction = ({id, data}) => (
  <div>
    <span>Instruction</span>
    <span>{id}</span>
    <span>{data.details}</span>
    <span>Ingredients:</span>
    <ul>
      {data.required.ingredients.map(({name, amount}) => (
        <li>
          <Ingredient name={name} amount={amount} />
        </li>
      ))}
    </ul>
  </div>
);

export default Instruction;
