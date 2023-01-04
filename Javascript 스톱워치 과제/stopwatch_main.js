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
    const subCheck = document.querySelectorAll('.subcheck');
    if (allCheck.checked){
        for (let i = 0; i < subCheck.length; i++){
            subCheck[i].checked = true;
        }
    } else {
        for (let i = 0; i < subCheck.length; i++){
            subCheck[i].checked = false;
        }
    }

}

allClear.onclick = function(){
    const subCheck = document.querySelectorAll('.subcheck');
    for (let j = 0; j < subCheck.length; j++){
        if(subCheck[j].checked){
            subCheck[j].parentElement.remove();
        }
    }
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
                <input type="checkbox" class="subcheck">
                <div class="record_screen"> 
                    <div class="seconds">00</div>
                    <div>:</div>
                    <div class="milliseconds">00</div>
                </div>
            </li>
        `;
        let targetsecond = document.querySelector('.record_main').lastElementChild.querySelector('.seconds');
        let targetmillisec = document.querySelector('.record_main').lastElementChild.querySelector('.milliseconds');
        targetsecond.textContent = fillZero(sec)
        targetmillisec.textContent = fillZero(millisec)

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


