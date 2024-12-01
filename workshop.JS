$(document).ready(function() {  
    $("#play-button").click(function() {  
      
     $("#claw-machine-sound").play();  
      
     $.post("/play", function(data) {  
      
      $("#cat-name").text(data.cat);  
      $("#cat-image").attr("src", data.cat_info.image);  
      $("#cat-info").html(`  
        <p>First Name: ${data.cat_info.first_name}</p>  
        <p>Last Name: ${data.cat_info.last_name}</p>  
        <p>Birthday: ${data.cat_info.birthday}</p>  
        <p>Age: ${data.cat_info.age}</p>  
        <p>Favorite Activities: ${data.cat_info.favorite_activities}</p>  
        <p>Species/Breed: ${data.cat_info.species_breed}</p>  
        <p>Background Info: ${data.cat_info.background_info}</p>  
      `);  
     });  
    });  
  });
  