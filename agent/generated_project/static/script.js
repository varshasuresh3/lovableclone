let num1 = document.getElementById('num1');
let num2 = document.getElementById('num2');
let operation = document.getElementById('operation');
let calculate = document.getElementById('calculate');
let result = document.getElementById('result');

import { Calculator } from './calculator.js';
import { render_template } from 'flask';

class ClientScript {
  constructor(calculator) {
    this.calculator = calculator;
  }

  handleInput() {
    let n1 = parseFloat(num1.value);
    let n2 = parseFloat(num2.value);
    let op = operation.value;
    let res;
    switch (op) {
      case 'add':
        res = this.calculator.add(n1, n2);
        break;
      case 'subtract':
        res = this.calculator.subtract(n1, n2);
        break;
      case 'multiply':
        res = this.calculator.multiply(n1, n2);
        break;
      case 'divide':
        res = this.calculator.divide(n1, n2);
        break;
      default:
        res = 'Invalid operation';
    }
    result.innerText = 'Result: ' + res;
  }
}

calculate.addEventListener('click', function() {
  let calculator = new Calculator();
  let clientScript = new ClientScript(calculator);
  clientScript.handleInput();
});