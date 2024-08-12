// get started form

function writetousbtn(){

 var fname = document.getElementById("fname").value.trim();
 var femail = document.getElementById("femail").value.trim();
 var fphone = document.getElementById("fphone").value.trim();

if(fname === ''){
    alert("Name Field Required");
    return;
}
if(femail === ''){
    alert("Email Field Required");
    return;
}
if (!isValidEmail(femail)) {
    alert("Invalid Email Format");
    return;
}

if(fphone === ''){
    alert("Phone Field Required");
    return;
}

if (!isValidPhone(fphone)) {
    alert("Invalid Phone Number Format");
    return;
}



    let formdata = {
        fname: fname,
        femail: femail,
        fphone: fphone,
    };

    let formDataJson = JSON.stringify(formdata);
    localStorage.setItem('formdata', formDataJson);
    window.location.href = 'questions/';

}
function isValidEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}
function isValidPhone(phone) {
    const phonePattern = /^\d{10}$/; // Adjust pattern according to your requirement
    return phonePattern.test(phone);
}



$(document).ready(function(){
    $('#allformssubmit').click(function(event){
        event.preventDefault();
        let brandpositionradio = $('input[name="brandpositionradio"]:checked').val();
        let mission = $('#mission').val()
        let brandtargetradio = $('input[name="brandtargetradio"]:checked').val();
        let engagebrandradio = $('input[name="engagebrandradio"]:checked').val();
        let brandperform = $('#brandperform').val()
        let brandchallenge = $('#brandchallenge').val()
        // let brandcheck = $('input[name=brandcheck]:checked').map(function(){
        //     return $(this).val();
        // }).get();
        var motivations = [];
        $('input[name="brandcheck"]:checked').each(function() {
            motivations.push($(this).val());
        });
        let achieve = $('#achieve').val()
        let brandexpectation = $('#brandexpectation').val()
        let storedFormDataJson = localStorage.getItem('formdata');
        let storedFormData = JSON.parse(storedFormDataJson);
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
        
        



        let data = new FormData();
        data.append('brandposition',brandpositionradio),
        data.append('corevalue',mission),
        data.append('brandtarget',brandtargetradio),
        data.append('customerfeedback',engagebrandradio),
        data.append('brandperform',brandperform),
        data.append('brandchallenge',brandchallenge),
        data.append('brandcheck',motivations),
        data.append('achieve',achieve),
        data.append('brandexpectation',brandexpectation),
        data.append('storedFormData', JSON.stringify(storedFormData));
        data.append('csrfmiddlewaretoken',csrfmiddlewaretoken),

        $.ajax({
            url:"/questions/",
            method: 'POST',
            processData:false,
            contentType:false,
            cache:false,
            data:data,
            success:function(data, status,xhr){
                $('#userAccountSetupForm')[0].reset();
                if(data.success === true){
                    alert("All Done.Thank You")
                    window.location.href ='/';
                }else{
                    alert(data.error)
                    window.location.href = '/questions/'
                }
            },
            error:function(data){
                alert("fail, submitted data")
            }
            
        })

    })
    
})


// Select all checkboxes
document.getElementById('checkall').addEventListener('change', function () {
    const checkboxes = document.querySelectorAll('input[name="brandcheck"]');
    checkboxes.forEach((checkbox) => {
        checkbox.checked = this.checked;
    });
});


// Enable/disable Next button based on input validation
document.querySelectorAll('input[type="text"], textarea').forEach((input) => {
    input.addEventListener('input', function () {
        const nextBtn = document.querySelector(`button[step_number="${currentStep + 1}"]`);
        if (this.value.trim() !== '') {
            nextBtn.disabled = true;
        } else {
            nextBtn.disabled = false;
        }
    });
});


