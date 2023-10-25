var date = new Date()
let display_date = "Fecha: " + date.toLocaleDateString()

$(document).ready(function(){
    $("#display-date").html(display_date)
})

let predicted_emotion

$(function(){
    $("#predict-button").click(function (){
        let input_data = {
            "text": $("#text").val()
        }
        console.log(input_data)

        $.ajax({
            type: 'POST',
            url: "/predict-emotion",
            data: JSON.stringify(input_data),
            dataType: "json",
            contentType: "application/json",
            success: function(result) {
                predicted_emotion = result.data.predicted_emotion
                emo_url = result.data.predicted_emotion_img_url

                $("#prediction").html(predicted_emotion)
                $("#prediction").css("display", "block")

                $("#emo-img-url").attr('src', emo_url)
                $("#emo-img-url").css("display", "block")
            },
            error: function (result) {
                alert(result.responseJSON.message)
            }
        })
    })
})