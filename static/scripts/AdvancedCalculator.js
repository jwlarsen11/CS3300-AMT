//-------- html elements -----------------
var ajoutput = document.getElementById("ajout"); //advanced joule slider numerical output
var ajslider = document.getElementById("ajouler"); //advanced joule slider
var afslider = document.getElementById("aFpsSlider"); //advanced fps slider
var afoutput = document.getElementById("afout"); //advanced fps slider numerical output
var awslider = document.getElementById("aweightSlider"); //advanced weight slider
var awoutput = document.getElementById("awout"); //advanced weight slider numerical output
var atwslider = document.getElementById("atweightSlider"); //advanced target weight slider
var atwoutput = document.getElementById("atwout"); //advanced target weight slider numerical output

//----- advanced calculation variables ------
var amps; //mps derived from fps input
var aAccelBase; //base acceleration calculated
var aTimeBase; //base time calculated
var aweighted = .32/1000; //base mass for joule creep
var aEnergyBase; //base energy calculated for joule creep

//----- advanced bb calculated variables ------
var aBBAccel;
var aBBTime;

//---- starting variables -------
var aLength = 0.36; //length of inner barrel
var afps = 310; //starting fps value
var anweighted = .32/1000; //weighted bb input
var ajoules = 1.43; //final energy calculated including joule creep / joule input


/* --------------------------------- starting weight slider --------------------------------- */
awoutput.innerHTML = aweighted*1000; //weight output
awslider.oninput = function() 
{
    switch(awslider.value) 
    {
    case '0':
        awoutput.innerHTML = .20;
        aweighted = .20/1000;
        break;
    case '1':
        awoutput.innerHTML = .25;
        aweighted = .25/1000;                    
        break;
    case '2':
        awoutput.innerHTML = .28;
        aweighted = .28/1000;                    
        break;
    case '3':
        awoutput.innerHTML = .30;
        aweighted = .30/1000;
        break;
    case '4':
        awoutput.innerHTML = .32;
        aweighted = .32/1000;
        break;
    case '5':
        awoutput.innerHTML = .36;
        aweighted = .36/1000;
        break;
    case '6':
        awoutput.innerHTML = .40;
        aweighted = .40/1000;
        break;
    case '7':
        awoutput.innerHTML = .42;
        aweighted = .42/1000;
        break;
    case '8':
        awoutput.innerHTML = .45;
        aweighted = .45/1000;
        break;
    case '9':
        awoutput.innerHTML = .48;
        aweighted = .48/1000;
        break;
    case '10':
        awoutput.innerHTML = .50;
        aweighted = .50/1000;
        break;
    case '11':
        awoutput.innerHTML = .52;
        aweighted = .52/1000;
        break;
    default:
        awoutput.innerHTML = .32;
        aweighted = .32/1000;
        break;
    }

    ajoules = (((1/2) * aweighted) * ((afps * 0.3048) ** 2));
    ajoutput.innerHTML = ajoules.toFixed(2);
    ajslider.value = ajoules;
    
    var newfps = (Math.sqrt((2*ajoules)/aweighted)) * 3.28084;
    afoutput.innerHTML = newfps.toFixed(0);
    afslider.value = newfps;
}

/* --------------------------------- target weight slider --------------------------------- */
atwoutput.innerHTML = aweighted*1000; //weight output
atwslider.oninput = function() 
{
    switch(atwslider.value) 
    {
    case '0':
        atwoutput.innerHTML = .20;
        anweighted = .20/1000;
        break;
    case '1':
        atwoutput.innerHTML = .25;
        anweighted = .25/1000;                    
        break;
    case '2':
        atwoutput.innerHTML = .28;
        anweighted = .28/1000;                    
        break;
    case '3':
        atwoutput.innerHTML = .30;
        anweighted = .30/1000;
        break;
    case '4':
        atwoutput.innerHTML = .32;
        anweighted = .32/1000;
        break;
    case '5':
        atwoutput.innerHTML = .36;
        anweighted = .36/1000;
        break;
    case '6':
        atwoutput.innerHTML = .40;
        anweighted = .40/1000;
        break;
    case '7':
        atwoutput.innerHTML = .42;
        anweighted = .42/1000;
        break;
    case '8':
        atwoutput.innerHTML = .45;
        anweighted = .45/1000;
        break;
    case '9':
        atwoutput.innerHTML = .48;
        anweighted = .48/1000;
        break;
    case '10':
        atwoutput.innerHTML = .50;
        anweighted = .50/1000;
        break;
    case '11':
        atwoutput.innerHTML = .52;
        anweighted = .52/1000;
        break;
    default:
        atwoutput.innerHTML = .32;
        anweighted = .32/1000;
        break;
    }

    amps = afps * .305;
    aAccelBase = (0.5 * aLength * amps * amps);
    aTimeBase = (2 * aLength/amps);
    aEnergyBase = (0.5 * aweighted * amps * amps);
    aBBAccel = (aweighted * aAccelBase/anweighted);
    aBBTime = (Math.sqrt(aAccelBase * aTimeBase * aTimeBase/aBBAccel));
    ajoules = (aBBTime * aEnergyBase/aTimeBase);
    ajoutput.innerHTML = ajoules.toFixed(2);
    ajslider.value = ajoules;

    
    var newfps = (Math.sqrt((2*ajoules)/anweighted)) * 3.28084;
    afoutput.innerHTML = newfps.toFixed(0);
    afslider.value = newfps;
}



/* --- FPS slider --- */
afoutput.innerHTML = afps;
afslider.oninput = function() 
{
    afps = this.value;
    afoutput.innerHTML = afps;

    ajoules = (((1/2) * aweighted) * ((afps * 0.3048) ** 2));
    ajoutput.innerHTML = ajoules.toFixed(2);
    ajslider.value = ajoules;
}

/* --- Joule Slider --- */
ajoutput.innerHTML = ajoules;
ajslider.oninput = function() 
{
    ajoules = this.value;
    ajoutput.innerHTML = ajoules;

    afps = (Math.sqrt((2*ajoules)/aweighted)) * 3.28084;
    afoutput.innerHTML = afps.toFixed(0);
    afslider.value = afps;
}