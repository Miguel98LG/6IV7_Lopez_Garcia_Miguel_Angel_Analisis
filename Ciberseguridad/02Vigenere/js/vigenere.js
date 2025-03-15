var vigenere = vigenere || (function(){

    //Aqui tenemos que crear una funcion que se encargue de obtener el texto, desplazamiento y si va a cifrar o descifrar

    var proceso = function(txt, desp, action){
        var replace = (function(){
            //ABC
            var abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
            var longitud = abc.length;

            return function(c){
                var i = abc.indexOf(c.toLowerCase());
                if(i != -1){
                    var pos = i;
                    if(action){
                        //cifrar
                        pos += desp;
                        pos = (pos >= longitud) ? pos - longitud : pos;
                    } else {
                        pos -= desp;
                        pos = (pos < 0) ? pos + longitud : pos;
                    }
                    return abc[pos];
                }
                return c;
            };
        })();

        //hay que validar la cadena
        var re = (/([a-zñ])/ig);
        return String(txt).replace(re, function(match){
            return replace(match);
        });
    };
    return {
        //vamos a saber si queremos cifrar o descifrar
        encode : function(txt, desp){
            return proceso(txt, desp, true);
        },
        decode : function(txt, desp){
            return proceso(txt, desp, false);
        }
    };
})();


//cifrar
function codificar() {
    var texto = document.getElementById('txt').value.trim();
    var clave = document.getElementById('txtclave').value.trim();

    if (texto === "" || clave === "") {
        alert("Por favor, ingresa tanto el texto como la clave.");
        return;
    }

    if (clave.length > texto.length) {
        alert("La clave no puede ser más larga que el texto.");
        return;
    }

    var resultado = "";
    var indiceclave = 0;
    var charartexto = texto.split('');

    for (var i = 0; i < charartexto.length; i++) {
        var desp = obindiceClave(clave.charAt(indiceclave));  // Desplazamiento basado en la clave
        var chartexto = charartexto[i];

        resultado += vigenere.encode(chartexto, (desp >= 26 ) ? desp % 26 : desp);

        indiceclave++;
        if (indiceclave >= clave.length) {
            indiceclave = 0;
        }
    }

    document.getElementById("respuesta").value = resultado;
}

function obindiceClave(reco) {
    var abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    return abc.indexOf(reco.toLowerCase());
}

//decifrar
function descifrar() {
    var texto = document.getElementById('txt').value.trim();
    var clave = document.getElementById('txtclave').value.trim();
    var resultado = "";

    if (texto === "" || clave === "") {
        alert("Por favor, ingresa tanto el texto como la clave.");
        return;
    }

    if (clave.length > texto.length) {
        alert("La clave no puede ser más larga que el texto.");
        return;
    }

    var indiceclave = 0;
    var charartexto = texto.split('');

    for (var i = 0; i < charartexto.length; i++) {
        var desp = obindiceClave(clave.charAt(indiceclave));  // Desplazamiento basado en la clave
        var chartexto = charartexto[i];

        if (desp === -1) {
            resultado += chartexto;  // Si el carácter no es una letra válida, lo dejamos sin descifrar
        } else {
            resultado += vigenere.decode(chartexto, desp);
        }

        indiceclave++;
        if (indiceclave >= clave.length) {
            indiceclave = 0;  // Reiniciar el índice de la clave si se excede
        }
    }

    document.getElementById("respuesta").value = resultado;
}

// Agregar los eventos de los botones al HTML
document.getElementById("cifrar").addEventListener("click", codificar);
document.getElementById("descifrar").addEventListener("click", descifrar);
document.getElementById("reiniciar").addEventListener("click", reiniciar);

// Función para reiniciar los campos
function reiniciar() {
    document.getElementById('txt').value = '';
    document.getElementById('txtclave').value = '';
    document.getElementById('respuesta').value = '';
}