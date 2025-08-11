

// $(document).ready(function() {
//   $("#fadeBox").hide().fadeIn(2000);  // Fades in after page load
// });

// $(document).ready(function() {
//   $("#fadeBox").delay(3000).fadeOut(1000);  // Waits 3 sec, then fades out
// });

// Popup Notification
//  document.addEventListener('DOMContentLoaded', function () {
//         var msgModal = new bootstrap.Modal(document.getElementById('messageModal'));
//         msgModal.show();
//     });

//About page

 $(document).ready(function()
            {
                $("#1").mouseenter(function(){
                    $("#1").css("background-color","black");
                    $("").css("background","linear-gradient(45deg,var(--text-color))",
                                
                    )
                
              });
              
              $("#1").mouseleave(function(){
                    $("#1").css("background","");
                    $("h3").css("background","")
                
              });
               $("#2").mouseenter(function(){
                    $("#2").css("background-color","black");
                
              });
              
              $("#2").mouseleave(function(){
                    $("#2").css("background","");
                
              });
               $("#3").mouseenter(function(){
                    $("#3").css("background-color","black");
                
              });
              
              $("#3").mouseleave(function(){
                    $("#3").css("background","");
                
              });
               $("#4").mouseenter(function(){
                    $("#4").css("background-color","black");
                
              });
              
              $("#4").mouseleave(function(){
                    $("#4").css("background","");
                
              });

            }
        );

// Login_home


   $(document).ready(function(){
      $("#show").hide();
      $("#show2").hide();
      $("#show3").hide();
      $("#show4").hide();
      $("#show5").hide();
      $("#show6").hide();

      $("#open").click(function(){
         $("#show").show();
      });
      $("#close").click(function(){
         $("#show").hide();
      });
      $("#open").click(function(){
         $("#show").show();
      });
      $("#close").click(function(){
         $("#show").hide();
      });

      $("#open2").click(function(){
         $("#show2").show();
      });
      $("#close2").click(function(){
         $("#show2").hide();
      });

      $("#open3").click(function(){
         $("#show3").show();
      });
      $("#close3").click(function(){
         $("#show3").hide();
      });

      $("#open4").click(function(){
         $("#show4").show();
      });
      $("#close4").click(function(){
         $("#show4").hide();
      });

      $("#open5").click(function(){
         $("#show5").show();
      });
      $("#close5").click(function(){
         $("#show5").hide();
      });

      $("#open6").click(function(){
         $("#show6").show();
      });
      $("#close6").click(function(){
         $("#show6").hide();
      });
   })
