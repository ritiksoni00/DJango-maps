# DJango-maps

i this small proj i used my first AJAX call!

```py
  $.ajax({
          url: "{% url 'default' %}",
          method: 'post',
          beforeSend: function(xhr){xhr.setRequestHeader('X-CSRFToken', $("input[name='csrfmiddlewaretoken']").val());},
          data: {
            "place" : place
          },
          success: function(response){
            var obj = JSON.parse(response);
            console.log(obj)
            for(var i= 1;i<4;i++){
            $('#im'+[i]).html('<img src=' + obj[i]['fields']['img'] + '/>')}
            $('#place_name').html('<h3>'+ obj[1]['fields']['place'] + '</h3><p>'+ obj[0]['fields']['info_about_place']+'</p>')
      
           },
         });
```

this is what i wrote! 
