/*
const texts = document.querySelector('.texts');

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

//To wait till we stop talking
recognition.interimResults = true;

//recognition.continuous = true;

//let p = document.createElement('p');

/*
var msg = document.getElementById("output").innerText;
if (msg != ""){
    responsiveVoice.speak(msg);
}
*/

/*
function speakText(){
    alert("Speak Text Function");
    var msg = document.getElementById('output').innerText;
    if(msg != ''){
        responsiveVoice.speak(msg);
        alert(msg);
        document.getElementById('output').innerText = '';
    }
}
*'/

//speakText();

recognition.addEventListener('result', (e) => {

    /*
    var msg = document.getElementById('output').innerText;
    if(msg != ''){
        speakText(msg);
        document.getElementById('output').innerText = '';
    }
    *'/

    const text = Array.from(e.results).map(result => result[0]).map(result => result.transcript).join('');

    //p.innerText = text;
    //texts.appendChild(p);

    //document.getElementById("temp").value = text;

    /*
    if(e.results[0].isFinal){
        /*
        if(text.includes('hello')){
            p = document.createElement('p');
            p.classList.add('reply');
            p.innerText = "Hi";
            texts.appendChild(p);
        }

        p = document.createElement('p');
    }
    *'/

    document.getElementById("passer").value = text;
    /*
    var msg = document.getElementById('output').innerText;
    if(msg != ''){
        speakText(msg);
    }
    *'/

    //console.log(text);


    if(e.results[0].isFinal){

        document.getElementById("formButton").click();
        window.alert("Form submitted");
    }



})

$("form").submit(function(event){
                event.preventDefault();
                $.ajax({
                        url:"{% url 'runTrial' %}",
                        type:'post',
                        data:{
                            Data:$('#passer').val(),
                            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                        },
                        success:function(response){
                            var success = response['success']
                            if(success){
                                document.getElementById('output').innerText = response['msg'];
                            }else{
                                window.alert("request not going successfuly");
                            }
                        },
                        failure:function(error){
                            alert("error occurred while request");
                        }
                });
            })

recognition.addEventListener('end', ()=>{

    /*
    if(document.getElementById("passer").value != "Default"){
        document.getElementById("commandForm").submit();
    }
    */

    /*
    if(document.getElementById("passer").value != "Default"){
        window.alert("Submitted");
        document.getElementById("formButton").click();
    }
    *'/

    //speakText();
    recognition.start();
})

recognition.start();
*/
//document.getElementById("passer").value = text;