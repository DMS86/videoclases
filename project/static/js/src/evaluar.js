/**
 *  ViewModel for the evaluar template, using Knockout.js
 */

function viewModel() {
    var self = this;

    self.responseValues = new ResponseValues();

    self.correctAnswer = ko.observable(false);
    self.wrongAnswer = ko.observable(false);
    self.correctAnswerText = ko.observable("");

    self.url = ko.observable(window.location.pathname);
    self.valor = ko.computed(function() { return self.responseValues.valor(); });
    self.respuesta = ko.observable();
    self.thumbUp = ko.computed(function() { 
        if (parseInt(self.valor()) == 1) {
            return self.responseValues.thumbUpGreen(); 
        } else {
            return self.responseValues.thumbUpGray(); 
        }
    });
    self.thumbDown = ko.computed(function() { 
        if (parseInt(self.valor()) == -1) {
            return self.responseValues.thumbDownRed(); 
        } else {
            return self.responseValues.thumbDownGray(); 
        }
    });

    self.clickSiguienteVideoclase = function() {
        if (self.respuesta() == undefined) {
            alert("Debes seleccionar una respuesta");
            return;
        }
        self.submitRespuestaDeAlumno();
    }

    self.evaluar = function(valor) {
        self.responseValues.valor(valor);
    }

    self.submitEvaluacionDeAlumno = function(data, event) {
        var fd = new FormData();
        fd.append("valor", parseInt(self.valor()));
        fd.append("videoclase", parseInt(self.responseValues.videoclase()));
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        return $.ajax('/alumno/evaluar-video/' + self.responseValues.evaluacion() + '/', {
            data: fd,
            type: "post",
            processData: false,
            contentType: false,
            success: function(response){
            }
        });
    }

    self.submitRespuestaDeAlumno = function() {
        var fd = new FormData();
        fd.append("respuesta", self.respuesta());
        fd.append("videoclase", self.responseValues.videoclase());
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        console.log(self.respuesta());
        console.log(self.responseValues.videoclase());
        return $.ajax('/alumno/evaluar-videoclase-form/', {
            data: fd,
            type: "post",
            processData: false,
            contentType: false,
            success: function(response){
                console.log(response);
                if (response.success) {
                    if (response.is_correct) {
                        self.correctAnswer(true);
                    } else {
                        self.correctAnswerText(response.correct_answer);
                        self.wrongAnswer(true);
                    }
                    setTimeout(function() { location.reload(); }, 2500);
                }
            }
        });
    }
}

var vm = new viewModel();