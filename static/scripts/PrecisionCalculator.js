var InputWeight = document.getElementById("pweight");
var InputFPS = document.getElementById("PFPS");
var InputJoules = document.getElementById("pJoules");
var creepS = document.getElementById("pcswitch");
var cout = document.getElementById("pcsout");

//------- default variables ---------
var pLength = .36;
var pjoules = 1.43;
var pfps = 310;
var pweight = .32/1000;

//----- advanced calculation variables ------
var pmps; //mps derived from fps input
var pAccelBase; //base acceleration calculated
var pTimeBase; //base time calculated
var pMassBase = .32/1000; //base mass for joule creep
var pEnergyBase; //base energy calculated for joule creep

//----- advanced bb calculated variables ------
var pBBAccel;
var pBBTime;

/*
creepS.onclick = function()
{
    var newVal;
    if (this.value == 0)
    {
        newVal = 1;
        cout.innerHTML = "True";
    }
    else
    {
        newVal = 0;
        cout.innerHTML = "False";
    }
    this.value = newVal;
}

creepS.oninput = function()
{
    var newVal;
    if (this.value == 0)
    {
        newVal = 1;
        cout.innerHTML = "True";
    }
    else
    {
        newVal = 0;
        cout.innerHTML = "False";
    }
    this.value = newVal;
} */

InputWeight.onchange = function()
{
    pweight = InputWeight.value/1000;
    if(creepS.value == 0)
    {
        pjoules = (((1/2) * pweight) * ((pfps * 0.3048) ** 2));
        pjoules = pjoules.toFixed(2);
        InputJoules.value = pjoules;
    }
    else
    {
        pmps = pfps * .305;
        pAccelBase = (0.5 * pLength * pmps * pmps);
        pTimeBase = (2 * pLength/pmps);
        pEnergyBase = (0.5 * pMassBase * pmps * pmps);
        pBBAccel = (pMassBase * pAccelBase/pweight);
        pBBTime = (Math.sqrt(pAccelBase * pTimeBase * pTimeBase/pBBAccel));
        pjoules = (pBBTime * pEnergyBase/pTimeBase);
        InputJoules.value = pjoules.toFixed(2);
        
        var newfps = (Math.sqrt((2*pjoules)/pweight)) * 3.28084;
        InputFPS = newfps.toFixed(0);
    }
}

InputFPS.oninput = function()
{
    if(creepS.value == 0)
    {
        pfps = this.value;
        pjoules = (((1/2) * pweight) * ((pfps * 0.3048) ** 2));
        pjoules = pjoules.toFixed(2);
        InputJoules.value = pjoules;
    }
    else
    {
        pfps = this.value;
        pmps = pfps * .305;
        pAccelBase = (0.5 * pLength * pmps * pmps);
        pTimeBase = (2 * pLength/pmps);
        pEnergyBase = (0.5 * pMassBase * pmps * pmps);
        pBBAccel = (pMassBase * pAccelBase/aweighted);
        pBBTime = (Math.sqrt(pAccelBase * pTimeBase * pTimeBase/pBBAccel));
        pjoules = (pBBTime * pEnergyBase/pTimeBase);
        InputJoules = pjoules.toFixed(2);
    }
}

InputJoules.oninput = function()
{
    if(creepS.value == 0)
    {
        pjoules = InputJoules.value;
        pfps = (Math.sqrt((2*pjoules)/pweight)) * 3.28084;
        InputFPS.value = pfps.toFixed(0);
    }
    else
        InputJoules.value = pjoules;
}