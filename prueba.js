function estaEntre(num1, num2, num3){
    return num1>num2 && num1<num3;
    
  }
  
function estaFueraDeRango(num1, num2, num3){
  return num1<num2 || num1>num3;
}

console.log(estaEntre(1,2,6)); 
console.log(estaFueraDeRango(5,12,27)); 

 