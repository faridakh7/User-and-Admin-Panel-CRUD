function Piramida(eded, herf)
{
    for (let i = 0; i < eded; i++) {
        var result = '';
        for (let j =0; j < eded - i; j++){
          result += ' ';
        } 
        for (let k = 0; k <= i; k++) {
          result += ' ' + herf + ' ';
        }
        console.log(result);  
    } 
}

Piramida(7,"K")