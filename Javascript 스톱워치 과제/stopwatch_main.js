let sec = 0;
let millisec = 0;

const screenSec = document.querySelector('.seconds');
const screenMillisec = document.querySelector('.milliseconds');
const startBtn = document.querySelector('.start');
const recordBox = document.querySelector('.record_main');
const stopBtn = document.querySelector('.stop');
const resetBtn = document.querySelector('.reset');
const allClear = document.querySelector('.all_clear');
const allCheck = document.querySelector('.allcheck');
let intervalId;


function fillZero(num) {
    return String(num).padStart(2, "0");
}

allCheck.onclick = function(){
    if (allCheck.checked){
        console.log('체크x->o')
    } else {
        console.log('체크o->x')
    }
}

allClear.onclick = function(){
    recordBox.innerHTML = ``
}

startBtn.onclick = function(){
    clearInterval(intervalId)
    intervalId = setInterval(operateTimer, 10)
}

stopBtn.onclick = function(){
    clearInterval(intervalId)

    if (sec != 0 || millisec != 0) {
        recordBox.innerHTML += `
            <li class="record_time">
                <input type="checkbox" id="subcheck">
                <div class="record_screen">
                    <div class="seconds">00</div>
                    <div>:</div>
                    <div class="milliseconds">00</div>
                </div>
            </li>
        `;
    }
}

resetBtn.onclick = function(){
    clearInterval(intervalId)
    millisec = 0; sec = 0;
    screenMillisec.textContent = "00"
    screenSec.textContent = "00"
}

function operateTimer(){
    millisec++;
    screenMillisec.textContent = fillZero(millisec)
    if (millisec > 99) {
        sec++;
        screenSec.textContent = fillZero(sec)
        millisec = 0;
        screenMillisec.textContent = fillZero(millisec)
    }
}


