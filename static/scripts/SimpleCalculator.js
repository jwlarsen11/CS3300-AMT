/* --------------------------------- slider scripts --------------------------------- */
var joutput = document.getElementById("sjout");
var fps = 310;
var weighted = .32/1000;
var joules = 1.43;
var tfps = 310;
var tjoules = 1.43;


/* ---------------------------------  weight slider --------------------------------- */
var wslider = document.getElementById("sweightSlider");
var woutput = document.getElementById("swout");
woutput.innerHTML = weighted*1000;

wslider.oninput = function() 
{
    switch(wslider.value) 
    {
    case '0':
        woutput.innerHTML = .20;
        weighted = .20/1000;
        break;
    case '1':
        woutput.innerHTML = .25;
        weighted = .25/1000;                    
        break;
    case '2':
        woutput.innerHTML = .28;
        weighted = .28/1000;                    
        break;
    case '3':
        woutput.innerHTML = .30;
        weighted = .30/1000;
        break;
    case '4':
        woutput.innerHTML = .32;
        weighted = .32/1000;
        break;
    case '5':
        woutput.innerHTML = .36;
        weighted = .36/1000;
        break;
    case '6':
        woutput.innerHTML = .40;
        weighted = .40/1000;
        break;
    case '7':
        woutput.innerHTML = .42;
        weighted = .42/1000;
        break;
    case '8':
        woutput.innerHTML = .45;
        weighted = .45/1000;
        break;
    case '9':
        woutput.innerHTML = .48;
        weighted = .48/1000;
        break;
    case '10':
        woutput.innerHTML = .50;
        weighted = .50/1000;
        break;
    case '11':
        woutput.innerHTML = .52;
        weighted = .52/1000;
        break;
    default:
        woutput.innerHTML = .32;
        weighted = .32/1000;
        break;
    }

    joules = (((1/2) * weighted) * ((fps * 0.3048) ** 2));
    joutput.innerHTML = joules.toFixed(2);
    jslider.value = joules;
}

/* --- FPS slider --- */
var fslider = document.getElementById("sFpsSlider")
var foutput = document.getElementById("sfout");
foutput.innerHTML = fps;

fslider.oninput = function() 
{
    fps = this.value;
    foutput.innerHTML = fps;

    tjoules = joules;
    joules = (((1/2) * weighted) * ((fps * 0.3048) ** 2));
    joutput.innerHTML = joules.toFixed(2);
    jslider.value = joules;
}

/* --- Joule Slider --- */
var jslider = document.getElementById("sjouleSlider");
joutput.innerHTML = joules;

jslider.oninput = function() 
{
    joules = this.value;
    joutput.innerHTML = joules;

    tfps = fps;
    fps = (Math.sqrt((2*joules)/weighted)) * 3.28084;
    foutput.innerHTML = fps.toFixed(0);
    fslider.value = fps;
}