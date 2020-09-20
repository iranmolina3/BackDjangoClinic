const nombre1 = document.getElementById("NOMBRE1")
const nombre2 = document.getElementById("NOMBRE2")
const apellido1 = document.getElementById("APELLIDO1")
const apellido2 = document.getElementById("APELLIDO2")
const dpi = document.getElementById("DPI")
const genero = document.getElementById("GENERO")
const edad = document.getElementById("EDAD")
const fecha_nacimiento = document.getElementById("FECHA_NACIMIENTO")
const fk_estado_civil = document.getElementById("FK_ESTADO_CIVIL")
const telefono = document.getElementById("TELEFONO")
const direccion = document.getElementById("DIRECCION")
const municipio = document.getElementById("MUNICIPIO")

const form = document.getElementById("FORM")
const parrafo = document.getElementById("warnings")

form.addEventListener('submit', e=>{
    let warnings = ""
    let regexNumero = /^[0-9]+$/
    let regexLetras = /^[A-Za-z]+$/
    let correcto = false
    //let regexEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
    if(nombre1.value.length>25 || nombre1.value.length<3){
        //alert("Primer nombre muy largo")
        warnings+='Primer nombre muy largo o corto<br>'
        if(!regexLetras.test(nombre1.value)){
            //alert("Solo ingresar numeros para dpi")
            warnings+='Primer nombre solo letras<br>'
            correcto=true
        }
        correcto=true
    }
    if(nombre2.value.length>25 || nombre2.value.length<3){
        //alert("Primer nombre muy largo")
        warnings+='Segundo nombre muy largo o corto<br>'
        if(!regexLetras.test(nombre2.value)){
            //alert("Solo ingresar numeros para dpi")
            warnings+='Segundo nombre solo letras<br>'
            correcto=true
        }
        correcto=true
    }
    if(apellido1.value.length>25 || apellido1.value.length<2){
        //alert("Primer nombre muy largo")
        warnings+='Primer apellido muy largo o corto<br>'
        if(!regexLetras.test(apellido1.value)){
            //alert("Solo ingresar numeros para dpi")
            warnings+='Primer apellido solo letras<br>'
            correcto=true
        }
        correcto=true
    }
    if(apellido1.value.length>25 || apellido1.value.length<2){
        //alert("Primer nombre muy largo")
        warnings+='Segundo apellido muy largo o corto<br>'
        if(!regexLetras.test(apellido1.value)){
            //alert("Solo ingresar numeros para dpi")
            warnings+='Segundo apellido solo letras<br>'
            correcto=true
        }
        correcto=true
    }
    if(dpi.value.length>13){
        //alert("Solo ingresar numeros para dpi")
        warnings+='El dpi no debe ser mayor a 13 digitos<br>'
        if(!regexNumero.test(dpi.value)){
            //alert("Solo ingresar numeros para dpi")
            warnings+='Solo ingresar numeros para dpi<br>'
            correcto=true
        }
        correcto=true
    }
    if(edad.value>150){
        warnings+='La edad no puede se mayor de 150 es improbable<br>'
        correcto=true
    }
    if(edad.value>150 || edad.value<=0){
        warnings+='Edad no debe se menor a 1 año y mayor 150 años<br>'
        correcto=true
    }
    if(telefono.value.length!=8){
        warnings+='El telefono ser igual a 8 digitos<br>'
        if(!regexNumero.test(telefono.value)){ff
            warnings+='El telefono solo debe de ser numero<br>'
            correcto=true
        }
        correcto=true
    }
    if(direccion.value.length>199){
        warnings+='Resumir la direccion'
        correcto=true
    }
    //console.log(!regexNumero.test(dpi.value))
    //console.log(correcto)
    if(correcto){
        parrafo.innerHTML=warnings
        e.preventDefault()
    }

})
